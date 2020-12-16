import columns
import pandas as pd
import re

def strip_white(df):
    '''Strip multiple spaces, including tabs, new lines, and leading and trailing whitespace for all string columns'''
    string_columns = columns.get_str_column_names(df)
    for col in string_columns:
        df[col] = df[col].map(str.strip)
        df[col] = df[col].map(lambda x: re.sub('\s+',' ', x))


