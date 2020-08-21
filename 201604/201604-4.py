# score 10
from sys import stdin
from collections import deque

n, m, t = (int(x) for x in stdin.readline().strip().split())
dangerous_spots = {}

for _ in range(t):
    r, c, a, b = (int(x) for x in stdin.readline().strip().split())
    dangerous_spots[(r, c)] = (a, b)


def in_danger(opt, t):
    return opt in dangerous_spots and dangerous_spots[opt][0] <= t <= dangerous_spots[opt][1]


def next_moves(r, c):
    options = []
    if 1 <= r + 1 <= n and 1 <= c <= m:
        options.append((r + 1, c))
    if 1 <= r - 1 <= n and 1 <= c <= m:
        options.append((r - 1, c))
    if 1 <= r <= n and 1 <= c + 1 <= m:
        options.append((r, c + 1))
    if 1 <= r <= n and 1 <= c - 1 <= m:
        options.append((r, c - 1))
    return options


queue = deque()
queue.append((1, 1, 0))  # (r, c, time)
visited = set()
while True:
    r, c, t = queue.popleft()
    if (r, c) == (n, m):
        print(t)
        break
    visited.add((r, c, t))
    options = next_moves(r, c)
    for opt in options:
        if (*opt, t + 1) not in visited and not in_danger(opt, t + 1) :
            queue.append((*opt, t + 1))
