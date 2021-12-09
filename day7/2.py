from sys import argv

filename = argv[1]

f = open(filename, "r").read()
l = [int(x) for x in f.split(",")]


def mediana(a):
    n = len(a)
    s = sorted(a)
    if n % 2 != 0:
        return (s[int(n//2)])
    return ((s[(n-1)//2] + s[n//2])//2)


m = mediana(l)
res = 0
for i in l:
    res += abs(i-m)

print(mediana(l))
print(res)
