import columns
import pandas as pd

def strip_white(df):
    '''Strip leading and trailing whitespace for all string columns'''
    string_columns = columns.get_str_column_names(df)
    for col in string_columns:
        df[col] = df[col].map(str.strip)