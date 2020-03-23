from sys import stdin

N, M = [int(x) for x in stdin.readline().split()]

data = []
for i in range(N):
    input_data = [int(x) for x in stdin.readline().split()]
    init = input_data[0]
    decrease = sum(input_data[1:])
    data.append((i, init + decrease, - decrease))

T = sum([x[1] for x in data])
temp = max([x for x in data], key=lambda x: x[2])
k = temp[0] + 1
P = temp[2]

print(T, k, P, sep=' ')
