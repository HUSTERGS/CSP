# score 100
from sys import stdin
n = int(stdin.readline())
nums = set(int(x) for x in stdin.readline().split())
count = 0
for num in nums:
    if num-1 in nums:
        count += 1
    if num+1 in nums:
        count += 1
print(count // 2)
