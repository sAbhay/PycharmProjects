from concorde.tsp import TSPSolver
import concorde
from matplotlib import collections  as mc
import numpy as np
import pandas as pd
import time
# import pylab as pl

path = '/Users/abhaysinghal/Documents/Kaggle/Travelling_Santa/'

cities = pd.read_csv(path + 'cities.csv')

solver = TSPSolver.from_data(cities.X, cities.Y, norm='EUC_2D')

t = time.time()
tour_data = solver.solve(time_bound = 60.0, verbose = True, random_seed = 42) # solve() doesn't seem to respect time_bound for certain values?
print(time.time() - t)
print(tour_data.found_tour)

pd.DataFrame({'Path': np.append(tour_data.tour,[0])}).to_csv('sub5.csv', index=False)