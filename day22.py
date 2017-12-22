from collections import defaultdict


from adventlib import *


DAY = 22


def main():
    inp = store_input(DAY)
    if inp is None:
        return
    lines = list(split_lines(inp))

    C, W, F, I = range(4)

    mp = defaultdict(lambda: 0)
    for x, l in enumerate(lines):
        for y, i in enumerate(l):
            if i == "#":
                mp[(x, y)] = I

    x = y = 12

    U, D, L, R = range(4)
    l = {U: L, L: D, D: R, R: U}
    r = {U: R, R: D, D: L, L: U}
    rv = {U: D, D: U, R: L, L: R}
    f = U

    ib = 0
    for _ in range(10000000):
        n = mp[(x, y)]
        if n == C:
            f = l[f]
            mp[(x, y)] = W
        elif n == W:
            mp[(x, y)] = I
            ib += 1
        elif n == F:
            f = rv[f]
            mp[(x, y)] = C
        else:
            f = r[f]
            mp[(x, y)] = F
        if f == U:
            x -= 1
        elif f == D:
            x += 1
        elif f == L:
            y -= 1
        elif f == R:
            y += 1

    print(ib)


if __name__ == '__main__':
    main()
