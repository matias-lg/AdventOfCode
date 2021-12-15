from sys import argv

lines = open(argv[1], "r").readlines()
coords = []
i = 0
while(len(lines[i]) > 1):
    ns = lines[i].split(",")
    coords.append((int(ns[0]), int(ns[1][:-1])))
    i += 1
i += 1
inst = []
for i in range(i, len(lines)):
    inst.append((lines[i][11], int(lines[i][13:-1])))

max_x, max_y = max([i for i, j in coords]), max([j for i, j in coords])
paper = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
print(len(inst))
for i in inst:
    print(i)


def p():
    for i in paper:
        for j in i:
            if j == 1:
                print("#", end="")
            else:
                print(".", end="")
        print("")


def at(x, y):
    return paper[y][x]


def s(x, y, n):
    paper[y][x] = n


for i, j in coords:
    s(i, j, 1)

# 14 - 2(14-7)
# y - 2(y-n) = -y+2n
# 14-8


def fold(c, n):
    if c == 'x':
        for x in range(n+1, max_x+1):
            for y in range(max_y + 1):
                try:
                    nx = 2*n-x
                    if nx >= 0:
                        s(2*n-x, y, at(x, y) or at(2*n-x, y))
                    s(x, y, 0)
                except IndexError:
                    print("e")
    else:
        for x in range(max_x+1):
            for y in range(n+1, max_y + 1):
                try:
                    ny = 2*n-y
                    if ny >= 0:
                        s(x, 2*n-y, at(x, y) or at(x, 2*n-y))
                    s(x, y, 0)
                except IndexError:
                    print("e")


for i, j in inst:
    fold(i, j)

p()
