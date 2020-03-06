import os

from selene.support.shared import browser

from core.config.env import PROJECT_DIRECTORY
from . import env

browser.config.timeout = int(env.get('UI_TIMEOUT', 5))

browser.config.reports_folder = os.path.join(PROJECT_DIRECTORY, 'reports')

BROWSER = env.get('BROWSER', 'chrome')
REMOTE_IP = env.get('REMOTE_IP', '127.0.0.1')
REMOTE_PORT = env.get('REMOTE_IP', '4444')
