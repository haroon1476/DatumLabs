# Merging two csvs

import pandas as pd

def MergeFiles(file1 , file2):
  
   
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

   
    merged_df = pd.merge(df1, df2, on='id', how='inner')  # Merging will be based on id and inner join wil take place

    merged_df.to_csv('mergedFile.csv', index=False)

    print("Files merged successfully!")


# function call
MergeFiles('csvfile1.csv' , 'csvfile2.csv')