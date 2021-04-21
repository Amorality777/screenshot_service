from time import sleep

from screenshot_service.celery import app
from logs.settings import setup_logger
from .utils import Parser
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager

log = setup_logger()


@app.task(name='parse')
def parse(url: str, depth: int):
    log.info(f'create new task. args: url - {url}, depth - {depth}')
    task_id = parse.request.id

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://ru.hexlet.io/programs')
    img = driver.save_screenshot('1.png')
    log.info(img)
    elements = driver.find_elements_by_tag_name('a')
    links = [element.get_attribute('href') for element in elements]
    for link in links:
        try:
            log.info(link)
            driver.get(link)
        except Exception as e:
            log.error(e)
    log.info('completed')
    driver.close()
