from adventlib import *


DAY = 3


def main():
    inp = store_input(DAY)
    if inp is None:
        return
    num = int(inp)
    l = 1
    x, y = 0, 0
    mp = {(0, 0): 1}
    def store(x, y):
        mp[(x, y)] = sum([
            mp.get((a, b), 0) for a, b in [
                (x + 1, y + 1),
                (x + 1, y),
                (x, y + 1),
                (x + 1, y - 1),
                (x - 1, y + 1),
                (x, y - 1),
                (x - 1, y),
                (x - 1, y - 1)]])
        print(mp[(x, y)], end=' ')
        if mp[(x, y)] > num:
            print(mp[(x, y)])
            exit(0)
    i = num
    while True:
        if i < l:
            x += i
            break
        for _ in range(l):
            x += 1
            store(x, y)
        i -= l
        if i < l:
            y += i
            break
        for _ in range(l):
            y += 1
            store(x, y)
        i -= l
        l += 1
        if i < l:
            x -= i
            break
        for _ in range(l):
            x -= 1
            store(x, y)
        i -= l
        if i < l:
            y -= i
            break
        for _ in range(l):
            y -= 1
            store(x, y)
        i -= l
        l += 1
    print(max(x, -x) + max(y, -y) - 1)


if __name__ == '__main__':
    main()
