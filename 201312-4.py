# score 100
from sys import stdin
n = int(stdin.readline())
max_n = 1001
result = 0
matrix = [[1, ] * max_n for _ in range(max_n)]
for i in range(1, max_n):
    for j in range(1, max_n-i):
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]


for i in range(2, n-1):
    # i 为0,1篮子中数字的的个数， j为2,3篮子的个数
    j = n - i
    result += matrix[i][j-1] * (i-1) * (j-1)
    result %= 1000000007

print(result)

