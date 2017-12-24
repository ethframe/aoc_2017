from adventlib import *


DAY = 24


def main():
    inp = store_input(DAY)
    if inp is None:
        return
    lines = list(split_lines(inp))

    comps = []
    cd = {}
    for e, c in enumerate(lines):
        c = tuple(int(i) for i in c.split("/"))
        comps.append(c)
        cd.setdefault(c[0], []).append(e)
        cd.setdefault(c[1], []).append(e)

    def rec(b=(), s=0, p=0, max_l=0, max_s=0):
        if len(b) > max_l:
            max_l = len(b)
            max_s = s
        elif len(b) == max_l:
            max_s = max(max_s, s)
        for i in cd[p]:
            if i in b:
                continue
            c = comps[i]
            op = c[0]
            if op == p:
                op = c[1]
            max_l, max_s = rec(b + (i,), s + c[0] + c[1], op, max_l, max_s)
        return max_l, max_s

    print(rec()[1])


if __name__ == '__main__':
    main()
