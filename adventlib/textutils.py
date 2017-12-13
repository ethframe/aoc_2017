def split_lines(s, strip=False):
    for line in s.strip("\n").split("\n"):
        if strip:
            line = line.strip()
        if line:
            yield line


def split_fields(s, sep="\t"):
    return s.split(sep)


def split_table(s, fs="\t"):
    return [split_fields(l, fs) for l in split_lines(s)]
