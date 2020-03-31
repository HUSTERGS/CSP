# score 100
from sys import stdin
from collections import deque

n, m = [int(x) for x in stdin.readline().strip().split()]


class Node:
    def __init__(self, is_switcher, index):
        self.is_switcher = is_switcher
        self.child = set()
        self.index = index


# 交换机编号与node的映射
switcher_connections = {x: Node(True, x) for x in range(1, n + 1)}
# 电脑编号到node的映射
computer_connections = {x: Node(False, x) for x in range(1, m + 1)}
for index, switcher in enumerate([int(x) for x in stdin.readline().strip().split()]):
    # 第index+2 台交换机所连接的交换机为switcher
    switcher_connections[index + 2].child.add(switcher_connections[switcher])
    switcher_connections[switcher].child.add(switcher_connections[index + 2])

for index, switcher in enumerate([int(x) for x in stdin.readline().strip().split()]):
    computer_connections[index + 1].child.add(switcher_connections[switcher])
    switcher_connections[switcher].child.add(computer_connections[index + 1])


def bfs(start_node):
    # 从某一个节点开始bfs,找到最远的点
    seen_node = set()
    queue = deque()
    queue.append((start_node, 0))
    while len(queue):
        # 当队列中为空的时候
        node, dist = queue.popleft()
        if node in seen_node:
            continue
        for child_n in node.child:
            if child_n not in seen_node:
                queue.append((child_n, dist + 1))
        seen_node.add(node)
        if len(seen_node) == n+m-1:
            return queue.popleft()


n1, d1 = bfs(switcher_connections[1])
n2, d2 = bfs(n1)
print(d2)
