filename = input()
l = []
with open(filename, "r") as f:
    lines = f.read().splitlines()
    l = [[int(char) for char in b] for b in lines]

gamma = 0
epsilon = 0
oxygen = []
co2 = []
zeros = 0
ones = 0

for i in range(len(l)):
    if l[i][0] == 0:
        zeros += 1
    else:
        ones += 1
w = 1
if zeros > ones:
    w = 0
# first filter
for i in range(len(l)):
    if l[i][0] == w:
        oxygen.append(l[i])
    else:
        co2.append(l[i])

p = 1
while len(oxygen) > 1:
    print(oxygen)
    # find max
    m = 0
    ones = 0
    zeros = 0
    for e in oxygen:
        if e[p] == 0:
            zeros += 1
        else:
            ones += 1
    if ones >= zeros:
        m = 1
    # remove e such that e[p] != max
    i = 0
    while i < len(oxygen):
        if oxygen[i][p] != m:
            oxygen.pop(i)
            continue
        i += 1
    p += 1
print(oxygen[0])

p = 1
while len(co2) > 1:
    # find min
    m = 1
    ones = 0
    zeros = 0
    for e in co2:
        if e[p] == 0:
            zeros += 1
        else:
            ones += 1
    if zeros <= ones:
        m = 0
    # remove e such that e[p] != max
    i = 0
    while i < len(co2):
        if co2[i][p] != m:
            co2.pop(i)
            continue
        i += 1
    p += 1

print(co2[0])
nox = 0
no2 = 0
for i in range(len(co2[0])):
    nox += oxygen[0][i] * 2**(len(oxygen[0]) - i - 1)
    no2 += co2[0][i] * 2**(len(co2[0]) - i - 1)
print(nox)
print(no2)
print(no2*nox)
