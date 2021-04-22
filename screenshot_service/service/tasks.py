from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from django_celery_results.models import TaskResult
from logs.settings import setup_logger
from screenshot_service.celery import app
from .utils import following_to_links

log = setup_logger()


@app.task(name='parse')
def parse(url: str, depth: int):
    log.info(f'create new task. args: url - {url}, depth - {depth}')
    task_id = parse.request.id
    task = TaskResult.objects.get(task_id=task_id)

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

    following_to_links(driver, task, [url, ], max_depth=int(depth))
    driver.close()
