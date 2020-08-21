# score 90
# 使用了各种办法还是无法提高到100，一直超时
from sys import stdin
from collections import deque
import sys

m, n, q = [int(x) for x in stdin.readline().strip().split()]
canvas = [[".", ] * m for _ in range(n)]
sys.setrecursionlimit(100000)
queue = deque()
handled = set()


def filling(x, y, c):
    queue.append((x, y))
    while len(queue) != 0:
        x, y = queue.popleft()
        canvas[y][x] = c
        handled.add((x, y))
        if (x, y + 1) not in handled and 0 <= x < m and 0 <= y + 1 < n and canvas[y + 1][x] not in "-|+":
            queue.append((x, y + 1))
        if (x, y - 1) not in handled and 0 <= x < m and 0 <= y - 1 < n and canvas[y - 1][x] not in "-|+":
            queue.append((x, y - 1))
        if (x + 1, y) not in handled and 0 <= x + 1 < m and 0 <= y < n and canvas[y][x + 1] not in "-|+":
            queue.append((x + 1, y))
        if (x - 1, y) not in handled and 0 <= x - 1 < m and 0 <= y < n and canvas[y][x - 1] not in "-|+":
            queue.append((x - 1, y))


for i in range(q):
    string = stdin.readline().strip().split()
    if len(string) == 4:
        # 操作1 填充操作
        _, x, y, c = string
        x = int(x)
        y = n - int(y) - 1
        handled = set()
        filling(x, y, c)
    else:
        # 操作0 画线操作
        _, x1, y1, x2, y2 = tuple(int(x) for x in string)
        if x1 == x2:
            # 纵向的线段
            y1 = n - y1 - 1
            y2 = n - y2 - 1
            upper_bound = max(y1, y2)
            lower_bound = min(y1, y2)
            for y in range(lower_bound, upper_bound + 1):
                if canvas[y][x1] == "-" or canvas[y][x1] == "+":
                    canvas[y][x1] = "+"
                else:
                    canvas[y][x1] = "|"
        else:
            # 横向的线段
            y = n - y1 - 1
            upper_bound = max(x1, x2)
            lower_bound = min(x1, x2)
            for x in range(lower_bound, upper_bound + 1):
                if canvas[y][x] == "|" or canvas[y][x] == "+":
                    canvas[y][x] = "+"
                else:
                    canvas[y][x] = "-"

for line in canvas:
    print("".join(line))
