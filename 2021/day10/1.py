from sys import argv
lines = [l[:-1] for l in open(argv[1], 'r').readlines()]

score = 0
n = len(lines[0])
for s in lines:
    cs = []
    print("##########")
    for c in s:
        for x in cs:
            print(x, end=" ")
        print(" ")
        if c in ['{', '[', '(', '<']:
            cs.append(c)
        elif c == '}':
            if cs[-1] == '{':
                cs.pop(-1)
            else:
               # print(s)
                cs.append(c)
                print(cs)
                score += 1197
                break
        elif c == ']':
            if cs[-1] == '[':
                cs.pop(-1)
            else:
                cs.append(c)
                print(cs)
                # print(s)
                score += 57
                break
        elif c == ')':
            if cs[-1] == '(':
                cs.pop(-1)
            else:
                # print(s)
                cs.append(c)
                print(cs)
                score += 3
                break
        else:
            if cs[-1] == '<':
                cs.pop(-1)
            else:
                # print(s)
                cs.append(c)
                print(cs)
                score += 25137
                break

print(score)
