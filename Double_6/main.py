import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from random import randint

data = []

numIter = 1000

for i in range(numIter):
    s = ''

    for j in range(2):
        r = randint(1,6)
        s += str(r)

    while (s[len(s)-1] != '6')  or (s[len(s)-2] != '6') or (s[len(s)-3] != '6') or (s[len(s)-4] != '6'):
        r = randint(1,6)
        s += str(r)

    data.append(len(s))

    print(i/numIter)

avg = sum(data)/len(data)

print(avg)

# plt.plot(data)