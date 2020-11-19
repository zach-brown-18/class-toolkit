import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

def investigate_null(df):
    '''Returns a sorted DataFrame of columns with null values'''
    # Identify null values by column
    null_count = df.isna().sum().reset_index()
    null_count.rename(columns = {'index':'column', 0:'null_count'}, inplace=True)
    null_count = pd.DataFrame(null_count)

    # Isolate columns with missing values
    has_nulls = null_count['null_count'] != 0
    null_count = null_count.loc[has_nulls, :].sort_values(by = 'null_count', ascending = False, ignore_index = True)
    
    return null_count


def plot_null(df):
    '''Plots the number of null values in all columns that contain at least one null value'''    
    null_count = investigate_null(df)
    
    plt.figure(figsize=(16,8))
    plt.title('Null Values by Column', size=16)
    plt.xticks(rotation=45)
    plt.bar(null_count['column'], null_count['null_count']);

    
def set_negatives_to_nan(df, **kwargs):
    '''Sets negative values to zero. Specify exclude_cols = column(s) to keep negative values.'''
    numeric_cols = df._get_numeric_data()
    
    if 'exclude_cols' in kwargs.keys():
        try:
            numeric_cols.drop(columns = kwargs['exclude_cols'], inplace = True)
        except:
            print('Some exclude_cols not found in df')
            print('Operation failed.')
            return None

    cols = numeric_cols.columns
    for col in cols:
        df[col] = df[col].map(lambda x: x if x >= 0 else np.nan)
