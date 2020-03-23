# score 100
from sys import stdin

n = int(stdin.readline())
H_time = [[int(x) for x in stdin.readline().split()] for _ in range(n)]
W_time = [[int(x) for x in stdin.readline().split()] for _ in range(n)]


def cross(x, y):
    a, b = x[0], x[1]
    c, d = y[0], y[1]
    if c > b or a > d:
        return False
    else:
        return True


total = 0
while len(H_time) and len(W_time):
    a, b = H_time[0]
    c, d = W_time[0]
    if cross(H_time[0], W_time[0]):
        total += min(b, d) - max(a, c)
    if b > d:
        W_time.pop(0)
    elif b < d:
        H_time.pop(0)
    else:
        H_time.pop(0)
        W_time.pop(0)


print(total)
