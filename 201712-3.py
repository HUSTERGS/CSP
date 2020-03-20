from sys import stdin

n, s, t = stdin.readline().strip().split()
n = int(n)
crontab = []
day_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
start_year = 1970

week_name = {
    "Sun": 0,
    "Mon": 1,
    "Tue": 2,
    "Wed": 3,
    "Thu": 4,
    "Fri": 5,
    "Sat": 6
}

month_name = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

for _ in range(n):
    # 按照元组方式存入时间和对应的指令
    config = stdin.readline().strip().split()
    crontab.append((config[0:-1], config[-1]))


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


def week_day(year, month, day):
    # 根据你年月日得到当前的星期
    day_count = (year - start_year) * sum(day_of_month) + leap_years(year) + sum(day_of_month[:month - 1]) + day
    if is_leap(year) and month > 2:
        # 如果是闰年并且是二月份之后
        day_count += 1
    return (day_count + 3) % 7


def reg_month(string):
    result = []
    for item in string.split(","):
        if "-" in item:
            start, end = item.split("-")
            if start.isalpha():
                start = month_name[start]
            else:
                start = int(start)

            if end.isapha():
                end = month_name[end]
            else:
                end = int(end)
            result.extend(list(range(start, end + 1)))
        elif item == "*":
            result = list(range(1, 13))
        else:
            if item.isalpha():
                item = month_name[item]
            else:
                item = int(item)
            result.append(item)
    return result


def reg_week(string):
    result = []
    for item in string.split(","):
        if "-" in item:
            start, end = item.split("-")
            if start.isalpha():
                start = week_name[start]
            else:
                start = int(start)

            if end.isalpha():
                end = week_name[end]
            else:
                end = int(end)
            result.extend(list(range(start, end + 1)))
        elif item == "*":
            result = list(range(0, 7))
        else:
            if item.isalpha():
                item = week_name[item]
            else:
                item = int(item)
            result.append(item)
    return result


def in_range(t, r):
    for item in r.split(","):
        if "-" in item:
            start, end = [int(x) for x in item.split("-")]
            if start <= t <= end:
                return True
        elif item == "*":
            return True
        elif int(item) == t:
            return True
    return False


def time_in_config(time, config):
    # 检查给定的time是否在config所涵盖的范围之内
    year, month, day, hour, minutes = [int(t) for t in (time[0:4], time[4:6], time[6:8], time[8:10], time[10:])]
    min, h, day_month, m, day_of_week = config
    if not month in reg_month(m):
        return False
    if not week_day(year, month, day) in reg_week(day_of_week):
        return False
    if not in_range(minutes, min):
        return False
    if not in_range(hour, h):
        return False
    return True


def next_time(time):
    year, month, day, hour, minutes = [int(t) for t in (time[0:4], time[4:6], time[6:8], time[8:10], time[10:])]
    minutes += 1
    if minutes == 60:
        minutes = 0
        hour += 1
    if hour == 24:
        hour = 0
        day += 1
    upper_bound = day_of_month[month - 1]
    if is_leap(year) and month == 2:
        upper_bound += 1
    if day == upper_bound + 1:
        day = 1
        month += 1
    if month == 13:
        month = 1
        year += 1
    return "%04d%02d%02d%02d%02d" % (year, month, day, hour, minutes)


while s != t:
    for config, command in crontab:
        if time_in_config(s, config):
            print(f"{s} {command}")
    s = next_time(s)
    # print(s)
