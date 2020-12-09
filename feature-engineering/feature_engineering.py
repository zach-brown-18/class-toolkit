import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

def add_poly(df, degree=3, target_name=None):
    '''Returns a dataframe with added polynoial features of degree=degree for all numeric features.'''
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    
    if target_name:
        poly_features = df.select_dtypes(include=numerics).drop(columns=target_name).columns
    else:
        poly_features = df.select_dtypes(include=numerics).columns

    poly_fit = poly.fit_transform(df[poly_features])
    df_poly = pd.DataFrame(poly_fit, columns=poly.get_feature_names(poly_features)).drop(columns=poly_features)
    df_combined = pd.concat([df, df_poly], axis=1)
    
    return df_combined