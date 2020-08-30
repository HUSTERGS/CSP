from sys import stdin
import re
n = int(stdin.readline().strip())
S = stdin.readline().strip()
s = '1'
transition_dict = {'1': '2', '2': '4', '4': '16', '6': '64'}
for _ in range(n):
    s = ''.join(transition_dict[c] for c in s)

print(len(re.findall(S, s)) % 99824453)
