# score 100
from sys import stdin

n = int(stdin.readline())
count = {}
nums = tuple(int(x) for x in stdin.readline().split())
for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

output = [[key, value] for key, value in count.items()]

output.sort(key=lambda x: x[0])
output.sort(key=lambda x: x[1], reverse=True)
for pair in output:
    print(pair[0], pair[1])