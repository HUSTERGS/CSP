# score 90
from sys import stdin

n, m = [int(x) for x in stdin.readline().strip().split()]

current_path = []

data = {}


def indent(string):
    l = 0
    for c in string:
        if c == ".":
            l += 1
        else:
            break
    if " " in string:
        string = f"{string.split()[0].lower()} {string.split()[1]}"
    return l // 2, string[l:]


for index in range(1, n + 1):
    line = stdin.readline().strip()
    l, s = indent(line)
    if l == len(current_path):
        current_path.append(s)
        data[index] = current_path.copy()
    else:
        current_path = current_path[0:l]
        current_path.append(s)
        data[index] = current_path.copy()


def contain(element, selector):
    if selector.startswith("#"):
        for index, value in enumerate(element):
            if value.split(" ")[-1] == selector:
                return index
    else:
        selector = selector.lower()
        for index, value in enumerate(element):
            if value.split(" ")[0] == selector:
                return index
    return -1


for _ in range(m):
    selector = stdin.readline().strip().split()
    selector.reverse()
    result = []
    for index in range(1, n + 1):
        element = data[index].copy()
        element.reverse()
        flag = True
        if contain(element[0:1], selector[0]) == -1:
            continue
        for sub in selector:
            if len(element) == 0:
                flag = False
                break
            i = contain(element, sub)
            if i != -1:
                element = element[i+1:]
            else:
                flag = False
                break
        if flag:
            result.append(index)
    print(len(result), end=" ")
    print(" ".join(str(x) for x in result))
