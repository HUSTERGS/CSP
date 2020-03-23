# score 100
from sys import stdin
n, k = [int(x) for x in stdin.readline().split()]
nums = tuple(int(x) for x in stdin.readline().split())
sum = 0
count = 0
for num in nums:
    sum += num
    if sum >= k:
        count += 1
        sum = 0
if sum != 0:
    print(count + 1)
else:
    print(count)