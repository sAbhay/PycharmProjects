import pandas as pd

path = '/Users/abhaysinghal/Documents/Kaggle/Travelling_Santa/'

sub = pd.read_csv(path + 'sub3.csv')
sub = sub.drop('Unnamed: 0', axis=1)
# sub.columns = ['Path']

sub.to_csv(path + 'sub4.csv', index=False)