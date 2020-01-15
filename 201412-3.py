from sys import stdin
# 先考虑没有取消的情况
records = []
cancel_order = []
while True:
    line = stdin.readline()
    if not line:
        break
    if len(line.split()) == 2:
        cancel_order.append(int(line.split()[1]))
    records.append(line)

buy = []
sell = []

for index, line in enumerate(records):
    if index + 1 not in cancel_order and len(line.split()) == 3:
        trans_type, money, count = line.split()
        if trans_type == "buy":
            buy.append((float(money), int(count)))
        elif trans_type == "sell":
            sell.append((float(money), int (count)))
buy.sort(key=lambda x: x[0], reverse=True)
sell.sort(key=lambda x: x[0])
p0 = None
while len(buy) and len(sell):
    buy_first = buy[0]
    sell_first = sell[0]
    