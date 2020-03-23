# score 100
from sys import stdin
n = int(stdin.readline())
nums = tuple(int(x) for x in stdin.readline().split())
print(max(abs(nums[index] - nums[index-1]) for index in range(1, n)))