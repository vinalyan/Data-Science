import pandas as pd

"""
The next method allows us to change the features in our dataset
"""
def change_feature_types(df):    
    lista = list(df.select_dtypes(include=[pd.np.object]).columns)
    lista.append("OverallQual")
    lista.append("OverallCond")
    lista.append("MSSubClass")
    df.loc[:,lista] = df.loc[:,lista].astype("category")    
    return df

"""
The next method allows us transform our features
+ lower case
"""
def transformation(df):
    df.columns = df.columns.str.lower()
    return df