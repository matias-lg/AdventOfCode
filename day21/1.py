from sys import argv

a = int(argv[1])
b = int(argv[2])

a_score = 0
b_score = 0
turn = 0
dice = 1
t = 0

while a_score < 1000 and b_score < 1000:
    t += 3
    roll = 3*dice + 3
    dice += 3
    if turn == 0:
        a = (a+roll) % 10
        if a == 0:
            a = 10
        a_score += a
        turn += 1
    else:
        b = (b + roll) % 10
        if b == 0:
            b = 10
        b_score += b
        turn -= 1
    if turn == 0:
        print(f"2 score: {a_score}")
    else:
        print(f"1 score: {b_score}")
print("-----end------")
print(a_score, b_score, t)
print(f"part one solution: {min(a_score,b_score)*t}")
