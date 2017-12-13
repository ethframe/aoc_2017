from adventlib import *


DAY = 6


def main():
    inp = store_input(DAY)
    if inp is None:
        return
    words = split_fields(inp, None)

    answer = 0
    seen = set()
    state = tuple(int(i) for i in words)
    while state not in seen:
        answer += 1
        seen.add(state)
        rd = max(state)
        idx = state.index(rd)
        state = list(state)
        state[idx] = 0
        while rd:
            idx = (idx + 1) % len(state)
            state[idx] += 1
            rd -= 1
        state = tuple(state)

    print(state)
    print(answer)

    answer = 0
    seen = set()
    while state not in seen:
        answer += 1
        seen.add(state)
        rd = max(state)
        idx = state.index(rd)
        state = list(state)
        state[idx] = 0
        while rd:
            idx = (idx + 1) % len(state)
            state[idx] += 1
            rd -= 1
        state = tuple(state)

    print(answer)


if __name__ == '__main__':
    main()
