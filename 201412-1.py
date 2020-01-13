# score 100
from sys import stdin
visitDict = {}
n = int(stdin.readline())
nums = tuple(int(x) for x in stdin.readline().split())
result = []
for num in nums:
    if num in visitDict:
        visitDict[num] += 1
    else:
        visitDict[num] = 1
    result.append(str(visitDict[num]))
print(" ".join(result))