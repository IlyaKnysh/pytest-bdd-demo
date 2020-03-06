from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from .driver_config import BROWSER, REMOTE_IP, REMOTE_PORT

BROWSERS = {
    'chrome': webdriver.Chrome,
    'remote': webdriver.Remote
}


class Driver:
    def __init__(self, **kwgs):
        self.kwgs = kwgs
        if BROWSER == 'chrome':
            self.kwgs['executable_path'] = ChromeDriverManager().install()
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            self.kwgs['options'] = options

        if BROWSER == 'remote':
            self.kwgs['command_executor'] = f'http://{REMOTE_IP}:{REMOTE_PORT}/wd/hub'
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            self.kwgs['desired_capabilities'] = options.to_capabilities()

    def start(self):
        driver = BROWSERS[BROWSER](**self.kwgs)
        return driver
