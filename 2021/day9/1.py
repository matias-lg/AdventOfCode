from sys import argv

filename = argv[1]
lines = open(filename, 'r').readlines()

nums = [[int(n) for n in num[:-1]] for num in lines]

check_left = True
check_right = True
check_up = True
check_down = True

score = 0

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
            score += nums[i][j]+1
        check_left = True
        check_right = True
        check_up = True
        check_down = True


print(score)
