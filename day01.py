def main():
    with open("day01.txt", "r") as fp:
        l = [int(i) for i in fp.read()]
    s = 0
    for a, b in zip(l, l[len(l) // 2:] + l[:len(l) // 2]):
        if a == b:
            s += a
    print(s)


if __name__ == '__main__':
    main()
