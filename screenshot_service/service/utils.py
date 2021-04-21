from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from logs.settings import setup_logger

log = setup_logger()


class Parser:

    def __init__(self, url, depth):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.url = url
        self.depth = depth
        self.links = []

    def run(self):
        links = self.get_links(self.url)
        for link in links:
            log.debug(link.text)

    def get_links(self, url: str):
        self.driver.get(url)
        return self.driver.find_elements_by_class_name(name='a')
#
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://translate.google.com/')