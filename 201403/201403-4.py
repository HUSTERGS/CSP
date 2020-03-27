# score 100
from sys import stdin
from collections import deque

n, m, k, r = [int(x) for x in stdin.readline().strip().split()]
routers = []
option_routers = set()
for _ in range(n):
    x, y = [int(x) for x in stdin.readline().strip().split()]
    routers.append((x, y))

for _ in range(m):
    x, y = [int(x) for x in stdin.readline().strip().split()]
    option_routers.add((x, y))

all_routers = set(routers).union(option_routers)
routers_seen = set()
source_router = routers[0]
target_router = routers[1]
source = deque()

source.append((source_router[0], source_router[1], 0, 0))


def in_range(s, t):
    return (s[0] - t[0]) ** 2 + (s[1] - t[1]) ** 2 <= r * r


# 同样是进行dfs，默认加入所有的路由器，包括已经安装的和可选的，dfs会自动选择最短的跳转路径
while True:
    router = source.popleft()
    # 如果已经见过了则直接跳过
    if (router[0], router[1]) in routers_seen:
        continue
    all_routers.remove((router[0], router[1]))
    routers_seen.add((router[0], router[1]))
    for rt in all_routers:
        if in_range(router, rt):
            # 如果某一个路由器在范围之内
            if rt == routers[1]:
                # 如果刚好是目标路由器则直接结束,输出结果
                print(router[2])
                exit(0)
            if rt in option_routers:
                # 如果是可选的路由器,将其加1
                source.append((rt[0], rt[1], router[2] + 1, router[3] + 1))
            else:
                source.append((rt[0], rt[1], router[2] + 1, router[3]))
