# score 100
from sys import stdin
import heapq

n, m = [int(x) for x in stdin.readline().strip().split()]
E = []


class Edge:
    def __init__(self, weight, start, end):
        self.weight = weight
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.weight < other.weight


class Vertex:
    def __init__(self):
        # pass
        self.edges = set()
        # self.added = False


# 标号到vertex对象的映射
index_to_vertex = {x: Vertex() for x in range(1, n + 1)}

for _ in range(m):
    a, b, c = [int(x) for x in stdin.readline().strip().split()]
    edge = Edge(c, a, b)
    index_to_vertex[a].edges.add(edge)
    index_to_vertex[b].edges.add(edge)

V_new = set()
V_new.add(index_to_vertex[1])
E_new = []
for edge in index_to_vertex[1].edges:
    heapq.heappush(E, edge)

while len(E_new) != n - 1:
    # 选取最小的边
    edge = heapq.heappop(E)
    start, end = edge.start, edge.end
    if index_to_vertex[start] in V_new and index_to_vertex[end] in V_new:
        continue
    E_new.append(edge)
    if index_to_vertex[start] not in V_new:
        V_new.add(index_to_vertex[start])
        for edge in index_to_vertex[start].edges:
            heapq.heappush(E, edge)
    else:
        V_new.add(index_to_vertex[end])
        for edge in index_to_vertex[end].edges:
            heapq.heappush(E, edge)

print(sum([x.weight for x in E_new]))
