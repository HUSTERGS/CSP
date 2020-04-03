# score 80
from sys import stdin
import heapq
n, m = [int(x) for x in stdin.readline().strip().split()]
root = 1
V = {}
max_dist = 0

for _ in range(m):
    v, u, t = [int(x) for x in stdin.readline().strip().split()]
    # (距离, 目标),用于heapify
    if v not in V:
        V[v] = []
    if u not in V:
        V[u] = []
    V[v].append((t, u))
    V[u].append((t, v))


E = V[root][:]
heapq.heapify(E)
seen_spots = set()
seen_spots.add(root)
# 判断条件改一下,并不是需要经过所有的点,而是要看到n
while n not in seen_spots:
    dist, target = heapq.heappop(E)
    if target not in seen_spots:
        max_dist = max(max_dist, dist)
        seen_spots.add(target)
        for d, t in V[target]:
            if t not in seen_spots:
                heapq.heappush(E, (d, t))

print(max_dist)