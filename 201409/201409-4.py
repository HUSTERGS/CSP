# score 70
from sys import stdin
from collections import deque

n, m, k, d = [int(x) for x in stdin.readline().strip().split()]
shops = []
customers = {}
# 禁用点
abandon = set()
for _ in range(m):
    x, y = [int(x) for x in stdin.readline().strip().split()]
    shops.append((x, y))

# 合并顾客需求
for _ in range(k):
    x, y, c = [int(x) for x in stdin.readline().strip().split()]
    if (x, y) in customers:
        customers[(x, y)] += c
    else:
        customers[(x, y)] = c
for _ in range(d):
    x, y = [int(x) for x in stdin.readline().strip().split()]
    abandon.add((x, y))

source = deque()
# 多点开始dfs,由于先进去的一定比后进去的距离短
for shop in shops:
    # x, y坐标以及cost
    source.append((shop[0], shop[1], 0))

total_cost = 0
count = 0
bias_x = [1, -1, 0, 0]
bias_Y = [0, 0, 1, -1]

customer_count = len(customers)


def in_range_n(dot):
    x, y = dot[0], dot[1]
    return 1 <= x <= n and 1 <= y <= n


while customer_count:
    x, y, c = source.popleft()
    # 此步将分数从40提高到70
    if (x, y) in abandon:
        continue
    if (x, y) in customers:
        total_cost += c * customers[(x, y)]
        del customers[(x, y)]
        customer_count -= 1
    # 已经见过的点加入abandon
    abandon.add((x, y))
    for index in range(4):
        new_dot = (x + bias_x[index], y + bias_Y[index])
        if new_dot in abandon or (not in_range_n(new_dot)):
            continue
        source.append((new_dot[0], new_dot[1], c + 1))
print(total_cost)
