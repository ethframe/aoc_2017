from adventlib import *


DAY = 7


def main():
    inp = store_input(DAY)
    if inp is None:
        return
    lines = list(split_lines(inp))

    ids = {}
    deps = {}
    rdeps = {}
    for line in lines:
        desc_dep = line.split(" -> ")
        desc = desc_dep[0]
        name, id_ = desc.split(" ")
        ids[name] = int(id_[1:-1])
        if len(desc_dep) == 2:
            dep = desc_dep[1]
            deplist = dep.split(", ")
            deps[name] = deplist
            for d in deplist:
                rdeps[d] = name

    print(set(ids) - set(rdeps))

    queue = [list(set(ids) - set(rdeps))[0]]
    weights = {}
    while queue:
        c = queue[-1]
        if not all(d in weights for d in deps.get(c, [])):
            for d in deps.get(c, []):
                if d not in weights:
                    queue.append(d)
            continue
        queue.pop()
        dw = [weights[d] for d in deps.get(c, [])]
        if dw and len(set(dw)) != 1:
            print(c, dw, deps.get(c, []), [ids[d] for d in deps.get(c, [])])
        weights[c] = sum([ids[c]] + dw)


if __name__ == '__main__':
    main()
