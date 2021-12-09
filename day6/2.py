from sys import argv
from functools import reduce

DAYS = 256

filename = argv[1]

f = open(filename, "r").read()
l = [int(x) for x in f.split(",")]
n = [0]*9

for i in l:
    n[i] += 1
print(n)
while DAYS > 0:
    y = [i for i in n]

    for i in range(8):
        n[i] = n[i+1]

    n[6] += y[0]
    n[8] = y[0]

    DAYS -= 1
print(n)
print(reduce(lambda a, b: a+b, n))

# cantidad de 8 -> cantidad de 0s que habian antes
# cantidad de 6 -> cantidad de 7 antes + 0 antes
# cantidad de 0 -> cantidad de 1 antes
