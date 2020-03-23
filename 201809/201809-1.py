# score 100
from sys import stdin
n = int(stdin.readline())
nums = [int(x) for x in stdin.readline().split()]
next_day = nums.copy()
next_day[0] = (nums[0] + nums[1]) // 2
next_day[n-1] = (nums[n-1] + nums[n-2]) // 2
for index in range(1, n-1):
    next_day[index] = (nums[index] + nums[index - 1] + nums[index + 1]) // 3
print(" ".join(str(x) for x in next_day))
