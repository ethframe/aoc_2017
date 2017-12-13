from collections import defaultdict


from adventlib import *


DAY = 8


def main():
    inp = store_input(DAY)
    if inp is None:
        return
    lines = list(split_lines(inp))

    m = 0
    regs = defaultdict(lambda: 0)
    for insn in lines:
        r, op, d, _, c, cop, v = insn.split()
        d = int(d)
        v = int(v)
        pred = (cop == ">" and regs[c] > v or
                cop == ">=" and regs[c] >= v or
                cop == "==" and regs[c] == v or
                cop == "!=" and regs[c] != v or
                cop == "<" and regs[c] < v or
                cop == "<=" and regs[c] <= v)
        if pred:
            if op == "inc":
                regs[r] += d
            elif op == "dec":
                regs[r] -= d
            else:
                raise ValueError(op)
            if regs[r] > m:
                m = regs[r]
    print(max((v, r) for r, v in regs.items()))
    print(m)


if __name__ == '__main__':
    main()
