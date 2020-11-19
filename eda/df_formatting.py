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
