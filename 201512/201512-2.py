# score 100
from sys import stdin

n, m = tuple(int(x) for x in stdin.readline().split())
matrix = [[int(x) for x in stdin.readline().split()] for _ in range(n)]
flags = [[0, ] * m for _ in range(n)]
for r in range(n):
    for c in range(m):
        current = matrix[r][c]
        if current == 0:
            continue
        # left
        left_start = -1
        right_end = -1
        up_start = -1
        down_end = -1
        horizon_clean = False
        vertical_clean = False

        x = c
        count = 0
        while x >= 0:
            if matrix[r][x] == current:
                count += 1
                x -= 1
                left_start = x+1
            else:
                break
        x = c + 1
        while x < m:
            if matrix[r][x] == current:
                count += 1
                x += 1
                right_end = x
            else:
                break
        if count >= 3:
            horizon_clean = True

        x = r
        count = 0
        while x >= 0:
            if matrix[x][c] == current:
                count += 1
                x -= 1
                up_start = x+1
            else:
                break
        x = r + 1
        while x < n:
            if matrix[x][c] == current:
                count += 1
                x += 1
                down_end = x
            else:
                break
        if count >= 3:
            vertical_clean = True

        if horizon_clean:
            for column in range(left_start, right_end):
                flags[r][column] = 1
        if vertical_clean:
            for row in range(up_start, down_end):
                flags[row][c] = 1

for r in range(n):
    for c in range(m):
        if flags[r][c] == 1:
            matrix[r][c] = 0

for r in range(n):
    print(" ".join([str(x) for x in matrix[r]]))
