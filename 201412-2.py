# score 100
from sys import stdin

#  将正方形倾斜
n = int(stdin.readline())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in stdin.readline().split()])

result = []


def tri_to_square(hight, left):
    # 三角形到正方形坐标, hight 从0开始,一直到2n - 2, 返回row和column
    if hight >= n:
        if left:
            return n - 1, hight - n + 1
        else:
            return hight - n + 1, n - 1
    else:
        if left:
            return hight, 0
        else:
            return 0, hight

is_left = True  # 是否是从左边开始
for hight in range(2 * n - 1):
    r, c = tri_to_square(hight, is_left)
    if hight >= n:
        for _ in range(2 * n - 1 - hight):
            result.append(matrix[r][c])
            if is_left:
                r -= 1
                c += 1
            else:
                r += 1
                c -= 1
    else:
        for _ in range(hight + 1):
            result.append(matrix[r][c])
            if is_left:
                r -= 1
                c += 1
            else:
                r += 1
                c -= 1
    is_left = not is_left
    # print(is_left)

print(" ".join(str(x) for x in result))