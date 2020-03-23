# score 100
from sys import stdin
isbn = stdin.readline().strip()
string = "".join(isbn.split("-"))
last_value = string[-1]
string = string[:-1]
sum = 0
for index, value in enumerate(string):
    sum += int(value) * (index + 1)
sum %= 11
if sum == 10:
    if last_value == "X":
        print("Right")
    else:
        print(isbn[0:-1] + "X")
else:
    if str(sum) == last_value:
        print("Right")
    else:
        print(isbn[0:-1] + str(sum))