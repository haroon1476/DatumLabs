# From csv to snowflake data transfer

import json
import csv
import snowflake.connector

import pandas as pd

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as jf, open(csv_file, 'w', newline='') as cf:
        data = json.load(jf)
        writer = csv.DictWriter(cf, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


json_to_csv('jsondata.json', 'csvdata.csv')

# reading cleaned csv
df = pd.read_csv("csvdata.csv")
print(df)

# defining the connection attribute with snowflake warehouse database
conn = snowflake.connector.connect(
    user='HAROONRASHEED',
    password='Haroonrasheed38621$',
    account='FZFNNCV-BA17928',
    warehouse='COMPUTE_WH',
    database='SNOWFLAKE_LEARNING_DB',
    schema='HAROONRASHEED_LOAD_SAMPLE_DATA_FROM_S3'
)

cursor = conn.cursor()

cursor.execute("""
CREATE OR REPLACE TABLE CSV_Database (
    
    id INT,
    name STRING,
    age STRING,
    city STRING,
    phone STRING,
    email STRING
)
""")

# Inserting the csv data into snowflake
for index, row in df.iterrows():
   
    sql = f"""
    INSERT INTO CSV_Database (id, name, age, city, email, phone)
    VALUES ({row['id']}, '{row['name']}', {row['age']}, '{row['city']}', '{row['email']}', '{row['phone']}')
    """
    

    cursor.execute(sql)