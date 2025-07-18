import json

# Reading json
with open('input.json', 'r') as file:
    data = json.load(file)

def flattenJSON(d, parent_key=''):

    items = [] 
    for k in d:

        new_key = f"{parent_key}_{k}" if parent_key else k

        # cheking if value against current key is a dictionary
        if isinstance(d[k], dict):

            # recursively going deep in the dictionary if the value against a key is a dictionary
            items.extend(flattenJSON(d[k], new_key).items())
        else:
            items.append((new_key, d[k]))

    #print(f"Current item status =  {items}")       

    # returning the data in dictionary form that will be converted into the csv
    return dict(items)

# Calling the function
flatData = flattenJSON(data)

with open("output.csv", "w") as f:

    # columns will be the main keys
    headers = list(flatData.keys())
    f.write(",".join(headers) + "\n")

    # rows will be the values
    values = [str(flatData[key]) for key in headers]
    f.write(",".join(values) + "\n")
