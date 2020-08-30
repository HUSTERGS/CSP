# score 100
from sys import stdin
import re
n, m = [int(x) for x in stdin.readline().split()]
url_dict = []
for _ in range(n):
    line = stdin.readline().strip().split()
    url_dict.append((line[0], line[1]))


def match(url, target):
    # url是否匹配target
    params = []
    target = target.split("/")
    url = url.split("/")
    if len(url) != len(target) and url[-1] != "<path>":
        return None
    if len(url) > len(target):
        return None
    else:
        for i in range(len(url)):
            if url[i] == target[i]:
                continue
            else:
                if url[i] == "<int>":
                    if re.match(r"[0-9]+", target[i]):
                        value = int(target[i])
                        params.append(str(value))
                    else:
                        return None
                elif url[i] == "<str>":
                    if re.match(r"[a-zA-Z0-9_\-.]+", target[i]):
                        params.append(target[i])
                    else:
                        return None
                elif url[i] == "<path>":
                    if re.match(r"[a-zA-Z0-9_\-./]+", "/".join(target[i:])):
                        params.append("/".join(target[i:]))
                        return params
                    return None
                else:
                    return None
        return params


for _ in range(m):
    url = stdin.readline().strip()
    find = False
    for key, value in url_dict:
        result = match(key, url)
        if result is not None:
            find = True
            print(f"{value} {' '.join(result)}")
            break
    if find:
        continue
    else:
        print(404)
