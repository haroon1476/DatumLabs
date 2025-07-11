import pandas as pd
import json
import logging

# Setting up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to recursively flatten a nested dictionary
def flatten_json(nested_json, parent_key='', sep='_'):
    # Flatenning a nested dictionary
    items = []
    for k, v in nested_json.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):  # If the value is a nested dictionary, recursively flatten it
            items.extend(flatten_json(v, new_key, sep=sep).items())
        elif isinstance(v, list):  # If the value is a list, iterate over the list and add indexed columns
            for i, sub_item in enumerate(v):
                items.extend(flatten_json({f"{k}_{i+1}": sub_item}, '', sep=sep).items())
        else:  # Else its a single value, so no need to do anything to it
            items.append((new_key, v))
    return dict(items)

def ConvertJsonToCsv(filename):
    try:
        logging.info(f"Now opening the file '{filename}'")

        with open(filename, 'r') as file:
            data = json.load(file)
            print(data)
            logging.info(f"Successfully loaded JSON data from '{filename}'.")

    except FileNotFoundError:
        logging.error(f"Error: The file '{filename}' was not found.")
        return None
    except json.JSONDecodeError:
        # if the format of json file is invalid
        logging.error(f"Error: The file '{filename}' contains invalid JSON.")
        return None

    # Flattening each JSON record and collecting them into a list
    flattened_data = []
    logging.info("Processing and flattening the loaded JSON data")

    for entry in data:
        flattened_data.append(flatten_json(entry))

    # Converting the list of flattened data into a DataFrame
    logging.info("Data processing completed. Converting to DataFrame for display purposes")
    return pd.DataFrame(flattened_data)

def saveToCSVFile(df, filename):
    if df is not None:
        logging.info("Saving the converted JSON data to a CSV file.")
        df.to_csv(filename, index=False)
        logging.info(f"CSV file saved successfully as '{filename}'.")
        print(df)
    else:
        logging.error("Conversion failed!")

# Function call
df = ConvertJsonToCsv('jsondata.json')
saveToCSVFile(df, 'csvdata.csv')
