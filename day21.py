from adventlib import *


DAY = 21


def rotate(p):
    return tuple(zip(*[reversed(i) for i in p]))


def flip(p):
    return tuple([tuple(reversed(i)) for i in p])


def main():
    inp = store_input(DAY)
    if inp is None:
        return
    lines = list(split_lines(inp))

    rules = {}
    for rule in lines:
        src, dst = rule.split(" => ")
        src = tuple([tuple(s) for s in src.split("/")])
        dst = [list(s) for s in dst.split("/")]
        for _ in range(2):
            for _ in range(4):
                rules[src] = dst
                src = rotate(src)
            src = flip(src)

    initial = [".#.", "..#", "###"]
    field = [list(i) for i in initial]

    for _ in range(18):
        w = len(field)
        new = []
        if w % 2 == 0:
            for row in range(0, w, 2):
                new.extend([[], [], []])
                for col in range(0, w, 2):
                    pat = tuple([tuple(r[col:col+2]) for r in field[row:row+2]])
                    sub = rules[pat]
                    new[-3].extend(sub[-3])
                    new[-2].extend(sub[-2])
                    new[-1].extend(sub[-1])
        elif w % 3 == 0:
            for row in range(0, w, 3):
                new.extend([[], [], [], []])
                for col in range(0, w, 3):
                    pat = tuple([tuple(r[col:col+3]) for r in field[row:row+3]])
                    sub = rules[pat]
                    new[-4].extend(sub[-4])
                    new[-3].extend(sub[-3])
                    new[-2].extend(sub[-2])
                    new[-1].extend(sub[-1])
        field = new

    c = 0
    for row in field:
        for col in row:
            if col == "#":
                c += 1

    print(c)


if __name__ == '__main__':
    main()
