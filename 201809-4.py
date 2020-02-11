from sys import stdin
n = int(stdin.readline().strip())
nums = tuple(int(x) for x in stdin.readline().strip().split())
origin = [1, ] * n
depth = 0
index = 0
