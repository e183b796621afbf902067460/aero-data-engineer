import sys

from loguru import logger

logger.remove(0)
log = logger

log.add(
    sys.stdout,
    format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}",
)
log.add(
    sys.stderr,
    format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}",
)
