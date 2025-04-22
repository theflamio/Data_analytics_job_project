"""
logger_Helper.py

This module provides a LoggerHelper class to easily set up a rotating logger
in Python applications. The logger rotates based on file size, maintains a limited
number of backups, and automatically deletes old log files after a retention period
(number of days).

Features:
- File size-based log rotation
- Backup file retention
- Automatic cleanup of old log files
- Easy to integrate into any Python project

Usage:
    from loggerHelper import LoggerHelper

    logHelper = LoggerHelper()
    logger = logHelper.get_logger()

    logger.info("Application started")

Author: [Your Name]
Date: 2025-04-22
"""

import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime, timedelta

class LoggerHelper:
    """
    A helper class for setting up and managing a rotating logger with file size limit
    and log file retention based on age.

    Attributes:
        log_dir (str): Directory to store log files.
        log_file (str): Base name of the log file.
        max_bytes (int): Maximum size in bytes before rotating the log file.
        backup_count (int): Number of backup files to keep.
        retention_days (int): Number of days to retain old log files.
    """

    def __init__(self, log_dir='logs', log_file='app.log', max_bytes=10*1024*1024, backup_count=10, retention_days=14):
        """
        Initializes the LoggerHelper with specified configuration.

        Args:
            log_dir (str): Directory where log files will be stored.
            log_file (str): Name of the main log file.
            max_bytes (int): Maximum size of a log file in bytes before rotation.
            backup_count (int): Number of rotated log files to keep.
            retention_days (int): Number of days to retain log files.
        """
        self.log_dir = log_dir
        self.log_file = log_file
        self.max_bytes = max_bytes
        self.backup_count = backup_count
        self.retention_days = retention_days

        os.makedirs(self.log_dir, exist_ok=True)
        self.logger = self._setup_logger()

    def _setup_logger(self):
        """
        Sets up the logger with a RotatingFileHandler and appropriate formatting.

        Returns:
            logging.Logger: Configured logger instance.
        """
        logger = logging.getLogger('AppLogger')
        logger.setLevel(logging.DEBUG)

        log_path = os.path.join(self.log_dir, self.log_file)

        handler = RotatingFileHandler(log_path, maxBytes=self.max_bytes, backupCount=self.backup_count)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        if not logger.hasHandlers():
            logger.addHandler(handler)

        return logger

    def get_logger(self):
        """
        Returns the configured logger after performing log cleanup.

        Returns:
            logging.Logger: The logger instance.
        """
        self._cleanup_old_logs()
        return self.logger

    def _cleanup_old_logs(self):
        """
        Deletes log files in the log directory that are older than the retention period.
        """
        now = datetime.now()
        for filename in os.listdir(self.log_dir):
            file_path = os.path.join(self.log_dir, filename)
            if os.path.isfile(file_path):
                file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                if now - file_time > timedelta(days=self.retention_days):
                    os.remove(file_path)
