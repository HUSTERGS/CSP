from sys import stdin

m, l, r = [int(x) for x in stdin.readline().strip().split()]
km = [int(x) for x in stdin.readline().strip().split()]
an = [1, ]
Q = 998244353
for n in range(1, r+1):
    s = 0
    for i in range(1, min(n, m)+1):
        s += km[i-1] * an[n-i] % Q
        s %= Q
    an.append(s)
    if n >= l:
        print(an[n])