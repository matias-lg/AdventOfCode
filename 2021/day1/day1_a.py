from sys import stdin

l = []
for x in stdin:
    l.append(int(x))
print(l)

res = 0
for i in range(1, len(l)):
    if l[i-1] < l[i]:
        res += 1
print(res)
