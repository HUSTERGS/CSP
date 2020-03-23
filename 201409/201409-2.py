# score 100
from sys import stdin

blockSet = set()
n = int(stdin.readline())
for _ in range(n):
    x1, y1, x2, y2 = tuple(int(x) for x in stdin.readline().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            blockSet.add((x, y))

print(len(blockSet))
