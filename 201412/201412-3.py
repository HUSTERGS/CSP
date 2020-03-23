from sys import stdin

records = {}
count = 1
while True:
    line = stdin.readline()
    if not line:
        break
    if len(line.split()) == 2:
        del records[int(line.split()[1])]
        continue
    records[count] = line.split()
    # if count == 6:
    #     break
    count += 1


records_list = list(records.values())
records_list.sort(key=lambda x: float(x[1]))
index = 0
p_0 = float(records_list[index][1])
buy_total = sum([int(x[2]) for x in records_list if x[0] == "buy"])
sell_total = 0
if records_list[index][0] == "sell":
    sell_total = int(records_list[index][2])
best_transaction = min(buy_total, sell_total)
highest_p = p_0
while index < len(records_list) - 1:
    i = index
    while i >= 0 and float(records_list[i][1]) == p_0 and records_list[i][0] == "buy":
        buy_total -= int(records_list[i][2])
        i -= 1
    index += 1
    p_0 = float(records_list[index][1])

    while index < len(records_list) and float(records_list[index][1]) == p_0:
        if records_list[index][0] == "sell":
            sell_total += int(records_list[index][2])
        index += 1
    index -= 1
    if min(sell_total, buy_total) > best_transaction:
        best_transaction = min(sell_total, buy_total)
        highest_p = p_0
print("%.2f" % (highest_p, ), best_transaction)

