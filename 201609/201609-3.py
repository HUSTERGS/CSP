# score 100
from sys import stdin

n = int(stdin.readline())


class Slave:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack

    def attack_slave(self, slave):
        self.health -= slave.attack
        slave.health -= self.attack
        return self.health, slave.health


player1 = [Slave(30, 0), ]
player2 = [Slave(30, 0), ]
players = [player1, player2]
current_player = 0
win = 0
for _ in range(n):
    action = stdin.readline().strip().split()

    if len(action) == 1:
        # end
        current_player += 1
        current_player %= 2
    elif len(action) == 3:
        # attack
        slave1, slave2 = int(action[1]), int(action[2])
        p1 = players[current_player]
        p2 = players[(current_player + 1) % 2]
        h1, h2 = p1[slave1].attack_slave(p2[slave2])
        if h1 <= 0:
            if slave1 == 0:
                # 如果是英雄死了,那么直接退出
                win = 2 * current_player - 1
                break
            p1.pop(slave1)
        if h2 <= 0:
            if slave2 == 0:
                win = -2 * current_player + 1
                break
            p2.pop(slave2)
    elif len(action) == 4:
        # summon
        position, attack, health = [int(x) for x in action[1:]]
        players[current_player].insert(position, Slave(health, attack))

print(win)
print(player1[0].health)
print(len(player1) - 1, end=" ")
print(" ".join(str(x.health) for x in player1[1:]))
print(player2[0].health)
print(len(player2) - 1, end=" ")
print(" ".join(str(x.health) for x in player2[1:]))