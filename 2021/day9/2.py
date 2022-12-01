from sys import argv

filename = argv[1]
lines = open(filename, 'r').readlines()

nums = [[[int(n), False] for n in num[:-1]] for num in lines]

check_left = True
check_right = True
check_up = True
check_down = True

score = 0
basins = []


def basinate(i, j):
    tmpnums = [[[int(n), False] for n in num[:-1]] for num in lines]

    tmpnums[i][j][1] = True

    def recur(i, j):
        # recursively basinate neighbors
        cr = True
        cl = True
        cu = True
        cd = True
        if i == 0:
            cu = False
        if i == len(tmpnums)-1:
            cd = False
        if j == 0:
            cl = False
        if j == len(tmpnums[0])-1:
            cr = False
        if cr:
            if tmpnums[i][j+1][0] != 9 and not tmpnums[i][j+1][1]:
                tmpnums[i][j+1][1] = True
                recur(i, j+1)
        if cl:
            if tmpnums[i][j-1][0] != 9 and not tmpnums[i][j-1][1]:
                tmpnums[i][j-1][1] = True
                recur(i, j-1)
        if cd:
            if tmpnums[i+1][j][0] != 9 and not tmpnums[i+1][j][1]:
                tmpnums[i+1][j][1] = True
                recur(i+1, j)
        if cu:
            if tmpnums[i-1][j][0] != 9 and not tmpnums[i-1][j][1]:
                tmpnums[i-1][j][1] = True
                recur(i-1, j)
    recur(i, j)
    # count size
    ret = 0
    for i in tmpnums:
        for j in i:
            if j[1]:
                ret += 1
    return ret


for i in range(len(nums)):
    for j in range(len(nums[0])):
        is_lp = True
        if i == 0:
            check_up = False
        if i == len(nums) - 1:
            check_down = False
        if j == 0:
            check_left = False
        if j == len(nums[0]) - 1:
            check_right = False
        if check_up:
            if nums[i-1][j] <= nums[i][j]:
                is_lp = False
        if check_down:
            if nums[i+1][j] <= nums[i][j]:
                is_lp = False
        if check_left:
            if nums[i][j-1] <= nums[i][j]:
                is_lp = False
        if check_right:
            if nums[i][j+1] <= nums[i][j]:
                is_lp = False
        if is_lp:
            sz = basinate(i, j)
            basins.append(sz)

        check_left = True
        check_right = True
        check_up = True
        check_down = True

res = 0
basins.sort()
print(basins[-1]*basins[-2]*basins[-3])
