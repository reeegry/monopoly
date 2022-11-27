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
        #self.property = {}
        self.money = 15000
        self.cell = 0

    def dice_roll(self):
        self.cell = (self.cell + random.randint(1, 12)) % cells_count

    def action(self):
        if (self.cell + 1) % 4 == 0:
            special_cell_active = SPECIAL_CELLS[(self.cell + 1) // 4]
        else:
            choice = int(input('1 - buy, 0 - skip'))
            property_name = list(property_list[self.cell // 4])[self.cell % 4]
            property_price = property_list[self.cell // 4][property_name][0]
            if choice and self.money > property_price:
                property_list[self.cell // 4][property_name][1] = self.name
                self.money -= property_price


class Logic:
    def __init__(self):
        pass


class Game:
    def __init__(self):
        pass


game = Game()