import logging

from core.config.env import DEBUG

logging_level = logging.DEBUG if DEBUG else logging.INFO

logger = logging.getLogger(__name__)
logger.setLevel(logging_level)

formatter = logging.Formatter('%(asctime)s %(name)-5s %(levelname)-8s %(message)s')

console = logging.StreamHandler()
console.setLevel(logging_level)
console.setFormatter(formatter)

logger.addHandler(console)
