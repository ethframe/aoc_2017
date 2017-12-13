from adventlib import *


DAY = 11


def main():
    inp = store_input(DAY)
    if inp is None:
        return
    inp = inp.rstrip("\n")
    
    steps = split_fields(inp, ",")
    x, y = 0, 0

    mx = 0

    for i in steps:
        if i == "n":
            x += 1
        elif i == "s":
            x -= 1
        elif i == "ne":
            if y % 2 == 1:
                x += 1
            y += 1
        elif i == "se":
            if y % 2 == 0:
                x -= 1
            y += 1
        elif i == "nw":
            if y % 2 == 1:
                x += 1
            y -= 1
        elif i == "sw":
            if y % 2 == 0:
                x -= 1
            y -= 1

        tx, ty = x, y
        answer = 0
        while x != 0 and y != 0:
            answer += 1
            if x > 0:
                if y > 0:
                    if y % 2 == 0:
                        x -= 1
                    y -= 1
                else:
                    if y % 2 == 0:
                        x -= 1
                    y += 1
            else:
                if y > 0:
                    if y % 2 == 1:
                        x += 1
                    y -= 1
                else:
                    if y % 2 == 1:
                        x += 1
                    y += 1
        answer = abs(x) + abs(y) + answer
        if answer > mx:
            mx = answer
        x, y = tx, ty

    answer = mx

    print(answer)


if __name__ == '__main__':
    main()
