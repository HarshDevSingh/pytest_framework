import logging
import inspect
from datetime import datetime


class Logger:

    @staticmethod
    def logger(log_level=logging.INFO):
        frame = inspect.currentframe().f_back
        name = frame.f_code.co_name
        logger = logging.getLogger(name)
        logger.setLevel(log_level)
        file_handler = logging.FileHandler(f"logs/log-{str(datetime.now().strftime('%Y-%m-%d:%H:%M'))}.log", mode="w")
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] : %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
