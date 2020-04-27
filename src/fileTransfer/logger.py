"""
#-----------------------------------------------------------------------------
# Name: logger.py
#
# Description: Import for logging
#
# Arguments: log_dir, log_level, log_days, log_name
#
# Authors: Franke Morris and Devan Lorenson
#
# Version: 1.0.0
#
# Date: 24 Oct 2019
#-----------------------------------------------------------------------------
# Update History
#
# Version      Date        Who              What Changed
#-----------------------------------------------------------------------------
"""
import os
import time
import logging
from datetime import date

class Logger:
    """Class used for logging"""

    def __init__(self, log_dir, log_level, log_days, log_name):
        self.log_dir = log_dir
        self.log_level = log_level
        self.log_days = log_days
        self.log_name = log_name

    def get_logger(self):
        """Method to setup log file"""
        logger = logging.getLogger(self.log_name)
        logger.setLevel(self.log_level)

        today = date.today().strftime('%Y%m%d')
        today_file = self.log_name + '.' + today + '.log'
        file_handler = logging.FileHandler(self.log_dir + '/' + today_file)

        format1 = logging.Formatter('%(asctime)s:Line %(lineno)d:%(levelname)s:%(message)s')
        file_handler.setFormatter(format1)

        logger.addHandler(file_handler)

        self.delete_log_files(logger)

        return logger

    def delete_log_files(self, logger):
        """Delete log files if older than # of days defined in properties file."""

        now = time.time()
        for _x in os.listdir(self.log_dir):
            if self.log_name in _x:
                if os.stat(os.path.join(self.log_dir, _x)).st_mtime < now - self.log_days * 86400:
                    logger.debug('Removing log file : %s', _x)
                    os.remove(self.log_dir + '/' + _x)
                else:
                    logger.debug('NOT removing log file : %s', _x)
