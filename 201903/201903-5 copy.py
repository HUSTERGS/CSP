from sys import stdin
from math import inf
n, m, k = [int(x) for x in stdin.readline().split()]
types = [int(x) for x in stdin.readline().split()]

d = [[inf,] * n for i in range(n)]




for i in range(m):
    # 读取每一条边
    source, target, dist = [int(x) for x in stdin.readline().split()]
    # 因为可能有重边和自环，所以就取较小的值
    if source != target:
        min_value = min(dist, d[target-1][source-1])
        d[source-1][target-1] = min_value
        d[target-1][source-1] = min_value

for i in range (n):
    # 自己到自己的距离为 0
    d[i][i] = 0

for u in range(n):
    for i in range(n):
        for j in [x for x in range(n) if types[x] == 1]:
            if d[i][j] > d[i][u] + d[u][j]:
                d[i][j] = d[i][u] + d[u][j]

for i in range(n):
    dist_list = [y for x, y in enumerate(d[i]) if types[x] == 1 and d[i][x] != inf]
    # print("dist_list = ", dist_list)
    if len(dist_list) <= k:
        print(sum(dist_list))
    else:
        dist_list.sort()
        print(sum(dist_list[0:k]))
