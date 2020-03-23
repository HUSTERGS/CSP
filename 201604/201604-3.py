# score 100
from sys import stdin
import re
P = int(stdin.readline())
current = stdin.readline().strip()
for _ in range(P):
    path = stdin.readline().strip()
    if len(path) == 0:
        print(current)
        continue
    if path.endswith("/") and len(path) > 1:
        path = path[:-1]
    if not path.startswith("/"):
        # 如果是相对路径
        path = current + "/" + path
    path = re.sub(r"/+", "/", path)
    path = path.split("/")
    while ".." in path:
        i = path.index("..")
        path.pop(i)
        if i == 1:
            continue
        else:
            path.pop(i-1)
    while "." in path:
        path.remove(".")
    path = "/".join(path)
    print(path)

