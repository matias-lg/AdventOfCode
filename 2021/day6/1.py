from sys import argv

DAYS = 80

filename = argv[1]

f = open(filename, "r").read()
l = [int(x) for x in f.split(",")]

while DAYS > 0:
    for i in range(len(l)):
        if l[i] == 0:
            l[i] = 6
            l.append(8)
        else:
            l[i] -= 1
    DAYS -= 1

print(len(l))
