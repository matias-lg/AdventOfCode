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


all_paths = []


def backtrack(begin: str, end: str, disc, path=""):
    tmpd = disc.copy()
    path += begin
    if begin == end:
        all_paths.append(path)
        return 1
    res = 0
    if not begin.isupper():
        tmpd[begin] += 1
    for i in graph[begin].keys():
        if tmpd[i] < 1:
            res += backtrack(i, end, tmpd, path)
    return res


tot = 0
# make all paths such that only one i is visitable twice
for i in graph.keys():
    if i == "start" or i == "end":
        continue
    g = {j: 0 for j in graph.keys()}
    g[i] -= 1
    backtrack("start", "end", g)
for i in graph.keys():
    print(i, graph[i])
print(len(list(set(all_paths))))
