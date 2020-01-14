# score 100
from sys import stdin
n = int(stdin.readline())
nums = tuple(int(x) for x in stdin.readline().split())
count = 0
for i in range(1, len(nums) - 1):
    if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        count += 1
    if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
        count += 1

print(count)