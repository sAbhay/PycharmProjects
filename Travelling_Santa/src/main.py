import pandas as pd
import numpy as np
import math
from sklearn.neighbors import KDTree

path = '/Users/abhaysinghal/Documents/Kaggle/Travelling_Santa/'

def is_prime(n):

    if n == 1:
        return 0 #False
    if n == 2:
        return 1 #True
    if n > 2 and n % 2 == 0:
        return 0 #False

    count_prime = 0
    div = math.floor(math.sqrt(n))
    for d in range(3, 1 + div, 2):
        if n % d == 0:
            return 0 #False
    return 1 #True

cities = pd.read_csv(path+'cities.csv', skiprows=1, names=['CityId', 'X', 'Y'])
# cities.set_index('CityId', inplace=True)
#
# i = -1
#
# with open(path + 'cities.csv', 'r') as read:
#     csvReader = csv.reader(read, delimiter=',')
#     with open(path + 'primes.csv', 'w') as write:
#         csvWriter = csv.writer(write, delimiter=',')
#         for row in csvReader:
#             if i >= 0:
#                 if is_prime(int(row[0])):
#                     csvWriter.writerow(row)
#
#             i += 1
            # if i % 1000 == 0:
            #     print(i)

# primes = pd.read_csv(path + 'primes.csv')
# non_primes = pd.read_csv(path + 'non_primes.csv')

# print(primes.describe())

# def dist(a, b):
#     ax, ay = cities.loc[a, :]
#     bx, by = cities.loc[b, :]
#     return math.sqrt((ax-bx)**2 + (ay-by)**2)
#
# def find_closest(curr):
#     i = 0
#     n = len(cities.index)
#     shortest_dist = 999999999
#     for city in cities.iterrows():
#         d = dist(curr, city[0])
#         if  d < shortest_dist and city[0] != curr:
#             shortest_dist = d
#             closest = city[0]
#         i += 1
#         if i == n-1:
#             return closest

def find_closest(curr, tree, prime):
    pt = np.array(cities.loc[curr, :]).reshape((1,2))
    n = 2
    i = tree.query(pt, k=n, return_distance=False, sort_results=True)[0][n - 1]
    if prime:
        while not is_prime(i):
            n += 1
            i = tree.query(pt, k=n, return_distance=False, sort_results=True)[0][n - 1]
    # print(i)
    return i

# current = 0
# prev = 0
# i = 0
# seq = [current]
# tree = KDTree(cities)
# primeCount = 17803
# while len(cities.index) > 1:
#     prev = current
#     if (i+1) % 10 == 0 and primeCount > 0:
#         current = cities.index[find_closest(current, tree, prime=True)]
#     else:
#         current = cities.index[find_closest(current, tree, prime=False)]
#     seq.append(current)
#     # print(current)
#     # print("Prev: %f" % prev)
#     # print(seq)
#     cities = cities.drop([prev], axis=0)
#     tree = KDTree(cities)
#     if i % 100 == 0:
#         print(i)
#         pass
#     i += 1
# seq.append(cities.index[0])

PRIMES = pd.read_csv(path+'primes.csv', skiprows=1, names=['CityId', 'X', 'Y'])

def greedy(verbose=True, k_iter=10000):
    ID = cities['CityId'].values
    coord = cities[['X', 'Y']].values
    id = 0
    pos = coord[0]
    path = [0]

    ID = np.delete(ID, 0)
    coord = np.delete(coord, 0, axis=0)

    # Prime penalisation matrix
    primes = -(0.1) * np.isin(ID, PRIMES) + 1.1

    it = 1

    while len(path) != cities.shape[0]:
        # Compute the distance matrix
        dist_matrix = np.linalg.norm(coord - pos, axis=1)

        # Add a penalisation for non-prime numbers
        if (it + 1) % 10 == 0 and id not in PRIMES:
            dist_matrix *= primes

        # Find the nearest city
        i_min = dist_matrix.argmin()

        id = ID[i_min]
        path.append(id)
        pos = coord[i_min]

        # Delete it
        coord = np.delete(coord, i_min, axis=0)
        ID = np.delete(ID, i_min)
        primes = np.delete(primes, i_min)

        it += 1

        if verbose and it % k_iter == 0:
            print('{} iterations, {} remaining cities.'.format(it, len(ID)))

    # Don't forget to add the north pole at the end!
    path.append(0)

    return path

seq = greedy()
df = pd.DataFrame(seq)
df.columns = ['Path']
df.to_csv(path + 'sub3.csv', index=False)

