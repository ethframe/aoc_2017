from adventlib import *


def main():
    store_input(2)
    with open("day02.txt", "r") as fp:
        inp = fp.read()
    chk = 0
    for row in inp.split("\n"):
        if not row:
            continue
        cells = [int(i) for i in row.split("\t")]
        for i, a in enumerate(cells):
            for b in cells[i + 1:]:
                if a > b:
                    if a % b == 0:
                        chk += a // b
                elif b % a == 0:
                    chk += b // a
    print(chk)


if __name__ == '__main__':
    main()
