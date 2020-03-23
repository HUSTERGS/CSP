# score 100
# 写的稀烂
from sys import stdin

a, b, c, y1, y2 = [int(x) for x in stdin.readline().strip().split()]

start_year = 1850
day_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(y):
    # 是否是闰年
    if y % 400 == 0:
        return True
    elif y % 4 == 0 and y % 100 != 0:
        return True
    else:
        return False


def leap_years(y):
    # 计算从1850年开始到第y年中，闰年的个数(不包括y)
    leap_count = 0
    for i in range(start_year, y):
        if is_leap(i):
            leap_count += 1
    return leap_count


def date_of_abc(a, b, c, y):
    # 计算某一年的
    # 第y年第a月第一天到start year 的天数
    # print(f"leap_year : {leap_years(y)}")
    day_count = (y - start_year) * sum(day_of_month) + leap_years(y) + sum(day_of_month[:a - 1])
    upper_bound = day_of_month[a - 1]
    # 根据当年是否是闰年以及要计算的月份和2月的关系(之后还是等于2)，对迭代的天数以及星期进行调整
    if is_leap(y):
        if a == 2:
            upper_bound += 1
        elif a > 2:
            day_count += 1
    # 这一天是星期几
    week = (day_count + 1) % 7

    for i in range(upper_bound):
        if week == c-1:
            if b == 1:
                return i + 1
            else:
                b -= 1
        week = (week + 1) % 7
    return None


for y in range(y1, y2 + 1):
    result = date_of_abc(a, b, c, y)
    if result is None:
        print("none")
    else:
        print("%04d/%02d/%02d" % (y, a, result))
