from sys import stdin
from math import sqrt, pi, acos
from itertools import combinations
n, m = [int(x) for x in stdin.readline().strip().split()]
r = float(stdin.readline())
O_position = [float(x) for x in stdin.readline().strip().split()]

Ps = []
for _ in range(m):
    Pi = [float(x) for x in stdin.readline().strip().split()]
    Ps.append(Pi)


# 先只考虑二维的情况
def dist(A, B):
    return sqrt(sum((a - b) ** 2 for a, b in zip(A, B)))

def dist_2(A, B):
    return sum((a - b) ** 2 for a, b in zip(A, B))

def trango(a, b):
    if a < b:
        a, b = b, a
    return sqrt(a ** 2 - b ** 2)


def min_distance(P1, P2):
    a = dist(P1, O_position)
    b = dist(P2, O_position)
    c = dist(P1, P2)
    cosc = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
    sinc = sqrt(1 - cosc ** 2)
    d = a * b * sinc / c
    if d >= r:
        return c

    cosq = r / a
    cosp = r / b
    alpa = acos(cosc) - acos(cosq) - acos(cosp)
    return trango(a, r) + trango(b, r) + abs(r * alpa)

result_dict = {}
for combi in combinations(range(m), 2):
    result_dict[combi] = min_distance(Ps[combi[0]], Ps[combi[1]])


for i in range(m):
    temp = 0
    for j in range(m):
        if j == i:
            continue
        if (i, j) in result_dict:
            temp += result_dict[(i, j)]
        else:
            temp += result_dict[(j, i)]
    print(temp)
# O_position = [0, 0]
# r = 1
# print(min_distance([0, 1], [0, -1]))