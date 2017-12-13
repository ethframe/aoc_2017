from collections import deque


from adventlib import *


DAY = 12


def main():
    inp = store_input(DAY)
    if inp is None:
        return
    inp = inp.rstrip("\n")
    lines = list(split_lines(inp))

    graph = {}

    for line in lines:
        prog, conns = line.split(" <-> ")
        conn = conns.split(", ")
        graph[int(prog)] = [int(i) for i in conn]

    def mkgrp(seed):
        grp = set({seed})
        queue = deque([seed])
        while queue:
            c = queue.pop()
            for n in graph[c]:
                if n not in grp:
                    grp.add(n)
                    queue.append(n)
        return grp

    grps = [mkgrp(0)]
    visited = set(grps[0])

    a = set(graph)
    while a.difference(visited):
        seed = list(a.difference(visited))[0]
        grp = mkgrp(seed)
        grps.append(grp)
        visited.update(grp)

    print(len(grps))


if __name__ == '__main__':
    main()
