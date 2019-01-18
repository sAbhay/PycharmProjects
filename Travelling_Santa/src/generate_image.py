# import matplotlib.pyplot as plt
import pandas as pd
# from pandas.plotting import table
import scipy.misc
import numpy as np

path = '/Users/abhaysinghal/Documents/Kaggle/Travelling_Santa/'
cities = pd.read_csv(path + 'cities.csv', names=['CityId', 'X', 'Y'], skiprows=1, nrows=1000)

cities.Index = cities['CityId']
cities = cities.drop(['CityId'], axis=1)

# max_x = np.max(cities['X'])
# max_y = np.max(cities['Y'])
# print(max_x)
# print(max_y)

max_x = 5099.502141
max_y = 3397.809824

map = np.zeros((int(max_y)+1, int(max_x)+1))

i = 0
p = 0
for row in cities.iterrows():
    # print(row)
    # print(row[1]['X'])
    map[int(row[1]['Y']), int(row[1]['X'])] = 255
    p = int((i/len(cities)) * 100)
    if p % 1 == 0:
        print(p)
    i += 1

scipy.misc.imsave('small_cities.jpg', map)

# ax = plt.subplot(111, frame_on=False)
# ax.xaxis.set_visible(False)
# ax.yaxis.set_visible(False)
#
# table(ax, cities)
#
# plt.savefig('mytable.png')