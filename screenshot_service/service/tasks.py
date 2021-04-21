from screenshot_service.logs.settings import setup_logger

log = setup_logger()


def create_task(url: str, depth: int):
    log.info(f'create new task. args: url - {url}, depth - {depth}')
