from time import sleep

from screenshot_service.celery import app
from logs.settings import setup_logger
from .models import Task
from .utils import check_url, following_to_links
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from webdriver_manager.chrome import ChromeDriverManager

log = setup_logger()


@app.task(name='parse')
def parse(url: str, depth: int):
    log.info(f'create new task. args: url - {url}, depth - {depth}')
    task_id = parse.request.id
    task = Task(
        task_id=task_id,
        url=url,
        depth=depth
    )
    task.save()

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    following_to_links(driver, task, [url, ], max_depth=int(depth))
    driver.close()
