# score 100
from sys import stdin

n = int(stdin.readline())
count = {}
nums = [int(x) for x in stdin.readline().split()]
for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

maxKey = 0
maxValue = 0
for key, value in count.items():
    if value == maxValue and key < maxKey:
        maxKey = key
    elif value > maxValue:
        maxKey = key
        maxValue = value

print(maxKey)