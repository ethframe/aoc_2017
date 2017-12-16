from adventlib import *


DAY = 16


def main():
    inp = store_input(DAY)
    if inp is None:
        return
    inp = inp.rstrip("\n")
    comm = inp.split(",")
    progs = list("abcdefghijklmnop")

    opt = []
    curr = list(range(16))
    mapp = list("abcdefghijklmnop")
    for c in comm:
        if c[0] == "s":
            n = int(c[1:])
            curr = curr[-n:] + curr[:-n]
        elif c[0] == "x":
            a, b = map(int, c[1:].split("/"))
            curr[a], curr[b] = curr[b], curr[a]
        elif c[0] == "p":
            an, bn = c[1:].split("/")
            a = mapp.index(an)
            b = mapp.index(bn)
            mapp[a], mapp[b] = mapp[b], mapp[a]

    mapp = dict(zip(progs, mapp))
    for _ in range(1000000000 % 60):
        progs = [mapp[progs[i]] for i in curr]

    print("".join(progs))


if __name__ == '__main__':
    main()
