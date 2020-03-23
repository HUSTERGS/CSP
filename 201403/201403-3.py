# score 100
from sys import stdin
import re
config = stdin.readline().strip()
N = int(stdin.readline())
config_dict = {}
while len(config):
    string = re.findall("[a-z]:*", config)[0]
    if len(string) == 2:
        config_dict[string[0]] = 1
        config = config[2:]
    else:
        config_dict[string] = 0
        config = config[1:]

for i in range(N):
    command = stdin.readline().split()[1:]
    local_config_dict = {}
    index = 0
    if len(command) > 0:
        while index < len(command):
            arg = command[index]
            if not (re.match(f"-[a-z]", arg) is None):
                arg = arg[1]
                if arg in config_dict:
                    if config_dict[arg] == 0:
                        # 如果不需要参数
                        local_config_dict[arg] = None
                    else:
                        # 如果需要参数
                        index += 1
                        # 有可能此时没有下一个了
                        if index >= len(command):
                            break
                        local_config_dict[arg] = command[index]
                else:
                    break
            else:
                break
            index += 1
    result = [f"Case {i+1}:", ]
    for key in sorted(local_config_dict.keys()):
        value = local_config_dict[key]
        if value is None:
            result.append(f"-{key}")
        else:
            result.append(f"-{key} {value}")
    print(" ".join(result))