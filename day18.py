from collections import defaultdict, deque


from adventlib import *


DAY = 18


def runner(code, pid):
    yield
    sent = 0
    ip = 0
    regs = defaultdict(lambda: 0)
    regs["p"] = pid

    def get_val(a):
        if a.isalpha():
            return regs[a]
        return int(a)

    cl = len(code)
    while 0 <= ip < cl:
        insn = code[ip]
        op = insn[0]
        if op == "snd":
            sent += 1
            yield get_val(insn[1])
        elif op == "set":
            regs[insn[1]] = get_val(insn[2])
        elif op == "add":
            regs[insn[1]] = get_val(insn[1]) + get_val(insn[2])
        elif op == "mul":
            regs[insn[1]] = get_val(insn[1]) * get_val(insn[2])
        elif op == "mod":
            regs[insn[1]] = get_val(insn[1]) % get_val(insn[2])
        elif op == "rcv":
            regs[insn[1]] = yield None
        if op == "jgz":
            if get_val(insn[1]) > 0:
                ip += get_val(insn[2])
            else:
                ip += 1
        else:
            ip += 1
    print(pid, "sent", sent)


def main():
    inp = store_input(DAY)
    if inp is None:
        return

    code = split_table(inp, None)

    ip = 0
    regs = defaultdict(lambda: 0)

    def get_val(a):
        if a.isalpha():
            return regs[a]
        return int(a)

    last = None
    while 0 <= ip < len(code):
        insn = code[ip]
        op = insn[0]
        if op == "snd":
            last = get_val(insn[1])
        elif op == "set":
            regs[insn[1]] = get_val(insn[2])
        elif op == "add":
            regs[insn[1]] = get_val(insn[1]) + get_val(insn[2])
        elif op == "mul":
            regs[insn[1]] = get_val(insn[1]) * get_val(insn[2])
        elif op == "mod":
            regs[insn[1]] = get_val(insn[1]) % get_val(insn[2])
        elif op == "rcv":
            if get_val(insn[1]) != 0:
                break
        if op == "jgz":
            if get_val(insn[1]) > 0:
                ip += get_val(insn[2])
            else:
                ip += 1
        else:
            ip += 1

    print(last)

    a = runner(code, 0)
    b = runner(code, 1)

    next(a)
    next(b)

    al = deque([])
    bl = deque([])

    arc = a.send(None)
    brc = b.send(None)
    ac = 0
    bc = 0
    while True:
        while arc is not None:
            ac += 1
            al.append(arc)
            arc = a.send(None)

        while brc is not None:
            bc += 1
            bl.append(brc)
            brc = b.send(None)

        if not al and not bl:
            break

        while arc is None and bl:
            arc = a.send(bl.popleft())

        while brc is None and al:
            brc = b.send(al.popleft())

    print(bc)


if __name__ == '__main__':
    main()
