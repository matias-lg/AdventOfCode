from sys import argv
from collections import defaultdict

lines = open(argv[1], 'r').readlines()

ini = lines[0][:-1]
rules = [i[:-1].split(" -> ") for i in lines[2:]]

count = defaultdict(int)
char_count = defaultdict(int)
char_count[ini[0]] += 1
for i in range(len(ini)-1):
    count[ini[i:i+2]] += 1
    char_count[ini[i+1]] += 1

N_STEPS = 40
# NNCB {NN:1 NC:1 CB:1}
# NCNBCHB {NN:0 NC:1 CN:1 NB:1 CB:0 BC:1 CH:1 BH:1}
for _ in range(N_STEPS):
    to_add = []
    to_sub = []
    for i in rules:
        if count[i[0]] > 0:
            n = count[i[0]]
            char_count[i[1]] += n
            to_sub.append((i[0], n))
            to_add.append((i[0][0]+i[1], n))
            to_add.append((i[1]+i[0][1], n))
    for i in to_add:
        count[i[0]] += i[1]
    for i in to_sub:
        count[i[0]] -= i[1]

print(max(char_count.values())-min(char_count.values()))
