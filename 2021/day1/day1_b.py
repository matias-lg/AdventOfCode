from sys import stdin
from functools import reduce

l = []
for x in stdin:
    l.append(int(x))

res = 0
sliding = [reduce(lambda a, b: a+b, l[i:i+3]) for i in range(0, len(l) - 2)]

for i in range(1, len(sliding)):
    if sliding[i-1] < sliding[i]:
        res += 1
print(sliding)
print(res)
