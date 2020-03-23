# score 100
from sys import stdin

N, K = [int(x) for x in stdin.readline().split()]
data = []
for _ in range(K):
    # 钥匙编号，开始上课时间。开始上课的时长
    data.append(tuple(int(x) for x in stdin.readline().split()))

keys = [x for x in range(1, N + 1)]
# 还钥匙的时间
# 先按照钥匙编号排一次序
return_time = sorted(data, key=lambda x: x[0])
return_time.sort(key=lambda x: x[1] + x[2])
# 拿到钥匙的时间
get_time = sorted(data, key=lambda x: x[1])


def find_empty():
    for i in range(N):
        if keys[i] == 0:
            return i


while len(return_time) and len(get_time):
    r_time = return_time[0][1] + return_time[0][2]
    g_time = get_time[0][1]
    if r_time <= g_time:
        key = return_time[0][0]
        # 如果还钥匙的时间要更早
        keys[find_empty()] = key
        return_time.pop(0)
    else:
        key = get_time[0][0]
        index = keys.index(key)
        keys[index] = 0
        get_time.pop(0)

for pair in return_time:
    w, s, c = pair
    keys[find_empty()] = w

print(" ".join(str(x) for x in keys))

