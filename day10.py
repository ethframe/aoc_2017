from functools import reduce


from adventlib import *


DAY = 10


def main():
    inp = store_input(DAY)
    if inp is None:
        return
    inp = inp.rstrip("\n")
    words = split_fields(inp, ",")
    vals = [17, 31, 73, 47, 23]

    insn = [ord(i) for i in inp.strip()] + vals
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

    sp = ""
    for i in range(16):
        sp += "%02x" % reduce(lambda a, b: a ^ b, lst[i * 16 + 1: i * 16 + 16], lst[i * 16])
    print(sp)


if __name__ == '__main__':
    main()
