from sys import stdin

n, m = [int(x) for x in stdin.readline().strip().split()]
dots = {}
for _ in range(n):
    x, y, t = [x for x in stdin.readline().strip().split()]
    dots[(int(x), int(y))] = t


for _ in range(m):
    theta_zero, theta_one, theta_two = [int(x) for x in stdin.readline().strip().split()]
    flag = True
    A_type_result = None
    B_type_result = None
    for dot, t in dots.items():
        x, y = dot
        result = theta_zero + theta_one * x + theta_two * y
        if t == 'A':
            if A_type_result is None:
                A_type_result = result
            if result * A_type_result < 0:
                flag = False
                break
        else:
            if B_type_result is None:
                B_type_result = result
            if result * B_type_result < 0:
                flag = False
                break
    if flag:
        print("Yes")
    else:
        print("No")

'''
9 3
1 1 A
1 0 A
1 -1 A
2 2 B
2 3 B
0 1 A
3 1 B
1 3 B
2 0 A
0 2 -3
-3 0 2
-3 1 1
'''