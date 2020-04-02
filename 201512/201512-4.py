from sys import stdin
import sys

sys.setrecursionlimit(1000000)

n, m = [int(x) for x in stdin.readline().strip().split()]

connections = {x: [] for x in range(1, n + 1)}

paths = set()
for _ in range(m):
    a, b = [int(x) for x in stdin.readline().strip().split()]
    connections[a].append(b)
    connections[b].append(a)

start_point = []
for key, value in connections.items():
    if len(value) % 2 == 1:
        start_point.append(key)
    # 不能有度为0的点
    if len(value) == 0:
        print(-1)
        exit(0)

result = []

visited = set()


def dfs(start):
    visited.add(start)
    result.append(start)
    for dst in connections[start]:
        if (dst, start) not in paths and (start, dst) not in paths:
            paths.add((dst, start))
            paths.add((start, dst))
            if dfs(dst):
                return True
            else:
                paths.remove((dst, start))
                paths.remove((start, dst))
    if len(visited) != n or len(result) != m + 1:
        # 没有访问到所有的点
        result.pop()
        visited.remove(start)
        return False
    else:
        # 到了最后一层
        return True


if len(start_point) > 2 or len(start_point) == 1:
    print(-1)
    exit(0)

if len(start_point) == 2 and (1 not in start_point):
    print(-1)
    exit(0)

for _, value in connections.items():
    value.sort()

if dfs(1):
    print(" ".join([str(x) for x in result]))
else:
    print(-1)
