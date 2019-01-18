import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

seq = []
numIter = 10000
occ = []
freq = []
t = 0

seq.append(0)
seq.append(1)

def firstDigit(x):
    return x // 10 ** int(math.log(x, 10))

for i in range(9):
    occ.append(0)
    freq.append(0)

for i in range(1, numIter):
    seq.append(seq[i-1] + seq[i]) # fibonacci series
    # seq.append(2 ** i) # powers of 2

for i in range(1, len(seq)):
    print(i)
    occ[firstDigit(seq[i])-1] += 1

for i in range(len(occ)):
    t += occ[i]

for i in range(len(occ)):
    freq[i] = occ[i]/t

print(occ)
print(freq)

plt.plot([1,2,3,4,5,6,7,8,9], freq)
plt.xlabel('Digit')
plt.ylabel('Frequency')
plt.title('Frequency of Leading Digits in the Fibonacci Series')
plt.show()