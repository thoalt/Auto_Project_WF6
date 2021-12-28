import logging
import inspect
from utilites import global_dir
import os

class Loggen:
    def __init__(self):
        logfile_name = "Automation.log"
        self.log_path = os.path.join(global_dir.LOG_FILES_PATH, logfile_name)

    #@staticmethod
    def loggen(self, logLevel=logging.DEBUG):
        # Set class/method name from where ít called
        logger_name = inspect.stack()[1][3]

        # Create Logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)

        # Create console handler or file handler and set the log level
        fh = logging.FileHandler(self.log_path, mode='a')

        # Create Formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s -%(name)s : %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

        # Add formatter to console or file handler
        fh.setFormatter(formatter)

        # Add console handler to logger
        logger.addHandler(fh)
        return logger