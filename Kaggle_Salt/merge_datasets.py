import csv
import time
import pandas as pd
import psutil

dataset = pd.DataFrame()

t = time.clock()

print(psutil.virtual_memory())

for i in range(24, 30):
    print(i)
    filepath = '/Users/abhaysinghal/PycharmProjects/Kaggle_Salt/salt_test_' + str(i) + '.csv'
    data = pd.read_csv(filepath, sep=",", low_memory=False)
    dataset = pd.concat([dataset, data])
    t = time.clock() - t
    print(t)

print(psutil.virtual_memory())
dataset.to_csv("salt_test_final_4.csv")
print(psutil.virtual_memory())
t = time.clock() - t
print(t)