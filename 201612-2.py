# score 100
from sys import stdin


def salary(S):
    if S <= 3500:
        return S
    else:
        A = S - 3500
        if 0 < A <= 1500:
            return S - A * 0.03
        elif 1500 < A <= 4500:
            return S - 1500 * 0.03 - (A - 1500) * 0.1
        elif 4500 < A <= 9000:
            return S - 1500 * 0.03 - 3000 * 0.1 - (A - 4500) * 0.2
        elif 9000 < A <= 35000:
            return S - 1500 * 0.03 - 3000 * 0.1 - 4500 * 0.2 - (A - 9000) * 0.25
        elif 35000 < A <= 55000:
            return S - 1500 * 0.03 - 3000 * 0.1 - 4500 * 0.2 - 26000 * 0.25 - (A - 35000) * 0.3
        elif 55000 < A <= 80000:
            return S - 1500 * 0.03 - 3000 * 0.1 - 4500 * 0.2 - 26000 * 0.25 - 20000 * 0.3 - (A - 55000) * 0.35
        else:
            return S - 1500 * 0.03 - 3000 * 0.1 - 4500 * 0.2 - 26000 * 0.25 - 20000 * 0.3 - 25000 * 0.35 - (
                        A - 80000) * 0.45


T = int(stdin.readline())
for i in range(0, 1001):
    if salary(i * 100) == T:
        print(i * 100)
        break
