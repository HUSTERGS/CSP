# score 100
from sys import stdin
import heapq
n, m, root = [int(stdin.readline().strip()) for _ in range(3)]

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
while len(seen_spots) != n:
    dist, target = heapq.heappop(E)
    if target not in seen_spots:
        max_dist = max(max_dist, dist)
        seen_spots.add(target)
        for d, t in V[target]:
            if t not in seen_spots:
                heapq.heappush(E, (d, t))
print(max_dist)