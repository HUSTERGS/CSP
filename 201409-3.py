# score 100
from sys import stdin
target = stdin.readline().strip()
case_sensitive = stdin.readline().strip() == '1'
n = int(stdin.readline())

if case_sensitive:
    for _ in range(n):
        string = stdin.readline().strip()
        if target in string:
            print(string)
else:
    for _ in range(n):
        string = stdin.readline().strip()
        if target.lower() in string.lower():
            print(string)