import pandas as pd
import re

def strip_white(df):
    '''Strip multiple spaces, including tabs, new lines, and leading and trailing whitespace for all string columns'''
    string_columns = [col for col in df.columns if type(df[col][0]) is str]
    for col in string_columns:
        df[col] = df[col].map(str.strip)
        df[col] = df[col].map(lambda x: re.sub('\s+',' ', x))


def remove_special_chars(text):
    string_encode = text.encode("ascii", "ignore")
    return string_encode.decode()


def remove_phone_numbers(string):
    regex1= "\w{3}-\w{3}-\w{4}"
    regex2= "(\w{3})\w{3}-\w{4}"
    
    replace_idx1 = [(m.start(0), m.end(0)) for m in re.finditer(regex1, string)]
    replace_idx2 = [(m.start(0), m.end(0)) for m in re.finditer(regex2, string)]
    patterns = [replace_idx1, replace_idx2]
    
    for pattern in patterns:
        if pattern:
            for start, stop in pattern:
                string = string[0: start:] + string[stop::]
    
    return string


def remove_emails(string):
    regex1 = '\S+@\S+\.com'
    regex2 = '\S+@\S+\.net'
    
    replace_idx1 = [(m.start(0), m.end(0)) for m in re.finditer(regex1, string)]
    replace_idx2 = [(m.start(0), m.end(0)) for m in re.finditer(regex2, string)]
    patterns = [replace_idx1, replace_idx2]
    
    for pattern in patterns:
        if pattern:
            for start, stop in pattern:
                string = string[0: start:] + string[stop::]
    
    return string


def has_phone_numbers(string):
    regex1= "\w{3}-\w{3}-\w{4}"
    regex2= "(\w{3})\w{3}-\w{4}"
    
    if re.search(regex1, string) or re.search(regex2, string):
        return 1
    return 0


def has_emails(string):
    regex1 = '\S+@\S+\.com'
    regex2 = '\S+@\S+\.net'
    lst1, lst2 = re.findall(regex1, string), re.findall(regex2, string)
    
    if lst1 or lst2:
        return 1
    return 0