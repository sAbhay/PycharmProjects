import pandas as pd

filepath = '/Users/abhaysinghal/Documents/Kaggle/Salt/mamodevu_preds_fccf7389.csv'
df = pd.read_csv(filepath)

def describe(df):
    print(df.shape)
    print(df.describe())

describe(df)