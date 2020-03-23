# score 100
from sys import stdin
n = int(stdin.readline())
nums = tuple(int(x) for x in stdin.readline().split())
for num in nums:
    if sum([x < num for x in nums]) == sum([x > num for x in nums]):
        print(num)
        exit(0)
print(-1)