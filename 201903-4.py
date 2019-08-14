from sys import stdin
from collections import deque

T, n = stdin.readline().split()
T = int(T)
n = int(n)
processes = {}
for count in range(T):
    for i in range(n):
        processes[i] = deque([(x[0], int(x[1])) for x in stdin.readline().split()])
        # processes[i].reverse()
    # print('processes: ', processes)
    flag = 1
    deadlock = 0
    while flag and not deadlock:
        flag = 0
        for i in range(n):
            # 遍历每一个进程的指令列表
            # print(processes, end='\n\n\n')
            if len(processes[i]):
                # 第i个进程的指令列表如果不是空的
                # 找到第一个指令的指令类型以及目标
                processType, target = processes[i][0]
                if not len(processes[target]):
                    # 如果对方的列表已经空了，说明已经产生了死锁
                    deadlock = 1
                    break
                else:
                    if processType == 'R' and processes[target][0][0] == 'S' and processes[target][0][1] == i:
                        # 如果目标进程也匹配的话，就pop
                        processes[i].popleft()
                        processes[target].popleft()
                        flag = 1
                    elif processType == 'S' and processes[target][0][0] == 'R' and processes[target][0][1] == i:
                        # 如果目标进程也匹配的话，就pop
                        processes[i].popleft()
                        processes[target].popleft()
                        flag = 1
    # 此时已经没有更多的指令可以消去或者发现了死锁
    if deadlock:
        print(1)
        continue
    if sum([len(x) for x in processes.values()]):
        print(1)
    else:
        print(0)


'''
样例１
3 2
R1 S1
S0 R0
R1 S1
R0 S0
R1 R1 R1 R1 S1 S1 S1 S1
S0 S0 S0 S0 R0 R0 R0 R0

样例２
2 3
R1 S1
R2 S0 R0 S2
S1 R1
R1
R2 S0 R0
S1 R1

'''


