from __future__ import annotations
from sys import argv


l = [line[:-1].split("-") for line in open(argv[1]).readlines()]

# insert all elements in graph
graph = {}
for nodes in l:
    if nodes[0] in graph:
        graph[nodes[0]][nodes[1]] = True
    else:
        graph[nodes[0]] = {nodes[1]: True}
    if nodes[1] in graph:
        graph[nodes[1]][nodes[0]] = True
    else:
        graph[nodes[1]] = {nodes[0]: True}


def backtrack(begin: str, end: str, disc) -> int:
    tmpd = disc.copy()
    if begin == end:
        return 1
    res = 0
    if not begin.isupper():
        tmpd[begin] = True
    for i in graph[begin].keys():
        if not tmpd[i]:
            res += backtrack(i, end, tmpd)
    return res


print(backtrack("start", "end", {i: False for i in graph.keys()}))
