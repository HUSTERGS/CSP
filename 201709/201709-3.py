# score 100
from sys import stdin
import json

n, m = [int(x) for x in stdin.readline().split()]
string = ""
for _ in range(n):
    string += stdin.readline()
obj = json.loads(string)
for _ in range(m):
    s = stdin.readline().strip()
    if "." in s:
        key_list = s.split(".")
        try:
            value = obj.get(key_list[0])
            for key in key_list[1:]:
                value = value[key]
            if type(value) == str:
                print(f"STRING {value}")
            else:
                print("OBJECT")
        except:
            print("NOTEXIST")
    else:
        try:
            if type(obj.get(s)) == str:
                print(f"STRING {obj.get(s)}")
            elif obj.get(s) is None:
                print("NOTEXIST")
            else:
                print("OBJECT")
        except:
            print("NOTEXIST")
