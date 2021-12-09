from sys import argv
from functools import reduce
from math import floor
print(sum([sum([j for j in range(
    1, abs((floor(reduce(lambda a, b: a+b, [int(x) for x in open(argv[1], "r").read().split(",")])))//(len([int(x) for x in open(argv[1], "r").read().split(",")]))-i)+1)]) for i in [int(x) for x in open(argv[1], "r").read().split(",")]]))
# use ceil instead of floor for example input
