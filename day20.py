from collections import deque


from adventlib import *


DAY = 20


class Vec(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def dist(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def tup(self):
        return self.x, self.y, self.z


def ss(a, b):
    return a.x * b.x >= 0 and a.y * b.y >= 0 and a.z * b.z >= 0


class Particle(object):
    def __init__(self, id, pos, vel, acc):
        self.id = id
        self.pos = Vec(*pos)
        self.vel = Vec(*vel)
        self.acc = Vec(*acc)

    def dist(self):
        return self.pos.dist()

    def upd(self):
        self.vel += self.acc
        self.pos += self.vel

    def ign(self):
        return ss(self.vel, self.acc) and ss(self.pos, self.vel)


def main():
    inp = store_input(DAY)
    if inp is None:
        return

    lines = list(split_lines(inp))

    parts = []
    for pi, l in enumerate(lines):
        p, v, a = l.split(", ")
        ps = [int(i) for i in p[3:-1].split(",")]
        vs = [int(i) for i in v[3:-1].split(",")]
        cs = [int(i) for i in a[3:-1].split(",")]
        parts.append(Particle(pi, ps, vs, cs))

    closest = parts[0].id
    dist = parts[0].dist()
    parts = deque(parts)
    for i in range(2000):
        if i % 100 == 0:
            print(i)
        nparts = deque([])
        colld = {}
        closest = parts[0].id
        dist = parts[0].dist()
        for p in parts:
            if p.id is None:
                continue
            pd = p.dist()
            if pd < dist:
                dist = pd
                closest = p.id
            p.upd()
            t = p.pos.tup()
            c = colld.get(t, None)
            if c is not None:
                c.id = None
            else:
                colld[t] = p
                nparts.append(p)
        parts = nparts
    print(len(parts))


if __name__ == '__main__':
    main()
