prime = []

n = 1

while n <= 10:
    p = True
    print("n = " + str(n))
    while p is True:
        i = 0
        while i <= n:
            i += 1
            print("i = " + str(i))
            if ((n/i) % 1) != 0:
                p = False
                n += 1
        if p is True:
            prime.append(n)
            n += 1
            p = False

print(prime)

