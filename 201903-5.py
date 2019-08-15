# score 0

from sys import stdin

n, m, k = [int(x) for x in stdin.readline().split()]

# class node:
#     def __init__(self, index, station_type):
#         self.index = index
#         self.paths = {self.index : 0}
#         self.station_type = station_type
#     def add_path(self, target, length):
#         # 如果新加入的边不存在或者比已存在的小，就将其换为新的长度
#         if target != self.index and target not in self.paths.keys() or self.paths[target] > length:
#             self.paths[target] = length
#         return
    
    # def __repr__(self):
    #     return "index = {}, station_type = {}, paths = {}".format(self.index, self.station_type, self.paths)
    # def __str__(self):
    #     return "index = {}, station_type = {}, paths = {}".format(self.index, self.station_type, self.paths)
# node 中存放的点是从1开始的，但是索引node的时候是从0开始的
#  处理每条边

def add_path(self, target, length):
    # 如果新加入的边不存在或者比已存在的小，就将其换为新的长度
    if target != self['index'] and target not in self['paths'].keys() or self['paths'][target] > length:
        self['paths'][target] = length
    return

# 读取数据
nodes = [{'index' : x + 1, 'paths': {x + 1 : 0}, 'station_type' : int(y)} for x, y in enumerate(stdin.readline().split())]
# nodes = [node(x + 1, int(y)) for x ,y in enumerate(stdin.readline().split())]
for i in range(m):
    source, target, length = [int(x) for x in stdin.readline().split()]
    # nodes[source - 1].add_path(target, length)
    # nodes[target - 1].add_path(source, length)
    add_path(nodes[source - 1], target, length)
    add_path(nodes[target - 1], source, length)
# print(nodes)


def find_min(current_path_value, V_set):
    # print('when find min, set = ', V_set)
    # print('when find min, values = ', current_path_value)
    current_min = 1
    flag = 0
    for index, value in enumerate(current_path_value):
        if current_path_value[current_min] == -1 or current_min in V_set:
            if index != 0 and index not in V_set and value != -1:
                current_min = index
                flag = 1
        else:
            if index != 0 and index not in V_set and value != -1 and value <= current_path_value[current_min]:
                current_min = index
                flag = 1
    if flag:
        return current_min
    else:
        return -1


    
def add_vertex(newNode, current_path_value, V_set):
    V_set.add(newNode['index'])
    # print("加入了: ", newNode.index)
    # print('node.paths = ', newNode.paths)
    for key, value in newNode['paths'].items():
        candidate = current_path_value[newNode['index']] + value
        # print("候选者等于: ", candidate)
        # 如果新添加的点所连接的边中，
        if key not in V_set and (current_path_value[key] == -1 or candidate < current_path_value[key]):
            current_path_value[key] = candidate
            # print("切换候选者")
            # print(current_path_value)
            # V_set.add(key)

def shortest_path(self):
    current_path_value = [ -1 ] * (n + 1)
    current_path_value[self['index']] = 0
    V_set = set()
    # 获取目前最短的路径的点的索引， 从1开始，作为初始点
    for _ in range(n):
        current_min_index = find_min(current_path_value, V_set)
        # print('current_min = ', current_min_index)
        # print('current_V_set = ', V_set)
        # print('node = ', nodes[current_min_index - 1])
        if current_min_index == -1:
            return current_path_value
        add_vertex(nodes[current_min_index - 1], current_path_value, V_set)
        # print(self.index, ': ')
        # print(current_path_value)
    return current_path_value
    




for i in range(n):
    current_path_value = shortest_path(nodes[i])
    nodes[i]['current_path_value'] = current_path_value
    # print('node: ', i + 1, ', path value = ', current_path_value)

for i in range(n):
    # print(nodes[i]['current_path_value'])
    newList = [y for x, y in enumerate(nodes[i]['current_path_value']) if y != -1 and nodes[x - 1]['station_type'] == 1]
    # print(newList)
    if len(newList) <= k:
        nodes[i]['sumup'] = sum(newList)
    else:
        newList.sort()
        nodes[i]['sumup'] = sum(newList[0:k])

for i in range(n):
    print(nodes[i]['sumup'])
'''
样例1
7 6 2
1 0 1 0 1 1 0
1 4 1
1 2 3
2 4 4
2 3 5
2 5 7
6 7 5

'''