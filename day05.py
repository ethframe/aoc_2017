from adventlib import *


DAY = 5


def main():
    inp = store_input(DAY)
    if inp is None:
        return
    lines = list(split_lines(inp))

    maze = list(map(int, lines))
    pos = 0
    steps = 0
    while pos != len(maze):
        npos = pos + maze[pos]
        if maze[pos] >= 3:
            maze[pos] -= 1
        else:
            maze[pos] += 1
        steps += 1
        pos = npos
    print(steps)


if __name__ == '__main__':
    main()
