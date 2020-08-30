from sys import stdin

m, l, r = [int(x) for x in stdin.readline().strip().split()]
km = [int(x) for x in stdin.readline().strip().split()]
an = [1, ]
Q = 998244353
Matrix = None

for i in range(m - 1):
    # 至少填充m-1个
    s = 0
    for t in range(min(i+1, m)):
        s += km[t] * an[i - t] % Q
    s %= Q
    an.append(s)
# 如果已经求出来的m个元素就已经包含了所有所需的值，则直接输出
if m > r:
    for i in range(l, r + 1):
        print(an[i])
    exit(0)

# 创建矩阵
Matrix = tuple((tuple(km), *tuple(tuple([0, ] * i + [1, ] + [0, ] * (m - 1 - i)) for i in range(m - 1))))


# 矩阵乘法
def mul(a, b):
    m, n = len(a), len(b)
    result = [[0, ] * len(b[0]) for _ in range(m)]
    for i in range(m):
        for j in range(len(b[0])):
            for q in range(n):
                result[i][j] += a[i][q] * b[q][j]
                result[i][j] %= Q
    return result


def matpow(A, n):
    # B为单位矩阵
    B = [[0, ] * len(A) for _ in range(len(A))]
    for i in range(len(A)):
        B[i][i] = 1
    while n > 0:
        if n & 1:
            B = mul(B, A)
        A = mul(A, A)
        n = n >> 1
    return B


base_mat = [[ai] for ai in reversed((an))]

result = []
count = l
while True:
    temp = mul(matpow(Matrix, count), base_mat)
    result.extend([x[0] for x in reversed(temp)])
    count += m
    if count > r:
        break


for i in range(r - l + 1):
    print(result[i])