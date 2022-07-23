import sys

from loguru import logger

from app.config.config import get_configs

configs = get_configs()


class Loguru:

    def __init__(self):
        pass

    @staticmethod
    def init_log(filename):
        sink_type = sys.stderr

        if configs.is_system_logging_enabled:
            sink_type = sys.stderr

        if configs.is_file_logging_enabled:
            sink_type = "/filmIndustry/logs/" + filename + ".log"

        logger.remove()
        logger.add(sink_type, format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}", backtrace=True,
                   diagnose=True, enqueue=True, catch=True, rotation="10 MB")

    @staticmethod
    def log(message: str, level: str = "DEBUG"):
        logger.log(level, message)
