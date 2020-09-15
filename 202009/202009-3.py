from sys import stdin
from copy import deepcopy
Q = int(stdin.readline().strip())

class component():
    def __init__(self, id):
        self.direct_input = set()
        self.component_input = set()
        self.depends_on_me = set()
        self.id = id
        self.func = None
        self.result = None


def compute_sequence(component_dict, N):
    seq = []
    seen_com = set()
    flag = False
    while True:
        for i in range(1, N+1):
            if i in seen_com:
                continue
            if len(component_dict[i].component_input) == 0:
                # 如果此时不依赖任何器件，那么加入列表
                flag = True
                seq.append(i)
                seen_com.add(i)
                for j in component_dict[i].depends_on_me:
                    if i in component_dict[j].component_input:
                        component_dict[j].component_input.discard(i)
        if not flag or len(seq) == N:
            break
    if len(seq) != N:
        return None
    return seq

def process(compute_seq, input_data, output_option, component_dict):
    for seq in compute_seq:
        com = component_dict[seq]
        calc_data = [input_data[x-1] for x in com.direct_input]
        for deps in com.component_input:
            calc_data.append(component_dict[deps].result)
        if com.func == "NOT":
            com.result = not calc_data[0]
        elif com.func == "AND":
            com.result = all(calc_data)
        elif com.func == "OR":
            com.result = any(calc_data)
        elif com.func == "XOR":
            com.result = eval(" ^ ".join([str(x) for x in calc_data]))
        elif com.func == "NAND":
            com.result = not all(calc_data)
        elif com.func == "NOR":
            com.result = not any(calc_data)

    return [component_dict[x].result for x in output_option]

for _ in range(Q):
    M, N = [int(x) for x in stdin.readline().strip().split()]
    component_data = {x : component(x) for x in range(1, N+1)}
    for i in range(N):
        FUNC, _, *L = stdin.readline().strip().split()
        com = component_data[i+1]
        com.func = FUNC
        for l in L:
            if l[0] == "O":
                com.component_input.add(int(l[1:]))
                # 在目标器件增加依赖项
                component_data[int(l[1:])].depends_on_me.add(i+1)
            else:
                com.direct_input.add(int(l[1:]))

    S = int(stdin.readline().strip())
    all_input_data = []
    all_output_requirement = []
    for _ in range(S):
        input_data = [x == '1' for x in stdin.readline().strip().split()]
        all_input_data.append(input_data)
    for _ in range(S):
        _, *component_indexes = [int(x) for x in stdin.readline().strip().split()]
        all_output_requirement.append(component_indexes)

    compute_seq = compute_sequence(deepcopy(component_data), N)
    if compute_seq is None:
        print("LOOP")
        continue

    for data, output in zip(all_input_data, all_output_requirement):
        r = process(compute_seq, data, output, component_data)
        print(" ".join([str(int(x)) for x in r]))







