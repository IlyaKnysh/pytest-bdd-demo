from selene.support.shared import browser

from core.testlib.helpers.logger import logger


def check_if_browser_log_has_errors():
    full_log = browser.driver.get_log('browser')
    errors = [x for x in full_log if x.get('level') == 'SEVERE']
    if errors:
        for error in errors:
            logger.error(f'JS ERROR:\n{error}\n')
        return errors
    return False
