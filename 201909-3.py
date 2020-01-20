# score 40
from sys import stdin

m, n = [int(x) for x in stdin.readline().strip().split()]
p, q = [int(x) for x in stdin.readline().strip().split()]

color_matrix = [[tuple(), ] * m for _ in range(n)]


def regulate(string):
    if len(string) == 7:
        return string[1:3], string[3:5], string[5:7]
    elif len(string) == 4:
        return string[1] * 2, string[2] * 2, string[3] * 2
    elif len(string) == 2:
        return [string[1] * 2, ] * 3


def hex_to_int(RGB):
    return tuple(eval(f"0x{x}") for x in RGB)


for j in range(n):
    for i in range(m):
        color_matrix[j][i] = hex_to_int(regulate(stdin.readline().strip()))


def add(a, b):
    a[0] += b[0]
    a[1] += b[1]
    a[2] += b[2]


def divide(a, c):
    for i in range(3):
        a[i] //= c


def equal(a, b):
    return a[0] == b[0] and a[1] == b[1] and a[2] == b[2]


def generate_ascii(color):
    prefix = r"\x1B"
    string = f"[48;2;{color[0]};{color[1]};{color[2]}m "
    string = "".join([r"\x" + hex(ord(x))[2:].upper() for x in string])
    return prefix + string


pre = (0, 0, 0)
default = (0, 0, 0)
t = None
for i in range(n // q):
    for j in range(m // p):
        t = [0, 0, 0]
        t[0] = sum(color_matrix[i * q + r][c + j * p][0] for r in range(q) for c in range(p))
        t[1] = sum(color_matrix[i * q + r][c + j * p][1] for r in range(q) for c in range(p))
        t[2] = sum(color_matrix[i * q + r][c + j * p][2] for r in range(q) for c in range(p))
        # for r in range(q):
        #     for c in range(p):
        #         add(t, color_matrix[i * q + r][c + j * p])
        divide(t, q * p)
        if equal(t, pre):
            print(r"\x20", end="")
        elif equal(t, default):
            print(r"\x1B\x5B\x30\x6D\x20", end="")
        else:
            print(generate_ascii(t), end="")
        pre = t
    if not equal(t, default):
        print(r"\x1B\x5B\x30\x6D", end="")
        pre = default
    print(r"\x0A", end="")
