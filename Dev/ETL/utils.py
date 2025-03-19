# python/utils.py

import logging

def setup_logging(log_file):
    """
    Function to set up logging configuration.
    """
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(message):
    """
    Function to log informational messages. Confirmation that things are working as expected.
    """
    logging.info(message)

def log_error(message):
    """
    Function to log error messages. A more serious problem that prevents the program from working as expected. 
    """
    logging.error(message)
