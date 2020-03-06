from selene.support.shared import browser


class BaseSteps:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        browser.driver.get(f'{self.page.path}{self.page.url}')
