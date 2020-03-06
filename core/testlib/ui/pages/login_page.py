from selene.support.shared import browser

from core.testlib.helpers import by
from core.testlib.ui.base_page import BasePage
from core.testlib.ui.blocks.header_block import Header


class LoginPage(Header, BasePage):
    path = ''

    email_field = browser.element(by.name('email'))
    password_field = browser.element(by.name('password'))
    do_not_remember_your_password_btn = browser.element(by.class_name('auth0-lock-input-wrap'))
    show_password_btn = browser.element(by.xpath("//label[@title='Show password']"))
