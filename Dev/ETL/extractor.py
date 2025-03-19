""" extractor module to extract data from a source. """
import polars as pl
from kaggle_api_handler import KaggleAPIHandler

def extract_data():
    """
    Function to extract data from a source.
    """
    config_dir = r'C:\Dev\Data_Analytics_jobproject\Dev\TestScripts\TestScripts\kaggle'
    dataset_name = 'lukebarousse/data-analyst-job-postings-google-search'
    save_dir = './Dev/datasets'

    # Create an instance of KaggleAPIHandler
    kaggle_handler = KaggleAPIHandler(config_dir)

    # Call the download_dataset method
    kaggle_handler.download_dataset(dataset_name, save_dir)

    data = pl.read_csv('./Dev/datasets/gsearch_jobs.csv', sep="\t",)
    return data
