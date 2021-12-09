from sys import argv

filename = argv[1]

f = open(filename, "r").read()
l = [int(x) for x in f.split(",")]


def mean(a):
    n = len(a)
    # First we sort the array
    s = sorted(a)
    if n % 2 != 0:
        return (s[int(n//2)])
    return ((s[(n-1)//2] + s[n//2])//2)


m = mean(l)
res = 0
for i in l:
    res += abs(i-m)

print(mean(l))
print(res)
