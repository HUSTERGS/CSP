# score 100
from sys import stdin
n, L, t = [int(x) for x in stdin.readline().split()]
ball_positions = [int(x) for x in stdin.readline().split()]
ball_direction = [1 for _ in range(n)]

for index, position in enumerate(ball_positions):
    if position == L:
        ball_direction[index] = -1

for _ in range(t):
    for index, position in enumerate(ball_positions):
        ball_positions[index] = position + ball_direction[index]

        if ball_positions[index] == L or ball_positions[index] == 0:
            ball_direction[index] = -ball_direction[index]
    for index in range(n):
        for sub_index in range(index, n):
            if ball_positions[index] == ball_positions[sub_index] and ball_direction[index] == -ball_direction[sub_index] and sub_index != index:
                ball_direction[index] = -ball_direction[index]
                ball_direction[sub_index] = -ball_direction[sub_index]

print(" ".join(str(x) for x in ball_positions))