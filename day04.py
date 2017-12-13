from adventlib import *


DAY = 4


def main():
    if not store_input(DAY):
        return
    with open(f"day{DAY:02d}.txt", "r") as fp:
        inp = fp.read()
    c = 0
    for line in inp.strip().split("\n"):
        s = set()
        valid = True
        for word in line.split():
            word = ''.join(sorted(word))
            if word in s:
                valid = False
            else:
                s.add(word)
        if valid:
            c += 1
    print(c)


if __name__ == '__main__':
    main()
