from sys import stdin
from heapq import nsmallest

n, X, Y = [int(x) for x in stdin.readline().strip().split()]
spots = []

def dist(x, y):
    return (x - X) ** 2 + (y - Y) ** 2

for i in range(n):
    x, y = [int(x) for x in stdin.readline().strip().split()]
    spots.append((dist(x, y), i))

result = nsmallest(3, spots)
print("\n".join([str(x[1] + 1) for x in result]))