# Method 1: Logging

import logging

_var = 121

logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S',
    level=logging.DEBUG)

logger = logging.getLogger(__name__)
logger.debug("This is a debug log")
logger.info("This is an info log")
logger.critical("This is critical")
logger.error("An error occurred")

logging.info(f"value of _var variable is {_var} only...")


# Method 2: By logger

from loguru import logger
logger.info(f"value of _var variable is {_var} only...")

