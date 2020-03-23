# score 100
from sys import stdin
import re
m, n = [int(x) for x in stdin.readline().split()]
content = ""
var_dict = {}
for _ in range(m):
    content += stdin.readline()
for _ in range(n):
    string = stdin.readline().strip().split()
    var_dict[string[0]] = " ".join(string[1:])[1:-1]

record = set(re.findall(r"{{ (.+?) }}", content))
for name in record:
    if name in var_dict:
        content = content.replace(f"{{{{ {name} }}}}", var_dict[name])
    else:
        content = content.replace(f"{{{{ {name} }}}}", "")
print(content)