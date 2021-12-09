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
        y_min = min(y_min, l[1], r[1])
        y_max = max(y_max, l[1], r[1])
        vents.append((l, r))


the_map = [[0]*int(y_max - y_min + 1)
           for i in range(int(x_max) - int(x_min) + 1)]
print(f"{len(the_map)} x {len(the_map[0])}")


def x(coord):
    return int(coord - x_min)


def y(coord):
    return int(coord - y_min)


def get_all_points(x1, y1, x2, y2):
    m = (y2-y1)//(x2-x1)
    n = y1 - m*x1
    ret = [[x, m*x + n] for x in range(min(x1, x2), max(x1, x2) + 1)]
    return ret


for coords in vents:
    # x1 = x2
    if coords[0][0] == coords[1][0]:
        # mark all y's
        ymin = min(coords[0][1], coords[1][1])
        ymax = max(coords[0][1], coords[1][1])
        for i in range(ymin, ymax+1):
            the_map[x(coords[0][0])][y(i)] += 1
    # y1 = y2
    if coords[0][1] == coords[1][1]:
        # mark all x's
        xmin = min(coords[0][0], coords[1][0])
        xmax = max(coords[0][0], coords[1][0])
        for i in range(xmin, xmax + 1):
            the_map[x(i)][y(coords[0][1])] += 1
    # 45 deg
    if abs(coords[0][0] - coords[1][0]) == abs(coords[0][1] - coords[1][1]):
        x1 = coords[0][0]
        y1 = coords[0][1]
        x2 = coords[1][0]
        y2 = coords[1][1]
        p = get_all_points(x1, y1, x2, y2)
        for i in p:
            the_map[x(int(i[0]))][y(int(i[1]))] += 1
res = 0


for i in the_map:
    for j in i:
        if j >= 2:
            res += 1
print(res)
