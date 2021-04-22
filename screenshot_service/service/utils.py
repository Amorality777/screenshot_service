import os

from selenium.common.exceptions import StaleElementReferenceException
from logs.settings import setup_logger
from screenshot_service.settings import MEDIA_ROOT
from service.models import Screenshot

log = setup_logger()


def check_url(url):
    return isinstance(url, str) and url.count('.')


def following_to_links(driver, task, links, max_depth, depth=1):
    if depth > max_depth:
        log.info('return')
        return
    for num, link in enumerate(links):
        if not check_url(link):
            continue
        try:
            driver.get(link)
            path = os.path.join(MEDIA_ROOT, f'task_{task.id}', f'depth_{depth}')
            os.makedirs(path, exist_ok=True)
            screenshot = Screenshot(task=task)
            screenshot.save()
            full_path = os.path.join(path, f'link_{screenshot.id}.png')
            driver.save_screenshot(full_path)
            screenshot.image = os.path.join(f'task_{task.id}', f'depth_{depth}', f'link_{screenshot.id}.png')
            screenshot.save()
            log.debug(f'{link} {max_depth} {depth}')
            elements = driver.find_elements_by_tag_name('a')
            """Если не преобразовать в список, возвращает ошибку"""
            new_links = [element.get_attribute('href') for element in elements]
            if depth >= max_depth:
                continue
            following_to_links(driver, task, new_links, max_depth, depth + 1)
        except StaleElementReferenceException as e:
            log.error(e)
            continue
