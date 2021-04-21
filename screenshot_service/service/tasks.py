from time import sleep

from screenshot_service.celery import app
from logs.settings import setup_logger

log = setup_logger()


@app.task
def create_task(url: str, depth: int):
    log.info(f'create new task. args: url - {url}, depth - {depth}')
    sleep(10)
    log.info('Task completed')
