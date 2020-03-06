from hamcrest import assert_that
from selene.support.conditions.be import visible

from core.config.env import USERS
from core.testlib.steps.base_steps import BaseSteps
from core.testlib.ui.pages.login_page import LoginPage


class LoginSteps(BaseSteps):
    def __init__(self):
        super().__init__(LoginPage)

    def login(self, account_type):
        """login by credentials"""
        account = USERS.get(account_type)
        self.page.email_field.send_keys(account.email)
        self.page.password_field.send_keys(account.password).submit()

    def is_login_page(self):
        """check that current page is login page"""
        assert_that(self.page.do_not_remember_your_password_btn.should(visible), "Seems like it's not login page")

    def is_logged_in(self):
        """check that we are on the main page and successfully logged in"""
        assert_that(self.page.welcome_string.should(visible), "Main page was not opened")