from sys import stdin
from math import inf
import heapq

n, m = [int(x) for x in stdin.readline().strip().split()]


class Vertex:
    def __init__(self):
        self.d = inf
        self.adj = {}

    def __lt__(self, other):
        return self.d < other.d


vertexes = {x: Vertex() for x in range(1, n + 1)}
for _ in range(m):
    a, b, c = [int(x) for x in stdin.readline().strip().split()]
    vertexes[a].adj[b] = c
    vertexes[b].adj[a] = c

vertexes[1].d = 0
S = set()
V = list(vertexes.values())
cost = {x: 0 for x in range(1, n + 1)}
cost[1] = 0
while len(V):
    u = heapq.heappop(V)
    S.add(u)

    for v, d in u.adj.items():
        if vertexes[v] not in S:
            if u.d + d < vertexes[v].d:
                vertexes[v].d = u.d + d
                cost[v] = d
            elif u.d + d == vertexes[v].d:
                cost[v] = min(cost[v], d)


result = sum(cost.values())
if result == inf:
    a = 1/0
print(result)
