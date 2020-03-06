from pytest_bdd import given, then, when, parsers, scenarios

from core.testlib.steps.auth_steps.login_steps import LoginSteps
from core.testlib.steps.steps_mapping import STEPS
from core.testlib.steps.main_page_steps import MainPageSteps

LOGIN_STEPS = LoginSteps()
MAIN_PAGE_STEPS = MainPageSteps()

scenarios('features')


@given(parsers.parse('{page} page is opened'))
def navigate_page(page):
    STEPS.get(page)().navigate()


@when('user is not logged in')
def check_user_is_not_logged_in():
    LOGIN_STEPS.is_login_page()


@then('check that logged in')
def check_user_is_logged_in():
    LOGIN_STEPS.is_logged_in()


@then(parsers.parse('login as {account_type}'))
def login_as_user(account_type):
    LOGIN_STEPS.login(account_type)


@then("I can see the <element>")
def element_is_displayed(element):
    MAIN_PAGE_STEPS.check_element_is_displayed(element)
