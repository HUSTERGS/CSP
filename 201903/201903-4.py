# score 80

from sys import stdin
# from collections import deque
T, n = [int(x) for x in stdin.readline().split()]

for i in range(T):
    processes = []
    success = True
    # 读取每一组数据
    for i in range(n):
        # processes.append(deque([x for x in stdin.readline().split()]))
        processes.append([x for x in stdin.readline().split()])
    while success:
        success = False
        for i in range(n):
            # 对于每一个进程
            if len(processes[i]):
                target = int(processes[i][0][1:])
                # 目标进程的序号
                if len(processes[target]) == 0:
                    # 如果目标进城已经是空的，那么必然是死锁，不用继续了
                    success = False
                    break
                if int(processes[target][0][1:]) == i:
                    if processes[i][0][0] != processes[target][0][0]:
                        del processes[i][0]
                        del processes[target][0]
                        success = True
                    else:
                        # 同样是死锁
                        success = False
                        break
    if sum([len(x) for x in processes]):
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


