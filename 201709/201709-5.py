# score 30
from sys import stdin
N, M = [int(x) for x in stdin.readline().strip().split()]
numbers = [int(x) for x in stdin.readline().strip().split()]


for _ in range(M):
    operation = [int(x) for x in stdin.readline().strip().split()]
    if operation[0] == 1:
        # 第一个操作
        l, r, v = operation[1:]
        for index in range(l-1, r):
            if numbers[index] % v == 0:
                numbers[index] //= v
    elif operation[0] == 2:
        # 第二种操作
        l, r = operation[1:]
        print(sum(numbers[l-1:r]))
