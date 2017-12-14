from collections import deque
from functools import reduce


from adventlib import *


DAY = 14


def knot(s):
    vals = [17, 31, 73, 47, 23]

    insn = [ord(i) for i in s] + vals
    skip = 0
    begin = 0
    lst = list(range(256))
    for rnd in range(64):
        for size in insn:
            sub = [0] * size
            for i in range(size):
                sub[i] = lst[(begin + i) % 256]
            sub = list(reversed(sub))
            for i, e in enumerate(sub):
                lst[(begin + i) % 256] = e
            begin += size + skip
            skip += 1

    sp = []
    for i in range(16):
        sp.append(reduce(lambda a, b: a ^ b, lst[i * 16 + 1: i * 16 + 16], lst[i * 16]))
    return sp


def p_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def main():
    inp = store_input(DAY)
    if inp is None:
        return
    inp = inp.rstrip("\n")
    used = 0
    m = {}
    s = set()

    for i in range(128):
        h = knot(inp + "-" + str(i))
        for j, e in enumerate(h):
            for jj in range(8):
                if e & 1 == 1:
                    m[(i, 8 * j + 7 - jj)] = 1
                    s.add((i, (8 * j + 7 - jj)))
                else:
                    m[(i, 8 * j + 7 - jj)] = 0
                e >>= 1

    def accessible(p):
        return m.get(p, 0) == 1

    def neighbors(curr):
        for neighbor in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            p = p_add(curr, neighbor)
            if accessible(p):
                yield p

    grps = 0
    while s:
        grps += 1
        st = s.pop()
        queue = deque([st])
        while queue:
            c = queue.popleft()
            for n in neighbors(c):
                if n in s:
                    s.remove(n)
                    queue.append(n)

    print(grps)


if __name__ == '__main__':
    main()
