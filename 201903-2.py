# score 100
import sys

input_count = int(sys.stdin.readline())

# 将 x 变为 乘号 *， 将除法 / 变为 整除 // 

for i in range(input_count):
    if eval(sys.stdin.readline().replace('x', '*').replace('/', '//')) == 24:
        print("Yes")
    else:
        print("No")