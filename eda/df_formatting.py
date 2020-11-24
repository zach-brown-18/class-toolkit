import pandas as pd
import numpy as np
import re

def format_column_titles(df):
    '''Changes column titles to lower_and_snake_case'''
    df.columns = map(lambda x: str(x), df.columns)
    df.columns = map(str.lower, df.columns)
    df.columns = map(lambda x: x.strip(), df.columns)
    df.columns = map(lambda x: x.replace(' ', '_'), df.columns)
    df.columns = map(lambda x: x.replace('.', '_'), df.columns)

    
def get_str_column_names(df):
    return [col for col in df.columns if type(df[col][0]) is str]  

def isnan(x):
    if x != x:
        return True
    return False

def get_binary_columns(df):
    '''Returns a list of column names for only binary columns'''
    cols = []
    for col in df:
        binary = len(df[col].unique()) == 2
        three_values = len(df[col].unique()) == 3
        has_nan = not all(isnan(name) for name in df[col].unique())
        if binary:
            cols.append(col)
        if three_values & has_nan:
            cols.append(col)
    
    return cols