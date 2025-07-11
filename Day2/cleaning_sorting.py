import pandas as pd

# ----------------- CLEANING COLUMNS NAMES

def cleanColumnNames(filename):
    df = pd.read_csv(filename, on_bad_lines='skip')

    # Cleaning the trainling and leading spaces in column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" " , "_")

    return df # returning the modified data frame which clean column names


# ----------------- FILLING MISSING VALUES

def fillMissingValues(filename):


    # First cleaning column names
    df = maintainJoiningDateFormat(filename)   
    print(df.columns)

    # Filling missing ages as means of ages
    df['age'] = df['age'].fillna('Unknown')

    # Filling missing departments as unknown departments
    df['department'] = df['department'].fillna('Unknown')

    # Filling other misssing column values

    # Writing 'Ghost' where the name of person is unknown
    df['name'] = df['name'].fillna('Ghost')

    df['city'] = df['city'].fillna('Unknown')
    df['city'] = df['city'].str.title()
    df['joining_date'] = df['joining_date'].fillna('Unknown')    

    # Writing '-' where the salary is unknown
    df['salary'] = df['salary'].fillna('Unknown')

    # Assigning the missing ids 

    # Ensure ID is treated as numeric (in case it has strings like "004")
    df['id'] = pd.to_numeric(df['id'], errors='coerce')

    # Finding the missing id from the data frame
    missing_id_mask = df['id'].isna()

    # Getting the max id from the data frame
    max_id = int(df['id'].max())

    # Assigning new id
    df.loc[missing_id_mask, 'id'] = max_id + 1

    print(df.head)
    df.to_csv('cleaned_data.csv', index=False)
    return df


# --------- FUNCTION TO MAKE THE FORMAT OF JOINING DATE SAME AS ALL

def maintainJoiningDateFormat(filename):

    df = pd.read_csv("messy_data.csv", on_bad_lines='skip')
    df = cleanColumnNames(filename)

     # Maintaining the same joining date format
    df['joining_date'] = pd.to_datetime(df['joining_date'], errors='coerce')  # convert to datetime
    df['joining_date'] = df['joining_date'].dt.strftime('%d-%m-%y')           # format uniformly

    return df


def applyCleaning(filename):
    fillMissingValues(filename)


# <------------- CODE FOR SORTING OF DATA ON THE BASIS OF SOME ATTRIBUTE

def sortData(attribute, filename):

    df = pd.read_csv(filename, on_bad_lines='skip')

    if attribute in df.columns:
        df = df.sort_values(by=attribute , ascending=True)
        print(df.to_string())
        print(f"Sorting applied on the basis of {attribute} successfully")
    else:
        print(f"Attribute {attribute} does not exist in dataframe")

    return



# <---------------  MAIN FUNCTION CALL
    

# FIlling the missing values 
applyCleaning('messy_data.csv')
print("Cleaning applied!")

attribute = input("Enter attribute on the basis of which sorting has to take place : ")

# Function call to sort
sortData(attribute , 'cleaned_data.csv')
