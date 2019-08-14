import sys

def convert(q, s, n):
    # global s,n
    x, y = divmod(q, s)
    # x 商， y 余数
    # s 是条带大小
    # x 是 q 所在第几个条带
    # y 是 所在条带的第几个块
    drive_number = x % n # 硬盘序号
    addition = x // (n - 1) * s# 需要额外增加的块的个数
    return (drive_number, addition + y)

def str2int(s):
    return list(map(lambda x : eval('0x' + x),  [s[0:2], s[2:4], s[4:6], s[6:8]]))


n, s, l = [int(x) for x in sys.stdin.readline().split()]

hard_drive = []

able_recover = (l >= n-1)

for i in range(l):
    index, content = sys.stdin.readline().split()
    index = int(index)

    hard_drive.append((index, content))

q_number = int(sys.stdin.readline())

# print('q_number = ', q_number)

for i in range(q_number):
    q = int(sys.stdin.readline())
    # print(i, 'th query = ', q)
    drive_number, index = convert(q, s, n)

    # print('drive number = ', drive_number, 'index = ', index)

    # 如果超出了阵列长度
    if index >= (n + 1) * s:
        print('-')
        continue

    if drive_number in [x[0] for x in hard_drive]:
        # print('硬盘没有丢失')
        # 如果所在硬盘没有丢失
        content = [x for x in hard_drive if x[0] == drive_number][0][1]
        print(content[index * 8: index * 8 + 8])
    else:
        # print('硬盘丢失')
        if able_recover:
            contentlist = [x[1][index * 8 : index * 8 + 8] for x in hard_drive]
            a, b, c, d = list(zip(*[str2int(x) for x in contentlist]))
            a = eval(' ^ '.join([str(x) for x in a]))
            b = eval(' ^ '.join([str(x) for x in b]))
            c = eval(' ^ '.join([str(x) for x in c]))
            d = eval(' ^ '.join([str(x) for x in d]))
            print(''.join([hex(x)[2:].upper() for x in [a, b, c, d]]))
        else:
            print('-')
            





# print(str2int('A0A1A2A3'))


'''
test example 2

3 2 2
0 000102030405060710111213141516172021222324252627
1 A0A1A2A3A4A5A6A7B0B1B2B3B4B5B6B7C0C1C2C3C4C5C6C7
2
2
5

2 1 2
0 000102030405060710111213141516172021222324252627
1 000102030405060710111213141516172021222324252627
2
0
1

'''

