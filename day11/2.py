from sys import argv, setrecursionlimit
from os import system
from time import sleep
from colorama import Style, Fore, init

setrecursionlimit(20000)
init()
filename = argv[1]
lines = open(filename, 'r').readlines()

nums = [[[int(n), False] for n in num[:-1]] for num in lines]

total_flashes = 0


def reset_all():
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            nums[i][j][1] = False


def print_nums():
    global total_flashes
    print(f"total flashes: {total_flashes}")
    for i in nums:
        for i in [i[0] for i in i]:
            if i == 0:
                print(Fore.RED + str(i), end='\033[39m')
            else:
                print(i, end="")
        print("")


def check_part_2():
    for i in nums:
        for j in i:
            if j[0] != 0:
                return False
    return True


def flash(i, j):
    global total_flashes
    global nums
    total_flashes += 1
    nums[i][j][1] = True
    nums[i][j][0] = 0

    neighbors = [(i+1, j), (i+1, j+1), (i+1, j-1), (i, j+1),
                 (i, j-1), (i-1, j), (i-1, j+1), (i-1, j-1)]
    to_search = []
    for i in range(len(neighbors)):
        if not ((neighbors[i][0] < 0) or (neighbors[i][0] > (len(nums)-1)) or (neighbors[i][1] > (len(nums[0])-1)) or neighbors[i][1] < 0):
            to_search.append(neighbors[i])

    for p in to_search:
        if not nums[p[0]][p[1]][1]:
            nums[p[0]][p[1]][0] += 1
            if nums[p[0]][p[1]][0] > 9:
                flash(p[0], p[1])


# @@@
STEP_NUM = int(argv[2]) + 1
# step
for step in range(STEP_NUM):
    # reset bool and cool print
    reset_all()
    print(f"step: {step},", end=" ")
    print_nums()
    sleep(0.05)
    if check_part_2():
        print(f"WE SYNCED AT {step}")
        break
    if step != STEP_NUM - 1:
        print("\033[F"*(len(nums)+2))
    # first add one to each
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            nums[i][j][0] += 1
    # then flash every possible
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if nums[i][j][0] > 9:
                flash(i, j)
