# score 90 超时
from sys import stdin
import re


def multi_dict(a, b):
    result = {}
    for key, item in a.items():
        result[key] = b * a[key]
    return result


def add_dict(a, b):
    result = a.copy()
    for key, value in b.items():
        if key in result:
            result[key] += b[key]
        else:
            result[key] = b[key]
    return result


def judge_one(formula):
    result = {}
    if len(formula) == 0:
        return result
    if '0' <= formula[0] <= '9':
        # 如果以数字开头
        times = re.findall(r"(\d+)", formula)[0]
        # 乘上倍数,然后分析剩余部分
        return multi_dict(judge_one(formula[len(times):]), int(times))
    if formula[0] == "(":
        count = 0
        index_of_next_bracket = 1
        while index_of_next_bracket < len(formula):
            if formula[index_of_next_bracket] == ")":
                if count == 0:
                    # 找到了对应的另外一个括号的index
                    if index_of_next_bracket < len(formula) - 1 and '0' <= formula[index_of_next_bracket + 1] <= '9':
                        # 如果括号后面有数字的话
                        times = re.findall(r"\d+", formula[index_of_next_bracket + 1:])[0]
                        return add_dict(multi_dict(judge_one(formula[1:index_of_next_bracket]), int(times)),
                                        judge_one(formula[index_of_next_bracket + len(times) + 1:]))
                    else:
                        # 如果括号后面没有数字
                        return add_dict(judge_one(formula[1:index_of_next_bracket]),
                                        judge_one(formula[index_of_next_bracket + 1:]))
                else:
                    count -= 1
            elif formula[index_of_next_bracket] == "(":
                count += 1
            index_of_next_bracket += 1

    # 最后的情况就是普通情况
    element = re.findall(r"[A-Z][a-z]*", formula)[0]
    if len(element) < len(formula) and '0' <= formula[len(element)] <= '9':
        # 如果元素后面是数字的话
        times = re.findall(r"\d+", formula[len(element):])[0]
        result[element] = int(times)
        return add_dict(judge_one(formula[len(element) + len(times):]), result)
    else:
        result[element] = 1
        return add_dict(judge_one(formula[len(element):]), result)


def equal(a, b):
    for key, value in a.items():
        if key not in b or value != b[key]:
            return False
    for key, value in b.items():
        if key not in a or value != a[key]:
            return False
    return True


n = int(stdin.readline())
for _ in range(n):
    left, right = [x for x in stdin.readline().strip().split("=")]
    left_dict = {}
    right_dict = {}
    for formula in [x.strip() for x in left.split("+")]:
        left_dict = add_dict(left_dict, judge_one(formula))
    for formula in [x.strip() for x in right.split("+")]:
        right_dict = add_dict(right_dict, judge_one(formula))
    if equal(left_dict, right_dict):
        print("Y")
    else:
        print("N")


"""
11
H2+O2=H2O
2H2+O2=2H2O
H2+Cl2=2NaCl
H2+Cl2=2HCl
CH4+2O2=CO2+2H2O
CaCl2+2AgNO3=Ca(NO3)2+2AgCl
3Ba(OH)2+2H3PO4=6H2O+Ba3(PO4)2
3Ba(OH)2+2H3PO4=Ba3(PO4)2+6H2O
4Zn+10HNO3=4Zn(NO3)2+NH4NO3+3H2O
4Au+8NaCN+2H2O+O2=4Na(Au(CN)2)+4NaOH
Cu+As=Cs+Au
"""