""" Main script for the ETL process. """
from extractor import extract_data
from transformer import transform_data
from loader import load_data
from config import DATABASE_URL


def main():
    """
    Main function for the ETL process.
    """
    # Extract data
    print("Extracting data...")
    data = extract_data()

    # Transform data
    print("Transforming data...")
    transformed_data = transform_data(data)

    # Load data
    print("Loading data into database...")
    load_data(transformed_data, DATABASE_URL)

    print("ETL process completed successfully!")

if __name__ == "__main__":
    main()