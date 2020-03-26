# score 20
from sys import stdin

n, q = [int(x) for x in stdin.readline().split()]
A = [x for x in range(0, n + 1)]

U0 = 314882150829468584
U1 = 427197303358170108
U2 = 1022292690726729920
U3 = 1698479428772363217
U4 = 2006101093849356424
Us = (U0, U1, U2, U3, U4)


def f(x):
    return (x % 2009731336725594113) % 2019


for index in range(q):
    l, r = [int(x) for x in stdin.readline().split()]
    s = sum((f(A[x]) for x in range(l, r + 1)))
    t = s % 5
    print(s)
    for x in range(l, r + 1):
        A[x] *= Us[t]

