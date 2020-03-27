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
known_spots = {x: set() for x in range(1, N + 1)}
for i in range(1, N + 1):
    # 初始化known_spots
    # 每一个点一开始知道的其他点是他所直接连接的点
    known_spots[i] = pos_connections[i].copy()
    known_spots[i].add(i)

# 我知道的点，连接我的点都必然知道
# 不妨直接从点1开始

queue = deque()
queue.extend([x for x in range(1, N + 1)])
while len(queue):
    current_spot = queue.popleft()
    for node in neg_connections[current_spot]:
        # 所有连接current spot的点
        if len(known_spots[current_spot] - known_spots[node]):
            # 开始向上传递
            known_spots[node] = known_spots[current_spot].union(known_spots[node])
            queue.append(node)

# 反向操作一波
for key, value in known_spots.items():
    known_spots[key] = known_spots[key].union(neg_connections[key])

reverse_known = {x: set() for x in range(1, N + 1)}
for key, value in known_spots.items():
    for node in value:
        reverse_known[node].add(key)

qualified_node = set()
for key, value in known_spots.items():
    if len(value) == N:
        qualified_node.add(key)

for key, value in reverse_known.items():
    if len(value) == N:
        qualified_node.add(key)
# print(known_spots)
# print(reverse_known)
print(len(qualified_node))
