from sys import argv
from functools import reduce
from math import floor

filename = argv[1]

f = open(filename, "r").read()
l = [int(x) for x in f.split(",")]

avg = (floor(reduce(lambda a, b: a+b, l)/len(l)))
print("avg:", avg)

res = 0
for i in l:
    tot = 0
    for i in range(1, abs(avg-i)+1):
        tot += i
    res += tot
print(res)
# for the example input use ceil instead of floor
