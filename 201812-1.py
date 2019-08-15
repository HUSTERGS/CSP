# score 100

from sys import stdin

r, y, g = [int(x) for x in stdin.readline().split()]
# 如果是绿灯 时间为0
# 如果是红灯， 时间为显示牌上的时间
# 如果是黄灯，时间为显示牌上的时间加上r
n = int(stdin.readline())
time_sum = 0
for i in range(n):
    k, t = [int(x) for x in stdin.readline().split()]
    if k == 0:
        # 如果是经过一段道路
        time_sum += t
    elif k == 1:
        # 如果是红灯:
        time_sum += t
    elif k == 2:
        # 如果是黄灯
        time_sum = time_sum + t + r
    else:
        continue

print(time_sum)

'''
测试用例1
30 3 30
8
0 10
1 5
0 11
2 2
0 6
0 3
3 10
0 3



'''