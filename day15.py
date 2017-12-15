from adventlib import *


DAY = 15


def main():
    inp = store_input(DAY)
    if inp is None:
        return
    phrases = split_table(inp, None)

    A = int(phrases[0][-1])
    B = int(phrases[1][-1])

    A_F = 16807
    B_F = 48271
    MOD = 2147483647

    a = A
    b = B
    c = 0
    for _ in range(5000000):
        a = (a * A_F) % MOD
        while a & 0x3 != 0:
            a = (a * A_F) % MOD
        b = (b * B_F) % MOD
        while b & 0x7 != 0:
            b = (b * B_F) % MOD
        if (a ^ b) & 0xFFFF == 0:
            c += 1

    print(c)


if __name__ == '__main__':
    main()
