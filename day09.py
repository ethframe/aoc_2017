from adventlib import *


DAY = 9


def main():
    inp = store_input(DAY)
    if inp is None:
        return

    inp = inp.strip()
    grp = 0
    score = 0
    gbg = 0
    i = 0
    while i < len(inp):
        c = inp[i]
        if c == '{':
            grp += 1
            score += grp
            i += 1
        elif c == '}':
            grp -= 1
            i += 1
        elif c == ',':
            i += 1
        elif c == '<':
            i += 1
            while i < len(inp):
                c = inp[i]
                if c == '>':
                    i += 1
                    break
                elif c == '!':
                    i += 2
                else:
                    gbg += 1
                    i += 1
        else:
            raise ValueError(c)
    print(score, gbg)


if __name__ == '__main__':
    main()
