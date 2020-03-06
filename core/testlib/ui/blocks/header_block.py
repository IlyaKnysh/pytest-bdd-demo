from selene.support.shared import browser

from core.testlib.helpers import by


class Header:
    surveillance_tab = browser.element(by.xpath("//a[text()='Surveillance']"))
    logout_btn = browser.element(by.xpath("//a[text()='Logout']"))