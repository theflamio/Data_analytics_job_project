"""
Module: kaggle_api_handler

This module provides a class for handling interactions with the Kaggle API.
"""

import os
from kaggle.api.kaggle_api_extended import KaggleApi

class KaggleAPIHandler:
    """A class for handling Kaggle API interactions."""

    def __init__(self, config_dir):
        """
        Initialize the Kaggle API handler.

        Parameters:
        - config_dir (str): The directory path containing Kaggle API credentials.
        """
        # Set the path for your Kaggle API credentials
        os.environ['KAGGLE_CONFIG_DIR'] = config_dir
        # Instantiate the Kaggle API
        self.api = KaggleApi()
        # Authenticate with your Kaggle API credentials
        self.api.authenticate()

    def download_dataset(self, dataset_name, save_dir):
        """
        Download a dataset from Kaggle.

        Parameters:
        - dataset_name (str): The name of the dataset on Kaggle.
        - save_dir (str): The directory path where the dataset will be saved.
        """
        try:
            # Create the directory if it doesn't exist
            os.makedirs(save_dir, exist_ok=True)
            # Download the dataset
            self.api.dataset_download_files(dataset_name, path=save_dir, unzip=True)
            print("Dataset downloaded successfully.")
        except FileNotFoundError as e:
            print(f"Directory not found: {e}")
        except PermissionError as e:
            print(f"Permission denied: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
