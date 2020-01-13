# score 100
from sys import stdin
n = int(stdin.readline())
nums = (int(x) for x in stdin.readline().split())
numSet = set()
count = 0
for num in nums:
    numSet.add(num)
    if -num in numSet:
        count += 1
print(count)