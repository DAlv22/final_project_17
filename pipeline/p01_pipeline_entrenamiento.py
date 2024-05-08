import pandas as pd
from preprocessing import a01_read_data

datasets = a01_read_data.load_data('files/datasets/input/')
merge_dataframes = a01_read_data.merge_dataframes(datasets)
merge_dataframes.to_csv('files/datasets/output/i00_data_merge.csv', index=False)
print(merge_dataframes.head(10))