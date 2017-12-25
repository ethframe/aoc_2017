from collections import defaultdict


from adventlib import *


DAY = 25


def main():
    initial = "A"
    steps = 12683008
    rules = {"A": {0: (1, 1, "B"), 1: (0, -1, "B")},
             "B": {0: (1, -1, "C"), 1: (0, 1, "E")},
             "C": {0: (1, 1, "E"), 1: (0, -1, "D")},
             "D": {0: (1, -1, "A"), 1: (1, -1, "A")},
             "E": {0: (0, 1, "A"), 1: (0, 1, "F")},
             "F": {0: (1, 1, "E"), 1: (1, 1, "A")}}


    tape = defaultdict(lambda: 0)

    pos = 0
    state = initial
    for _ in range(steps):
        tape[pos], m, state = rules[state][tape[pos]]
        pos += m

    print(sum(tape.values()))


if __name__ == '__main__':
    main()
