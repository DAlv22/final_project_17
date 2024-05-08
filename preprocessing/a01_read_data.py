# Libraries ------------------------------------------- 

import pandas as pd
import numpy as np

# Loading data ---------------------------------------- 

def load_data(folder_path):
    datasets = {}
    datasets_name = ['contract', 'personal', 'internet', 'phone']
    for item in datasets_name:
        datasets[item] = pd.read_csv(folder_path + item + '.csv')
    return datasets


# Data merge ---------------------------------------------

def merge_dataframes(datasets):
    """
    merge de varios DataFrames de manera iterativa.
    """
    merged_df = datasets[0]
    for df in datasets[1:]:
        merged_df = merged_df.merge(df, how='left', on='customerID')
    return merged_df
