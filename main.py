import random



SPECIAL_CELLS = [i for i in range(4)]

property_list = [{"p1": [4000, None], "p2": [3800, None], "p3": [4400, None]},    SPECIAL_CELLS[0],
                 {"p4": [4000, None], "p5": [4000, None], "p6": [4000, None]},    SPECIAL_CELLS[1],
                 {"p7": [4000, None], "p8": [4000, None], "p9": [4000, None]},    SPECIAL_CELLS[2],
                 {"p10": [4000, None], "p11": [4000, None], "p12": [4000, None]}, SPECIAL_CELLS[3]]

cells_count = 0
for i in property_list:
    if isinstance(i, dict):
        cells_count += len(i)
    else:
        cells_count += 1


class Interface:
    def __init__(self):
        pass


class Player:
    def __init__(self, name):
        self.name = name
        self.money = 15000
        self.cell = 0
        self.skip = False

    def dice_roll(self):
        self.cell = (self.cell + random.randint(1, 12)) % cells_count

    def in_cell(self):
        if (self.cell + 1) % 4 == 0:
            special_cell_activate = SPECIAL_CELLS[(self.cell + 1) // 4]
        else:
            choice = int(input('1 - buy, 0 - skip'))
            property_name = list(property_list[self.cell // 4])[self.cell % 4]
            property_price = property_list[self.cell // 4][property_name][0]
            if choice and self.money > property_price:
                property_list[self.cell // 4][property_name][1] = self.name
                self.money -= property_price


class Game:
    def __init__(self, players_count=2):
        self.players_count = players_count
        self.players = []
        self.player_number = 0

    def players_create(self):
        for i in range(self.players_count):
            name = input(f"Input {i + 1} player name: ")
            player = Player(name)
            self.players.append(player)

    def move(self):
        active_player = self.players[self.player_number]
        if not active_player.skip:
            active_player.dice_roll()
            active_player.in_cell()
            self.player_number = (self.player_number + 1) % self.players_count
        else:
            print("relax and skip your move")

    def active(self):
        for i in self.players:
            if self.players[i].money() < 0:
                return False

        return True


game = Game()
while game.active():
    game.move()