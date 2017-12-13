from adventlib import *


DAY = 13


def main():
    inp = store_input(DAY)
    if inp is None:
        return
    inp = inp.rstrip("\n")
    lines = list(split_lines(inp))

    rec = []
    for l in lines:
        d, r = l.split(": ")
        rec.append((int(d), int(r)))

    delay = 0
    caught = True
    dr = {k: 2 * v - 2 for k, v in rec}
    lst = [k for k, _ in rec]
    l = max(dr) + 1
    while caught:
        delay += 1
        caught = False
        tick = 0
        sev = 0
        for tick in lst:
            if (tick + delay) % dr[tick] == 0:
                caught = True
                break
    print(delay)


if __name__ == '__main__':
    main()
