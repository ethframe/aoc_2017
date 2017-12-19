import string


from adventlib import *


DAY = 19


def main():
    inp = store_input(DAY)
    if inp is None:
        return
    lines = list(split_lines(inp))

    diag = [list(l) for l in lines]

    x, y = 0, 0

    while diag[0][y] != "|":
        y += 1

    letters = []

    D, U, R, L = 0, 1, 2, 3

    d = D

    steps = 0
    while True:
        if diag[x][y] == "|":
            steps += 1
            if d == R:
                y += 1
            elif d == L:
                y -= 1
            elif d == D:
                x += 1
            elif d == U:
                x -= 1
        elif diag[x][y] == "+":
            if d in (R, L):
                if diag[x + 1][y] != " ":
                    d = D
                    x += 1
                    steps += 1
                elif diag[x - 1][y] != " ":
                    d = U
                    x -= 1
                    steps += 1
            elif d in (U, D):
                if diag[x][y + 1] != " ":
                    d = R
                    y += 1
                    steps += 1
                elif diag[x][y - 1] != " ":
                    d = L
                    y -= 1
                    steps += 1
        elif diag[x][y] == "-":
            if d == R:
                y += 1
            elif d == L:
                y -= 1
            elif d == D:
                x += 1
            elif d == U:
                x -= 1
            steps += 1
        elif diag[x][y] in string.ascii_uppercase:
            letters.append(diag[x][y])
            if d == D:
                x += 1
            elif d == U:
                x -= 1
            elif d == R:
                y += 1
            elif d == L:
                y -= 1
            steps += 1
        else:
            break

    print("".join(letters), steps)


if __name__ == '__main__':
    main()
