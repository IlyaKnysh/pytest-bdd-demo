from hamcrest import assert_that
from selene.support.conditions.be import visible

from core.testlib.steps.base_steps import BaseSteps
from core.testlib.ui.pages.main_page import MainPage


class MainPageSteps(BaseSteps):
    def __init__(self):
        super().__init__(MainPage)

    def check_element_is_displayed(self, element_):
        """check that element is displayed"""
        assert_that(getattr(self.page, element_).should(visible), 'Element is displayed')
