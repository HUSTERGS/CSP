# score 100
from sys import stdin

m, n = (int(x) for x in stdin.readline().split())
matrix = [[int(x) for x in stdin.readline().split()] for _ in range(m)]

for i in reversed(range(0, n)):
    print(" ".join(str(matrix[j][i]) for j in range(0, m)))


