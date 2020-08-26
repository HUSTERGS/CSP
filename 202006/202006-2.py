# score 60
from sys import stdin

n, a, b = [int(x) for x in stdin.readline().strip().split()]

u = {}
v = {}
key_set = set()
for _ in range(a):
    key, value = [int(x) for x in stdin.readline().strip().split()]
    key_set.add(key)
    u[key] = value

uv = 0

for _ in range(b):
    key, value = [int(x) for x in stdin.readline().strip().split()]
    if key in key_set:
        uv += u[key] * value

print(uv)

'''
10 3 4
4 5
7 -3
10 1
1 10
4 20
5 30
7 40
'''