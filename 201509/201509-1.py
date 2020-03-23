# score 100
from sys import stdin
n = int(stdin.readline())
nums = tuple(int(x) for x in stdin.readline().split())
current = nums[0]
count = 1
for num in nums:
    if num != current:
        current = num
        count += 1
print(count)