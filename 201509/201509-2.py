# score 100
from sys import stdin

year = int(stdin.readline())
day = int(stdin.readline())
month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month2 = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    return False


current_month = None
if is_leap_year(year):
    current_month = month2
else:
    current_month = month
for index, count in enumerate(current_month):
    if day - count > 0:
        day = day - count
    else:
        print(index + 1)
        print(day)
        break
