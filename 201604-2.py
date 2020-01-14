# score 100
from sys import stdin
matrix = [[int(x) for x in stdin.readline().split()] for _ in range(15)]
block = [[int(x) for x in stdin.readline().split()] for _ in range(4)]
start_column = int(stdin.readline())

# 先找到要插入图案最靠下面的方块
block_set = set()
for r in range(4):
    for c in range(4):
        if block[r][c] == 1:
            block_set.add((r, c))

inner_start = min(x[1] for x in block_set)
inner_end = max(x[1] for x in block_set)

for down_count in range(19):
    # 最多下降19次,每次计算下降之前的坐标,如果在其下面没有
    row_bias = down_count - 4
    column_bias = start_column - 1
    blocked = False
    for pair in block_set:
        # 计算下面是否有方块
        r, c = pair
        test_r = r + row_bias + 1
        test_c = c + column_bias
        if test_r == 15:
            blocked = True
            break
        if 0 <= test_r <= 14 and 0 <= test_c <= 9 and matrix[test_r][test_c] == 1:
            blocked = True
            break
    if blocked:
        for pair in block_set:
            r, c = pair
            test_r = r + row_bias
            test_c = c + column_bias
            if 0 <= test_r <= 14 and 0 <= test_c <= 9:
                matrix[test_r][test_c] = 1
        for row in matrix:
            print(" ".join(str(x) for x in row))
        break
