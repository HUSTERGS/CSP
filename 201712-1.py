# score 100
from sys import stdin
n = int(stdin.readline())
nums = [int(x) for x in stdin.readline().split()]
nums.sort()
print(min([abs(nums[x] - nums[x+1]) for x in range(0, n-1)]))
