fib = []
ratio = []

numIter = 10000

fib.append(1)
fib.append(1)

for i in range(1, numIter):
    fib.append(fib[i-1]+fib[i])
    print(i/numIter)

for i in range(1, len(fib)):
    ratio.append(fib[i]/fib[i-1])
    print(i / numIter)

print(ratio[len(ratio)-1])
