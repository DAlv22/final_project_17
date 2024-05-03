# Libraries ------------------------------------------- 

import pandas as pd
import numpy as np
import re 

# Loading data ---------------------------------------- 

def load_data(folder_path):
    datasets = {}
    datasets['contract'] = pd.read_csv(folder_path + 'contract.csv', parse_dates=['EndDate'])
    datasets['personal'] = pd.read_csv(folder_path + 'personal.csv')
    datasets['internet'] = pd.read_csv(folder_path + 'internet.csv')
    datasets['phone'] = pd.read_csv(folder_path + 'phone.csv')
    return datasets


# access each datase
if __name__ == "__main__":
    folder_path = 'files/datasets/input/'
    data = load_data(folder_path)
    contract_data = data['contract']
    personal_data = data['personal']
    internet_data = data['internet']
    phone_data = data['phone']