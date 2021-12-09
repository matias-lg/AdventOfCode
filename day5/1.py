from sys import argv
from math import inf


filename = argv[1]
vents = []
with open(filename, "r") as f:
    lines = f.read().splitlines()
    x_min = inf
    x_max = -inf
    y_min = inf
    y_max = -inf
    for line in lines:
        l, r = [i.split(",") for i in line.split(" -> ")]
        l = list(map(int, l))
        r = list(map(int, r))
        x_min = min(x_min, l[0], r[0])
        x_max = max(x_max, l[0], r[0])
        y_min = min(y_min, l[0], r[0])
        y_max = max(y_max, l[0], r[0])
        vents.append((l, r))

print(vents)

the_map = [[0]*int(y_max - y_min + 1)
           for _ in range(int(x_max) - int(x_min) + 1)]
print(f"{len(the_map)} x {len(the_map[0])}")


def x(coord):
    return int(coord - x_min)


def y(coord):
    return int(coord - y_min)


for coords in vents:
    # x1 = x2
    if coords[0][0] == coords[1][0]:
        # mark all y's
        ymin = min(coords[0][1], coords[1][1])
        ymax = max(coords[0][1], coords[1][1])
        for i in range(ymin, ymax+1):
            the_map[x(coords[0][0])][y(i)] += 1
    elif coords[0][1] == coords[1][1]:
        xmin = min(coords[0][0], coords[1][0])
        xmax = max(coords[0][0], coords[1][0])
        for i in range(xmin, xmax + 1):
            the_map[x(i)][y(coords[0][1])] += 1

res = 0

for j in range(len(the_map[0])):
    for i in range(len(the_map)):
        print(the_map[i][j], end=" ")
    print("")

for i in the_map:
    for j in i:
        if j >= 2:
            res += 1
print(res)
