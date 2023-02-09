import logging
import inspect
from datetime import datetime


class Logger:

    @staticmethod
    def logger(log_level=logging.INFO):
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logger.setLevel(log_level)
        file_handler = logging.FileHandler(f"{str(datetime.now())[:-7]}.log", mode="w")
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] [%(name)s] : %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
