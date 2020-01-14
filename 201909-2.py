from sys import stdin

N = int(stdin.readline())
final_data = []


def process(data):
    apple_tree = {"init": data[0], "later": data[1:], "current": data[0], "drop": False}
    for temp in apple_tree["later"]:
        if temp > 0:
            if temp < apple_tree["current"]:
                apple_tree["drop"] = True
                apple_tree["current"] = temp
        else:
            apple_tree["current"] += temp
            # 如果是去掉了
    final_data.append(apple_tree)


for i in range(N):
    # every tree
    data = [int(x) for x in stdin.readline().split()]
    process(data[1:])

T = sum([x["current"] for x in final_data])
D = sum(x["drop"] for x in final_data)

drop_list = [x["drop"] for x in final_data]
# 计算相邻情况
E = 0
for x in range(N):
    if x == N - 1:
        if drop_list[N - 2] + drop_list[N - 1] + drop_list[0] == 3:
            E += 1
        break
    if drop_list[x - 1] + drop_list[x] + drop_list[x + 1] == 3:
        E += 1
print(T, D, E, sep=' ')
