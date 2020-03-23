# score 100
from sys import stdin

n, k = [int(x) for x in stdin.readline().split()]
kids = [x for x in range(1, n + 1)]


def contain(num):
    return num % k == 0 or num % 10 == k


current_num = 1
current_index = 0
while len(kids) > 1:
    if contain(current_num):
        kids.pop(current_index)
    else:
        current_index += 1
    current_index %= len(kids)
    current_num += 1
print(kids[0])
