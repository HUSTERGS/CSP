# score 100

from sys import stdin

r, y, g = [int(x) for x in stdin.readline().split()]
# 如果是绿灯 时间为0
# 如果是红灯， 时间为显示牌上的时间
# 如果是黄灯，时间为显示牌上的时间加上r
n = int(stdin.readline())

def deal_with(light_type, current_sum, t):
    current_sum %= r + g + y
    if light_type == 1:
        # 如果是红灯
        if current_sum < t:
            # 依然是红灯
            return t - current_sum
        elif g > current_sum - t >= 0:
            # 经过了红灯。停留在绿灯
            return 0
        elif y > current_sum - t - g >= 0:
            # 经过了红灯和绿灯，到达了黄灯
            return y - (current_sum - t - g) + r
        else:
            # 又回到了红灯
            return r - (current_sum - t - g - y)

    elif light_type == 2:
            # 如果是黄灯
        if current_sum < t:
            # 依然是黄灯
            return t - current_sum + r
        elif r > current_sum - t >= 0:
            # 经过了黄灯，到达了红灯
            return r - (current_sum - t)
        elif g > current_sum - t - r >= 0:
            # 经过了黄灯，和红灯，停留在绿灯
            return 0
        else:
            # 又回到黄灯
            return y - (current_sum - t - r -g) + r
    elif light_type == 3:
        # 如果是绿灯
        if current_sum < t:
            # 如果依然是绿灯
            return 0    
        elif y > current_sum -t >= 0:
            # 经过了绿灯，停留在黄灯
            return y - (current_sum - t) + r
        elif r > current_sum -t - y >= 0:
            # 经过了绿灯，黄灯。在红灯
            return r - (current_sum - t - y)
        else:
            # 回到了绿灯
            return 0



time_sum = 0
for i in range(n):
    k, t = [int(x) for x in stdin.readline().split()]
    if k == 0:
        # 如果是经过一段道路
        time_sum += t
    else:
        time_sum += deal_with(k, time_sum, t)



print(time_sum)


'''
测试用例
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