# score 75
from sys import stdin
from collections import deque

N, M = [int(x) for x in stdin.readline().strip().split()]
# 正向连接
pos_connections = {x: set() for x in range(1, N + 1)}
# 反向连接
neg_connections = {x: set() for x in range(1, N + 1)}
for _ in range(M):
    a, b = [int(x) for x in stdin.readline().strip().split()]
    pos_connections[a].add(b)
    neg_connections[b].add(a)

# 每一个点所知道的其他点
known_spots = {x: [set(), set()] for x in range(1, N + 1)}
for i in range(1, N + 1):
    # 初始化known_spots
    # 每一个点一开始知道的其他点是他所直接连接的点
    known_spots[i][0] = pos_connections[i].copy()
    known_spots[i][0].add(i)
    known_spots[i][1] = neg_connections[i].copy()

# 我连接的点，连接我的点都必然知道

queue = deque()
queue.extend([x for x in range(1, N + 1)])
while len(queue):
    current_spot = queue.popleft()
    for node in neg_connections[current_spot]:
        # 所有连接current spot的点
        if len(known_spots[current_spot][0] - known_spots[node][0]):
            # 开始向上传递
            known_spots[node][0] = known_spots[current_spot][0].union(known_spots[node][0])
            queue.append(node)

# 梅开二度
# 连接我的的点，我连接的的点都必然知道
queue.extend([x for x in range(1, N + 1)])
while len(queue):
    current_spot = queue.popleft()
    for node in pos_connections[current_spot]:
        if len(known_spots[current_spot][1] - known_spots[node][1]):
            known_spots[node][1] = known_spots[current_spot][1].union(known_spots[node][1])
            queue.append(node)

result = 0
for key, value in known_spots.items():
    if len(value[0].union(value[1])) == N:
        result += 1
print(result)
