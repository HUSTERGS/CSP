from sys import stdin
n, k, t, x_l, y_d, x_r, y_u = [int(x) for x in stdin.readline().strip().split()]

def within(x, y):
    return x_l <= x <= x_r and y_d <= y <= y_u

def judge_one(seq):
    current_max = float('-inf')
    current = 0
    is_in = False
    for yes in seq:
        if yes:
            is_in = True
            current += 1
        else:
            if current > current_max:
                current_max = current
            current = 0
    if current > current_max:
        current_max = current
    return current_max >= k, is_in

stay_count = 0
is_in_count = 0

for _ in range(n):
    data = [int(x) for x in stdin.readline().strip().split()]
    data = [(data[2 * i], data[2 * i + 1]) for i in range(t)]
    data = [within(x[0], x[1]) for x in data]
    stay, is_in = judge_one(data)
    stay_count += stay
    is_in_count += is_in

def within(x, y):
    return x_l <= x <= x_r and y_d <= y <= y_u

print(is_in_count)
print(stay_count)