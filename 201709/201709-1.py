# score 100
from sys import stdin
N = int(stdin.readline())
N = N // 10
sum = 0
while True:
    if N >= 5:
        N -= 5
        sum += 7
    elif N >= 3:
        N -= 3
        sum += 4
    else:
        sum += N
        break
print(sum)