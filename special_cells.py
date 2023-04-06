import random


def start(player):
    player.money += 1000

def forfeit(player):
    player.money -= 1000

def skip(player):
    player.skip = True

def chance(player):
    r = random.randint(1, 2)
    if r == 1:
        player.money += 1000

def lotery(player):
    r = random.random()
    if r <= 0.01:
        player.money += 10000
    else:
        player.money -= 100

def surcharge(player):
    player.money *= 0.9