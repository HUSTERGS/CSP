from sys import stdin

X_win = 1
O_win = 2


def print_matrix(m):
    for i in range(3):
        for j in range(3):
            print(m[i][j], " ", end="")
        print()
    print()


def copy(m):
    return [m[x][:] for x in range(3)]


class Grid:
    EMPTY = 0
    PUT_X = 1
    PUT_O = 2

    def __init__(self, matrix):
        self.matrix = matrix
        self.children = None
        self.value = None
        self.winner = None


# T = int(stdin.readline().strip())
root_matrix = [[0, ] * 3 for _ in range(3)]
root_node = Grid(root_matrix)


def winner(matrix):
    # 判断是否有赢家
    # 检查每一行
    return 0



def evaluate(matrix):
    # 评估棋局
    result = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                result += 1
    return result + 1


def construct_init_tree(node: Grid, is_o):
    # print_matrix(node.matrix)
    w = winner(node.matrix, is_o)
    if w != 0:
        # 如果已经有赢家
        node.winner = w
        if w == X_win:
            node.value = evaluate(node.matrix)
        else:
            node.value = -evaluate(node.matrix)
        return
    # 如果没有赢家
    is_full = True
    node.children = []
    for i in range(3):
        for j in range(3):
            if node.matrix[i][j] == 0:
                is_full = False
                new_matrix = copy(node.matrix)
                new_matrix[i][j] = is_o + 1  # 下子
                new_node = Grid(new_matrix)
                node.children.append(new_node)
                construct_init_tree(new_node, not is_o)

    if is_full:
        # 如果已经满了，那么当前棋局为平局
        node.value = 0


construct_init_tree(root_node, False)
