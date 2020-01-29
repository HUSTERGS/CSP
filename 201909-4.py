# score 20 超时
from sys import stdin
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
            # 先按照编号进行排序
            # temp.sort(key=lambda x: x[1])
            # 再按照分数进行排序
            temp.sort(key=lambda x: x[2], reverse=True)
            # 如果大于商品数量，则全部加入
            if Kn[t] >= len(data[t].keys()):
                candidate.extend(temp)
            else:
                candidate.extend(temp[:Kn[t]])
        # 由于在加入的时候已经针对编号进行了排序，并且排序是稳定的，加入的时候也是按照分类号从小到大排序的

        if K < len(candidate):
            candidate.sort(key=lambda x: x[2], reverse=True)
            candidate = candidate[:K]
        for t in range(m):
            temp = [x[1] for x in candidate if x[0] == t]
            if len(temp) == 0:
                print(-1)
            else:
                print(" ".join(str(x) for x in temp))


'''
2 3
1 3
2 2
3 1
8
3 100 1 1
1 0 4 3
1 0 5 1
3 10 2 2
3 10 1 1
2 0 1
3 2 1 1
3 1 1 1

'''