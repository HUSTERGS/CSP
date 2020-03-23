# score 100
from sys import stdin

N, M = (int(x) for x in stdin.readline().split())
windows = {}
for index in range(N):
    windows[index + 1] = tuple(int(x) for x in stdin.readline().split())

queue = [x for x in range(1, N + 1)]
queue.reverse()  # 从最上面到最下面的窗口序号
for _ in range(M):
    x, y = (int(x) for x in stdin.readline().split())
    clicked = False
    for index in queue:
        x1, y1, x2, y2 = windows[index]
        if x1 <= x <= x2 and y1 <= y <= y2:
            queue.remove(index)
            queue.insert(0, index)
            clicked = True
            print(index)
            break
    if not clicked:
        print("IGNORED")