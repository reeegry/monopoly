def forfeit(player):
    player.money -= 1000

def skip(player):
    player.skip = True

def lucky(player):
    player.money += 1000

def surcharge(player):
    player.money *= 0.9