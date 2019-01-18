import pandas as pd
import numpy as np

path = '/Users/abhaysinghal/Documents/Kaggle/Revenue/'

train = pd.read_csv(path + 'test_features.csv', low_memory=False)
# train = train.drop(columns=['device', 'geoNetwork', 'totals', 'trafficSource'])
# features = pd.read_csv(path + 'test_features.csv', low_memory=False)
# train = pd.concat([train, features], axis=1)

# print(list(train.columns.values))
print("Loaded datasets")

train['transactionRevenue'] = train['transactionRevenue'].fillna(0)

train['total'] = train.groupby(['fullVisitorId'])['transactionRevenue'].transform('sum')
train['total'] = train['total'].apply(lambda x: np.log(x+1))

train = train.drop_duplicates(subset=['fullVisitorId'])

train.to_csv(path + 'test_set.csv')