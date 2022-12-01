filename = input()
l = []
with open(filename, "r") as f:
    lines = f.read().splitlines()
    l = [[int(char) for char in b] for b in lines]

gamma = 0
epsilon = 0
gamma_arr = []
for j in range(len(l[0])):
    zeros = 0
    ones = 0
    for i in range(len(l)):
        if l[i][j] == 0:
            zeros += 1
        else:
            ones += 1
    if ones > zeros:
        gamma += 2**(len(l[0]) - j - 1)
    else:
        epsilon += 2**(len(l[0]) - j - 1)
print(gamma)
print(epsilon)

# (l[i] & 2^(j-1)) >> (j-1)
