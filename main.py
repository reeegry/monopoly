import random
import special_cells


property_list = {"p1": [4000, None, 0], "p2": [3800, None, 0], "p3": [4400, None, 0], "s1" : [-1],    
                 "p4": [4000, None, 0], "p5": [4000, None, 0], "p6": [4000, None, 0], "s2" : [-1], 
                 "p7": [4000, None, 0], "p8": [4000, None, 0], "p9": [4000, None, 0], "s3" : [-1],   
                 "p10": [4000, None, 0], "p11": [4000, None, 0], "p12": [4000, None, 0], "s4" : [-1]}

cells_count = len(property_list)

sphere_code = 0
for value, keys in property_list.items():
    if len(keys) == 3:
        keys.append(sphere_code // 1000)
        sphere_code += 1

print(property_list)

class Interface:
    def __init__(self, players_list):
        self.players_list = players_list

    def rendering(self):
         print("-" * 100)
         print(self.players_list[0].name, "\t" * 4, self.players_list[1].name)
         print(self.players_list[0].money,  "\t" * 4, self.players_list[1].money)
         print(self.players_list[0].cell, "\t" * 4, self.players_list[1].cell)
         print(self.players_list[0].properties, "\t" * 4, self.players_list[1].properties)
         print("-" * 100)
        
    def transfer_print(self, player_from, player_to, sum):
        print(f"{player_from} gave {player_to} {sum}$")

    def step(self, player):
        property_name = list(property_list)[player.cell]
        print(f"player {player.name}")
        print(f"cell {player.cell}")
        print(f"property name {property_name}")

    def forfeit(self, player):
        print(f"player {player.name} paid forfeit")

    def skip(self, player):
        print(f"player {player.name} got into jail, skip one step")
    
    def lucky(self, plyaer):
        print(f"player {plyaer.name} found a treasure in his backyard")

    def surcharge(self, player):
        print(f"player {player.name} got into a fight with a tax worker in a bar and was subject to additional taxation")

class Player:
    def __init__(self, name):
        self.name = name
        self.money = 15000
        self.cell = 0
        self.skip = False
        self.properties = []

    def dice_roll(self):
        self.cell = (self.cell + random.randint(1, 12))
        if self.cell > cells_count:
            self.money += 1000
        self.cell %= cells_count

    def cost_for_another_players(self):
        temp_count = [0 for i in range(sphere_code)]
        for prop in self.properties:
            temp_count[prop[1]] += 1
        
        for i in range(len(temp_count)):
            coef = 1

            if temp_count[i] == 2:
                coef = 1.2
            if temp_count[i] == 3:
                coef = 1.4

            for j in self.properties:
                if j[1] == i:
                    property_list[j[0]][2] = property_list[j[0]][0] // 10 * coef

    def transef_of_money(self, player_2, sum):
        self.money -= sum
        player_2.money += sum

    def in_cell(self):
        property_name = list(property_list)[self.cell]
        property_price = property_list[property_name][0]
        owner = property_list[property_name][1]
        
        cost_for_stand = property_list[property_name][2]
        if owner != self.name and owner != None and cost_for_stand > 0:
            return owner, cost_for_stand

        choice = int(input(f'{property_name, property_price} 1 - buy, 0 - skip: '))


        if choice and self.money > property_price and owner == None:
            property_list[property_name][1] = self.name
            property_list[property_name][2] = property_price // 10
            self.properties.append([property_name, property_list[property_name][3]])
            self.money -= property_price
            self.cost_for_another_players()
        
        return None, 0
            

    def __str__(self):
        return self.name + " " +  str(self.money) + " " + str(self.cell)


class Game:
    def __init__(self, players_count=2):
        self.players_count = players_count
        self.players = []
        self.player_number = 0
        self.players_create()
        self.interface = Interface(self.players)

    def players_create(self):
        for i in range(self.players_count):
            name = input(f"Input {i + 1} player name: ")
            player = Player(name)
            self.players.append(player)

    def transaction(self, player_to, player_from, sum):
        player_to.money += sum
        player_from.money -= sum

    def give_player_obj_from_name(self, name):
        for i in self.players:
            if i.name == name:
                return i

    def move(self):
        active_player = self.players[self.player_number]
        if not active_player.skip:
            active_player.dice_roll()
            property_name = list(property_list)[active_player.cell]
            if len(property_list[property_name]) == 1:
                if property_name == "s1":
                    special_cells.forfeit(active_player)
                    self.interface.forfeit(active_player)
                elif property_name == "s2":
                    special_cells.skip(active_player)
                    self.interface.skip(active_player)
                elif property_name == "s3":
                    special_cells.lucky(active_player)
                    self.interface.lucky(active_player)
                elif property_name == "s4":
                    special_cells.surcharge(active_player)
                    self.interface.surcharge(active_player)
            else:
                player_to_name, sum = active_player.in_cell()
                self.interface.step(active_player)
                if player_to_name != None and sum != 0: 
                    player_to = self.give_player_obj_from_name(player_to_name)
                    self.transaction(player_to, active_player, sum)
                    self.interface.transfer_print(active_player.name, player_to_name, sum)
                
            self.player_number = (self.player_number + 1) % self.players_count

        else:
            print("relax and skip your move")
            active_player.skip = False

    def active(self):
        for player in self.players:
            if player.money < 0:
                return False

        return True


game = Game()
while game.active():
    game.interface.rendering()
    game.move()
    input("Input Enter for continue")