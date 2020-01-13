
from sys import stdin
from math import inf
# n, m, root = [int(stdin.readline()) for x in range(3)]

n = 4
m = 5
root = 1
string = '''1 2 3
1 3 4
1 4 5
2 3 8
3 4 2'''
class Vertex(object):
    def __init__(self, index):
        self.index = index # 节点序号
        self.adjList = {} # 相邻节点的List
        self.level = None
    def add_adj(self, target, dist):
        if target not in self.adjList:
            self.adjList[target] = dist
        elif self.adjList[target] > dist:
            self.adjList[target] = dist
    def __str__(self):
        print("index = ", self.index)
        print("adjList = ", self.adjList)
        print("level = ", self.level, end='\n\n')
        return ""
vertexList = [Vertex(0), ] # 多计算一个点
vertexList.extend([Vertex(i) for i in range(1, n+1)])


remainVertextSet = vertexList[:] # 所有的点
currentVertexSet = set() # 已经加入的点

min_dist = [inf, ] * (n + 1) # 用于记录最小距离的
min_dist[root] = 0
vertexList[root].level = 1

# 读入数据
# for i in range(m):
#     v1, v2, dist = [int(x) for x in stdin.readline().split()]
#     vertexList[v1].add_adj(v2, dist)
#     vertexList[v2].add_adj(v1, dist)

for line in string.split("\n"):
    v1, v2, dist = [int(x) for x in line.split()]
    vertexList[v1].add_adj(v2, dist)
    vertexList[v2].add_adj(v1, dist)
    

while len(remainVertextSet):
    # 遍历所有剩余的点, 找出距离 root 最短的点
    min_v = min(remainVertextSet, key=lambda x : min_dist[x.index])
    # print("min_v = \n", min_v)
    remainVertextSet.remove(min_v)
    currentVertexSet.add(min_v.index)
    # print(min_v.adjList)
    for target, dist in min_v.adjList.items():
        if target not in currentVertexSet and min_dist[target] > dist + min_dist[min_v.index]:
            min_dist[target] = dist + min_dist[min_v.index]
            vertexList[target].level = min_v.level + 1
            print("添加了 v = ", target)
            print(target, " to ", min_v.index , " = ", min_dist[target])


print(min_dist)
print(x.level for x in vertexList)





'''
4
5
1
1 2 3
1 3 4
1 4 5
2 3 8
3 4 2
'''