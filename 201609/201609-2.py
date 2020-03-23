# score 100
from sys import stdin

n = int(stdin.readline())
nums = tuple(int(x) for x in stdin.readline().split())
empty = [1, ] * 100


def find_available(total):
    for i in [x * 5 for x in range(20)]:
        for start in range(i, i + 6 - total):
            if sum([empty[j] for j in range(start, total + start)]) == total:
                return start
    return -1


def patch(total):
    count = 0
    result = []
    for i in range(100):
        if empty[i] == 1:
            empty[i] = 0
            result.append(i + 1)
            count += 1
            if count == total:
                break
    print(" ".join(str(x) for x in result))


for num in nums:
    index = find_available(num)
    result = []
    if index == -1:
        patch(num)
    else:
        for i in range(index, index + num):
            empty[i] = 0
            result.append(i+1)
        print(" ".join(str(x) for x in result))
