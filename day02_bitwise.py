from adventlib import *


def div(a, b):
    q = 0
    while a > b:
        d = b
        v = 1
        while a >= d << 1:
            d <<= 1
            v <<= 1
        # a -= d
        while d:
            a, d = a ^ d, ((~a) & d) << 1
        q += v
    if a == b:
        return q + 1, 0
    return q, a


def main():
    inp = store_input(2)
    if inp is None:
        return
    chk = 0
    for row in inp.split("\n"):
        if not row:
            continue
        cells = [int(i) for i in row.split("\t")]
        for i, a in enumerate(cells, 1):
            for b in cells[i:]:
                q, r = div(a, b)
                if r != 0:
                    q, r = div(b, a)
                if r == 0:
                    # chk += q
                    while q:
                        chk, q = chk ^ q, (chk & q) << 1
    print(chk)


if __name__ == '__main__':
    main()
