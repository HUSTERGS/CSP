# score 80

# 记一个ip地址前面不为0的部分的长度为L
# len 的合法取值范围为32 >= len >= L
# 匹配集 前面len的长度都是一样的，后面随意

from sys import stdin
from functools import cmp_to_key

n = int(stdin.readline())


# n = 2
def is_legal(ip_string: str):
    pref, length = ip_string.split('/')
    if int(length) > 32 or int(length) < 0:
        return False
    test = ''.join(['0' * (8 - len(bin(int(x))[2:])) + bin(int(x))[2:] for x in pref.split('.')])
    if sum([int(x) for x in test[int(length):].split()]) == 0:
        return True
    else:
        return False


def regulizeIP(ip_string: str):
    if '/' in ip_string:
        # 标准型或者省略后缀型
        pref, length = ip_string.split('/')
        return pref + '.0' * (4 - len(pref.split('.'))) + '/' + length
        # if len(pref.split('.') == 4):
        #     # 标准型
        #     return ip_string
        # else:
        #     # 省略后缀型
        #     return pref + '.0' * (4 - len(pref.split('.'))) + '/' + length
    else:
        # 省略长度型
        length = len(ip_string.split('.'))
        return regulizeIP(ip_string + '/' + str(8 * length))


def compare_func(str1: str, str2: str):
    pref1, len1 = str1.split('/')
    pref2, len2 = str2.split('/')
    if pref1 == pref2:
        if int(len1) > int(len2):
            return 1
        elif len1 == len2:
            return 0
        else:
            return -1
    else:
        test1 = [int(x) for x in pref1.split('.')]
        test2 = [int(x) for x in pref2.split('.')]
        # print('test1 = ', test1, ', test2 = ', test2)
        if test1 > test2:
            # print('test1 > test2')
            return 1
        else:
            # print('test1 < test2')
            return -1


def is_subset(a, b):
    pref1, len1 = a.split('/')
    pref2, len2 = b.split('/')

    if int(len1) > int(len2):
        return False
    else:
        test1 = ''.join(['0' * (8 - len(bin(int(x))[2:])) + bin(int(x))[2:] for x in pref1.split('.')])
        test2 = ''.join(['0' * (8 - len(bin(int(x))[2:])) + bin(int(x))[2:] for x in pref2.split('.')])
        if test1[:int(len1)] == test2[:int(len1)]:
            return True
        else:
            return False


'''Step1'''
ip_list = sorted([regulizeIP(stdin.readline().strip()) for _ in range(n)], key=cmp_to_key(compare_func))
# ip_list = ['0.0.0.0/1', '128.0.0.0/1']


# def convert(ipAdr):
#     print(['0' * (8 - len(bin(int(x))[2:])) + bin(int(x))[2:] for x in ipAdr.split('.')])


'''Step2'''
i = 0
while True:
    try:
        if is_subset(ip_list[i], ip_list[i + 1]):
            del ip_list[i + 1]
        else:
            i += 1
    except:
        break

'''Step3'''


def step3_func(a, b):
    pref1, len1 = a.split('/')
    pref2, len2 = b.split('/')

    if len1 == len2:
        a_plus = pref1 + '/' + str(int(len1) - 1)
        if is_legal(a_plus):
            test1 = ''.join(['0' * (8 - len(bin(int(x))[2:])) + bin(int(x))[2:] for x in pref1.split('.')])
            test2 = ''.join(['0' * (8 - len(bin(int(x))[2:])) + bin(int(x))[2:] for x in pref2.split('.')])
            max1 = int(test1[:int(len1)] + '1' * (32 - int(len1)), 2)
            min1 = int(test1, 2)
            max2 = int(test2[:int(len2)] + '1' * (32 - int(len2)), 2)
            min2 = int(test2, 2)
            new_max = int(test1[:int(len1) - 1] + '1' * (33 - int(len1)), 2)
            new_min = int(test2[:int(len1) - 1] + '0' * (33 - int(len1)), 2)
            if min1 > max2 + 1 or min2 > max1 + 1:
                return False
            else:
                if max(max1, max2) == new_max and min(min1, min2) == new_min:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False


i = 0
while True:
    # print("进入", i)
    try:
        if (step3_func(ip_list[i], ip_list[i + 1])):
            pref, length = ip_list[i].split('/')
            a_plus = pref + '/' + str(int(length) - 1)
            ip_list[i] = a_plus
            del ip_list[i + 1]
            if i > 0:
                i -= 1
            # print("成功")
        else:
            # print("失败")
            i += 1
    except:
        break

for item in ip_list:
    print(item)

# test function regulizeIP

# test_list = ['101.6.6/23', '101/8', '1/32', '101.6.6.0', '101.6', '1']
# for i in test_list:
#     print(regulizeIP(i))
