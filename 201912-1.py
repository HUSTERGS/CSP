from sys import stdin
call_count = [0, ] * 4
n = int(stdin.readline())
current_num = 1
current_index = 0
count = 0
while count != n:
    if current_num % 7 == 0 or '7' in str(current_num):
        call_count[current_index] += 1
    else:
        count += 1
    current_num += 1
    current_index += 1
    current_index %= 4

for num in call_count:
    print(num)