# score 60
from sys import stdin
import heapq
from math import inf

n, m, root = [int(stdin.readline().strip()) for _ in range(3)]

vertex_dict = {}


class Vertex:
    def __init__(self, index):
        self.index = index
        self.adj = {}
        self.dist = None  # 该点距离生成树的最小距离

    def __lt__(self, other):
        return self.dist < other.dist


for _ in range(m):
    v, u, t = [int(x) for x in stdin.readline().strip().split()]
    # 如果点v,u之前没有出现过就将其加入
    if v not in vertex_dict:
        vertex_dict[v] = Vertex(v)
    if u not in vertex_dict:
        vertex_dict[u] = Vertex(u)
    # 添加边
    vertex_dict[v].adj[u] = t
    vertex_dict[u].adj[v] = t

V = set()
V_new = []
vertex_dict[root].dist = -inf
heapq.heappush(V_new, vertex_dict[root])
max_dist = -inf
while len(V_new) != 0:
    v = heapq.heappop(V_new)
    V.add(v.index)
    max_dist = max(max_dist, v.dist)
    for key, value in v.adj.items():
        if key not in V:
            if vertex_dict[key].dist is None:
                vertex_dict[key].dist = value
                heapq.heappush(V_new, vertex_dict[key])
            elif value < vertex_dict[key].dist:
                vertex_dict[key].dist = value

print(max_dist)
