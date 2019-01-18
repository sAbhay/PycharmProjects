import pandas as pd
import numpy as np

import os
import math
# import matplotlib.pyplot as plt
import numpy as np
import urllib.request
from PIL import Image
from tsp_solver.greedy_numpy import solve_tsp
from scipy.spatial.distance import pdist, squareform

image_path = '/Users/abhaysinghal/PycharmProjects/Travelling_Santa/src/small_cities.jpg'

original_image = Image.open(image_path)
bw_image = original_image.convert('1', dither=Image.NONE)

bw_image_array = np.array(bw_image, dtype=np.int)
white_indices = np.argwhere(bw_image_array == 1)
# chosen_black_indices = white_indices[np.random.choice(white_indices.shape[0], replace=False, size=10000)]res

distances = pdist(white_indices)
distance_matrix = squareform(distances)

optimized_path = solve_tsp(distance_matrix, endpoints=(0,0))

print(optimized_path)
# print(len(optimized_path) != len(set(optimized_path)))

df = pd.Series(optimized_path)
print(df)


# path = '/Users/abhaysinghal/Documents/Kaggle/Travelling_Santa/'
# cities = pd.read_csv(path + 'cities.csv', names=['CityId', 'X', 'Y'], skiprows=1)

