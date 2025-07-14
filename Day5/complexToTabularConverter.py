# Converting complex csv file to tabular form

import json
import pandas as pd
from pandas import json_normalize

def readJsonFile(filename):
    with open(filename, mode='r') as file:
        data = json.load(file) 
    return data

def convertToTabular(jsonData): 

    flatData = json_normalize(jsonData, sep='_')
    print(flatData)
    return flatData

# reading the complex json data
jsonData = readJsonFile('complexJSON.json')

# passing the complex json data for simplification
convertToTabular(jsonData)
