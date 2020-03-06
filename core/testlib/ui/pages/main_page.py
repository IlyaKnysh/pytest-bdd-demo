from selene.support.shared import browser

from core.testlib.helpers import by
from core.testlib.ui.base_page import BasePage
from core.testlib.ui.blocks.header_block import Header


class MainPage(Header, BasePage):
    path = ''

    edit_all = browser.element(by.xpath("//small[text()='Edit All']"))
    clear_all = browser.element(by.xpath("//small[text()='Clear All']"))
    list_vew = browser.element(by.xpath("//button[contains(text(),'List View')]"))
    search_field = browser.element(by.name("searchText"))
    sort_by = browser.element(by.xpath("//span[text()='Sort By']"))
