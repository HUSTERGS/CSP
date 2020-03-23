# score 100
from sys import stdin
n = int(stdin.readline())
m = int(stdin.readline())
students = [x for x in range(1, n+1)]
for _ in range(m):
    p, q = [int(x) for x in stdin.readline().split()]
    index = students.index(p)
    students.remove(p)
    students.insert(q + index, p)
print(" ".join(str(p) for p in students))