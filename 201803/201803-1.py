# score 100
from sys import stdin

nums = tuple(int(x) for x in stdin.readline().split())
is_first = True
last_score = 0
score = 0
for num in nums:
    if num == 1:
        score += 1
        last_score = 1
    elif num == 2:
        if is_first or (last_score == 1):
            score += 2
            last_score = 2
        else:
            last_score += 2
            score += last_score
    else:
        break
    is_first = False
print(score)
