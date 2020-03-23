# score 100
from sys import stdin
p = int(stdin.readline())
privilege_dict = {}
for _ in range(p):
    pr = stdin.readline().strip()
    if ":" in pr:
        key, value = pr.split(":")
        privilege_dict[key] = int(value)
    else:
        privilege_dict[pr] = None
r = int(stdin.readline())
role_dict = {}
for _ in range(r):
    string = stdin.readline().strip().split()
    role = string[0]
    temp_dict = {}
    for i in range(int(string[1])):
        pr = string[2+i]
        if ":" in pr:
            key, value = pr.split(":")
            if key in temp_dict and int(value) > temp_dict[key]:
                temp_dict[key] = int(value)
            if key not in temp_dict:
                temp_dict[key] = int(value)
        else:
            temp_dict[pr] = None
    role_dict[role] = temp_dict
u = int(stdin.readline())
user_dict = {}
for _ in range(u):
    string = stdin.readline().strip().split()
    user = string[0]
    user_dict[user] = set(string[2:])

for user in user_dict.keys():
    temp_dict = {}
    for role in user_dict[user]:
        for key, value in role_dict[role].items():
            if value is not None:
                if key in temp_dict:
                    if temp_dict[key] < value:
                        temp_dict[key] = value
                else:
                    temp_dict[key] = value
            else:
                temp_dict[key] = value
    user_dict[user] = temp_dict


q = int(stdin.readline())
for _ in range(q):
    user, privilege = stdin.readline().strip().split()
    if user in user_dict:
        if ":" in privilege:
            # 带等级查询
            key, value = privilege.split(":")
            value = int(value)
            if (key not in privilege_dict) or (privilege_dict[key] < value):
                print("false")
                continue
            else:
                if key in user_dict[user]:
                    if user_dict[user][key] >= value:
                        print("true")
                        continue
                print("false")

        else:
            # 不带等级查询
            if privilege not in privilege_dict:
                print("false")
                continue
            else:
                if privilege in user_dict[user]:
                    if user_dict[user][privilege] is not None:
                        print(user_dict[user][privilege])
                    else:
                        print("true")
                else:
                    print("false")

    else:
        print("false")
