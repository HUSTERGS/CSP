# score 20 超时
from sys import stdin
from heapq import nlargest
m, n = [int(x) for x in stdin.readline().strip().split()]

data = {t: {} for t in range(m)}

for _ in range(n):
    Id, score = [int(x) for x in stdin.readline().strip().split()]
    # 每一个类的对应的编号的分数
    for t in data.keys():
        data[t][Id] = score

# op num
for _ in range(int(stdin.readline().strip())):
    ops = stdin.readline().strip().split()
    if ops[0] == '1':
        # 增加编号
        t, commodity, score = [int(x) for x in ops[1:]]
        data[t][commodity] = score
    elif ops[0] == '2':
        t, commodity = [int(x) for x in ops[1:]]
        del data[t][commodity]
    elif ops[0] == '3':
        K = int(ops[1])
        Kn = tuple(int(x) for x in ops[2:])
        candidate = []
        # 对于每一类商品
        for t in data.keys():
            # 商品类型，商品编号，商品分数    三元组
            temp = [(t, Id, data[t][Id]) for Id in sorted(data[t].keys())]
            candidate.extend(nlargest(Kn[t], temp, key=lambda x: x[2]))
        # 由于在加入的时候已经针对编号进行了排序，并且排序是稳定的，加入的时候也是按照分类号从小到大排序的
        candidate = nlargest(K, candidate, key=lambda x: x[2])
        result = [[] for _ in range(m)]
        for item in candidate:
            result[item[0]].append(item[1])
        for item in result:
            if len(item) == 0:
                print(-1)
            else:
                print(" ".join(str(x) for x in item))