# score 100
from sys import stdin
n = int(stdin.readline())
stations = set(tuple(int(x) for x in stdin.readline().split()) for _ in range(n))

station_count = [0, 0, 0, 0, 0]

for station in stations:
    x, y = station
    count = 0
    if tuple([x + 1, y]) in stations and tuple([x, y + 1]) in stations and tuple([x, y - 1]) in stations and tuple([x-1, y]) in stations:
        if tuple([x+1, y+1]) in stations:
            count += 1
        if tuple([x+1, y-1]) in stations:
            count += 1
        if tuple([x-1, y+1]) in stations:
            count += 1
        if tuple([x-1, y-1]) in stations:
            count += 1
        station_count[count] += 1

for count in station_count:
    print(count)

