# score 100
from sys import stdin

n, m = [int(x) for x in stdin.readline().strip().split()]

connections = {x: [] for x in range(1, n + 1)}

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
stack = []

now = []  # 充当运行时存放参数的栈


# Hierholzer算法,非递归版本
def dfs(start):
    now.append(start)
    while True:
        while len(connections[start]):
            dst = connections[start].pop()
            connections[dst].remove(start)
            start = dst
            now.append(start)
        if len(connections[start]) == 0:
            try:
                result.append(now.pop())
                if len(result) != m + 1:
                    start = now[-1]
            except:
                return
        if len(result) == m + 1:
            return


if len(start_point) > 2 or len(start_point) == 1:
    print(-1)
    exit(0)

if len(start_point) == 2 and (1 not in start_point):
    print(-1)
    exit(0)

for _, value in connections.items():
    value.sort(reverse=True)

dfs(1)
if len(result) == m + 1:
    print(" ".join([str(x) for x in result[::-1]]))
else:
    print(-1)
    exit(0)
