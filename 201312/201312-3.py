# score 100
"""
每次添加一个矩形，那么最大值必定为以下两者之一
1. 之前的最大值
2. 添加的最右边的矩形之后从该矩形开始向左延伸的最大矩形
其中2的计算中需要计算最小值，可以不用调用min函数，从而减少时间复杂度
"""

from sys import stdin

n = int(stdin.readline())
nums = tuple(int(x) for x in stdin.readline().split())
queue = []
max_rect = nums[0]


def find_max():
    length = len(queue)
    index = length - 1
    max_value = queue[-1]
    min_one = queue[-1]
    while index >= 0:
        if queue[index] < min_one:
            min_one = queue[index]
        temp_value = min_one * (length - index)
        if temp_value > max_value:
            max_value = temp_value
        index -= 1
    return max_value


i = 0
while i < len(nums):
    next_num = nums[i]
    queue.insert(len(queue), next_num)

    temp = find_max()
    if temp > max_rect:
        max_rect = temp
    i += 1
print(max_rect)