from sys import argv
lines = [l[:-1] for l in open(argv[1], 'r').readlines()]
inc = []
for s in lines:
    cs = []
    n = len(s)
    cnt = 0
    for c in s:
        cnt += 1
        for x in cs:
            print(x, end=" ")
        print(" ")
        if c in ['{', '[', '(', '<']:
            cs.append(c)
        elif c == '}':
            if cs[-1] == '{':
                cs.pop(-1)
            else:
                break
        elif c == ']':
            if cs[-1] == '[':
                cs.pop(-1)
            else:
                break
        elif c == ')':
            if cs[-1] == '(':
                cs.pop(-1)
            else:
                break
        else:
            if cs[-1] == '<':
                cs.pop(-1)
            else:
                break
        # we are in incomplete
        if cnt == n:
            inc.append(cs)
scrs = []
for s in inc:
    scr = 0
    while len(s) > 0:
        x = s.pop(-1)
        scr *= 5
        if x == '(':
            scr += 1
        elif x == '[':
            scr += 2
        elif x == '{':
            scr += 3
        else:
            scr += 4
    scrs.append(scr)

scrs.sort()
print(scrs[len(scrs)//2])
