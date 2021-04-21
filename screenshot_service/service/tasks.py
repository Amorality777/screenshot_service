from time import sleep

from celery.result import AsyncResult
from screenshot_service.celery import app
from logs.settings import setup_logger

log = setup_logger()


@app.task(name='parse')
def parse(url: str, depth: int):
    log.info(f'create new task. args: url - {url}, depth - {depth}')
    task_id = parse.request.id
