# score 100
from sys import stdin
import sys
sys.setrecursionlimit(100000)
n, m = [int(x) for x in stdin.readline().strip().split()]

connections = {x: set() for x in range(1, m + 1)}

for _ in range(m):
    a, b = [int(x) for x in stdin.readline().strip().split()]
    connections[a].add(b)


class SetStack():
    def __init__(self):
        self.set = set()
        self.stack = []
        self.current_dnf = 1

    def contain(self, item):
        return item in self.set

    def pop(self):
        self.set.remove(self.stack[-1])
        return self.stack.pop()

    def push(self, item):
        self.current_dnf += 1
        self.set.add(item)
        self.stack.append(item)


set_stack = SetStack()
visited = set()
LOW = {}
DFN = {}
strong_connected_component = []


def tarjan(u):
    # 从u点开始tarjan算法
    DFN[u] = set_stack.current_dnf
    LOW[u] = set_stack.current_dnf
    visited.add(u)
    set_stack.push(u)

    for v in connections[u]:
        if v in visited and set_stack.contain(v):
            # 如果之前访问过并且还在栈中,就进行更新,否则不进行处理
            LOW[u] = min(LOW[u], DFN[v])
        if v not in visited:
            LOW[u] = min(LOW[u], tarjan(v))

    if DFN[u] == LOW[u]:
        # 如果当前的DFN和LOW相等,那么就开始从栈中不断pop,直到遇到其本身,期间的所有点属于同一个联通分量
        result = []
        while True:
            result.append(set_stack.pop())
            if result[-1] == u:
                strong_connected_component.append(result)
                break
    return LOW[u]


for i in range(1, n + 1):
    if i not in visited:
        tarjan(i)

def calc_pair(n):
    return n * (n-1) // 2


print(sum([calc_pair(len(x)) for x in strong_connected_component]))
