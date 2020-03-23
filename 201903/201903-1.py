# score 100

import sys

# 数字的个数
number_count = int(sys.stdin.readline())

# 数字
numbers = [int(x) for x in sys.stdin.readline().split()]
# 最大值
max_number = max(numbers)
# 最小值
min_number = min(numbers)

# 可能是中位数的两个数
sum_two = numbers[number_count // 2] + numbers[(number_count - 1) // 2]


x, y = divmod(sum_two, 2)
if y:
    mid_number = x + 0.5
else:
    mid_number = x

print(max_number, mid_number, min_number, sep=' ')