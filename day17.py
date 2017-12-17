from adventlib import *


DAY = 17


class n:
    __slots__ = ("v", "n")
    def __init__(self, v, n):
        self.v = v
        self.n = n

    def after(self, v):
        c = n(v, self.n)
        self.n = c
        return c


def main():
    inp = store_input(DAY)
    if inp is None:
        return
    inp = int(inp)

    b = n(0, 1)
    b.n = b
    c = 0
    for i in range(1, 5000000 + 1):
        for _ in range(inp):
            b = b.n
        b = b.after(i)

    while b.v != 0:
        b = b.n
    print(b.n.v)


if __name__ == '__main__':
    main()
