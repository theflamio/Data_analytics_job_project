# python/transformer.py

def transform_data(data):
    """
    Function to transform the extracted data.
    Replace this with your actual data transformation logic.
    """
    print("Transforming data...")
    transformed_data = []
    for entry in data:
        transformed_entry = {
            'id': entry['id'],
            'name': entry['name'].upper(),
            'age_group': 'Young' if entry['age'] < 30 else 'Adult'
        }
        transformed_data.append(transformed_entry)
    return transformed_data
