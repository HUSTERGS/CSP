# score 70
# 远古代码
import sys

num = int(sys.stdin.readline())
prices = [int(price) for price in sys.stdin.readline().split()]

result = []


def recursive(order, a_one, a_two):
    if order == num - 1:
        if (a_one + a_two) // 2 == prices[-1]:
            return True
        else:
            return False
    possible_one = 3 * prices[order] - a_one - a_two
    if possible_one > 0:
        if (recursive(order + 1, a_two, possible_one)):
            result.append(possible_one)
            return True
        else:
            pass
    if possible_one > -1:
        if (recursive(order + 1, a_two, possible_one + 1)):
            result.append(possible_one + 1)
            return True
        else:
            pass
    if possible_one > -2:
        if (recursive(order + 1, a_two, possible_one + 2)):
            result.append(possible_one + 2)
            return True
        else:
            pass
    return False


def start():
    for i in range(1, prices[0] * 2):
        a_two = prices[0] * 2 - i
        result.extend([i, a_two])
        if (i + a_two) // 2 == prices[0]:
            if recursive(1, i, a_two):
                return True
            else:
                result.pop()
                result.pop()
        elif (i + a_two + 1) // 2 == prices[0]:
            reuslt.extend([i, a_two + 1])
            if recursive(1, i, a_two + 1):
                return True
        else:
            continue


start()
a = result[0:2]
b = result[2:]
b.reverse()
a.extend(b)
print(' '.join([str(num) for num in a]))

