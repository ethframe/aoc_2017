from collections import defaultdict


from adventlib import *


DAY = 23


def runner(code):
    sent = 0
    ip = 0
    regs = defaultdict(lambda: 0)

    def get_val(a):
        if a.isalpha():
            return regs[a]
        return int(a)

    cl = len(code)
    mulc = 0
    while 0 <= ip < cl:
        insn = code[ip]
        op = insn[0]
        if op == "set":
            regs[insn[1]] = get_val(insn[2])
        elif op == "add":
            regs[insn[1]] += get_val(insn[2])
        elif op == "sub":
            regs[insn[1]] -= get_val(insn[2])
        elif op == "mul":
            mulc += 1
            regs[insn[1]] *= get_val(insn[2])
        elif op == "mod":
            regs[insn[1]] %= get_val(insn[2])
        elif op == "jgz":
            if get_val(insn[1]) > 0:
                ip += get_val(insn[2])
                continue
        elif op == "jnz":
            if get_val(insn[1]) != 0:
                ip += get_val(insn[2])
                continue
        ip += 1
    return mulc


def primes_upto(limit):
    """
    Taken from https://rosettacode.org/wiki/Sieve_of_Eratosthenes#Python
    """
    is_prime = [False] * 2 + [True] * (limit - 1)
    for n in range(int(limit**0.5 + 1.5)):
        if is_prime[n]:
            for i in range(n*n, limit+1, n):
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]


def main():
    inp = store_input(DAY)
    if inp is None:
        return
    code = split_table(inp, None)

    print(runner(code))

    b = 81 * 100 + 100000
    c = b + 17000
    p = primes_upto(int(c ** 0.5 + 1.5))
    h = 0
    for i in range(b, c + 17, 17):
        for e in p:
            if i % e == 0:
                h += 1
                break
    print(h)


if __name__ == '__main__':
    main()
