import random
import special_cells
import pygame
import sys


LENGHT = 1000
HEIGHT = 575

pygame.init()
screen = pygame.display.set_mode((LENGHT, HEIGHT))
screen.fill((100, 150, 200))

property_list = {'start': [-1], 'мотель' : [4000, None, 0, 4], 'турбаза' : [4000, None, 0, 4], 'шанс1' : [-1], 'гостинница' : [4000, None, 0, 4],  'северный порт' : [4000, None, 0, 1],   
                 'аудиосалон' : [4000, None, 0, 5], 'лотерея1' : [-1], 'видеосалон' : [4000, None, 0, 5], 'TV-магазин' : [4000, None, 0, 5], 'отделение полиции' : [-1],
                 'салон связи': [4000, None, 0, 6], 'налоги1' : [-1], 'салон игр' : [4000, None, 0, 6], 'компьютеры и оргтехника' : [4000, None, 0, 6], 'восточный порт': [4000, None, 0, 1], 
                 'спортзал' : [4000, None, 0, 7], 'водоснажебние' : [4000, None, 0, 3], 'бассейн' : [4000, None, 0, 7], 'гольфклуб' : [4000, None, 0, 7], 'стадион' : [-1], 'магазин мототехники': [4000, None, 0, 8],
                 'автосалон' : [4000, None, 0, 8], 'шанс' : [-1], 'салон спец-автотехника' : [4000, None, 0, 8], 'южный порт': [4000, None, 0, 1], 
                 'автотранс' : [4000, None, 0, 9], 'лотерея' : [-1], 'железная дорога' : [4000, None, 0, 9], 'авиакомпания' : [4000, None, 0, 9], 
                 'пустая клетка' : [-1], 'пресса' : [4000, None, 0, 0], 'колл-центр' : [3800, None, 0, 0], 'налоги' : [-1], 'книжный магазин' : [4400, None, 0, 0],
                 'западный порт' : [4000, None, 0, 1], 'закусочная' : [4000, None, 0, 2], 'электричество' : [4000, None, 0, 3], 'bar' : [4000, None, 0, 2], 'кафе': [4000, None, 0, 2]}

cells_count = len(property_list)

sphere_code = 10

class Interface:
    def __init__(self, players_list):
        self.players_list = players_list
        self.surface_info = pygame.Surface((LENGHT - HEIGHT, 300))
        self.surface_step = pygame.Surface((LENGHT - HEIGHT, 150))
        self.rect_step = self.surface_step.get_rect(topleft=(HEIGHT, 300))
        self.rect_info = self.surface_info.get_rect(topleft=(HEIGHT, 0))
        self.font = pygame.font.SysFont('arial', 15)

    def render_text(self, str_, surface, cords=(0,0)):
        text = self.font.render(str_, True, (0, 0, 0))
        text_rect = text.get_rect(topleft=cords)
        surface.blit(text, text_rect)

    def render_properties(self, x=0, player_number=0):
        for j in range(len(self.players_list[player_number].properties)):
            self.render_text(str(self.players_list[player_number].properties[j][0]), self.surface_info, (x, 60 + 20 * j))

    def render_plyer_info(self, player_number, cords):
        x, y = cords
        self.render_text(self.players_list[player_number].name, self.surface_info, (x, y))
        self.render_text(str(self.players_list[player_number].money), self.surface_info, (x, y + 20))
        self.render_text(str(self.players_list[player_number].cell), self.surface_info, (x, y + 40))
        self.render_properties(x, player_number)

    def rendering(self):
        self.surface_info.fill((100, 150, 200))
        self.surface_step.fill((100, 150, 200))
        self.render_plyer_info(0, (0, 0))
        self.render_plyer_info(1, (200, 0))
        screen.blit(self.surface_info, self.rect_info)
        screen.blit(self.surface_step, self.rect_step)


    def step(self, player):
        self.surface_step.fill((100, 150, 200))
        text_1 = f'имя игрока: {player.name}'
        text_2 = f'номер клетки: {player.cell}'
        property_name = list(property_list)[player.cell]
        text_3 = f'клетка: {property_name}'
        text_4 = '1 - купить, 0 - отказаться'

        self.render_text(text_1, self.surface_step, (20, 40))
        self.render_text(text_2, self.surface_step, (20, 60))
        self.render_text(text_3, self.surface_step, (20, 80))
        self.render_text(text_4, self.surface_step, (20, 100))

        screen.blit(self.surface_step, self.rect_step)

        pygame.display.update()

    def transfer_print(self, player_from, player_to, sum):
        self.surface_step.fill((100, 150, 200))

        text = f'{player_from} дал {player_to} {sum}$'
        self.render_text(text, self.surface_step, (20, 60))
        screen.blit(self.surface_step, self.rect_step)

        pygame.display.update()

        print(text)

    def forfeit(self, player):
        self.surface_step.fill((100, 150, 200))
        text = f'{player.name} заплатил налоги' 
        self.render_text(text, self.surface_step, (20, 60))
        screen.blit(self.surface_step, self.rect_step)

        pygame.display.update()

    def skip(self, player):
        self.surface_step.fill((100, 150, 200))
        text = f'{player.name} попал в обезьянник за пьяный дебош, пропуск хода'
        self.render_text(text, self.surface_step, (20, 60))
        screen.blit(self.surface_step, self.rect_step)

        pygame.display.update()
    
    def chance(self, plyaer):
        text = f'{plyaer.name} получается шанс получить 1000 денег'
        self.render_text(text, self.surface_step, (20, 60))
        screen.blit(self.surface_step, self.rect_step)

        pygame.display.update()

    def lotery(self, plyaer):
        text = f'{plyaer.name} крутит рулетку...'
        self.render_text(text, self.surface_step, (20, 60))
        screen.blit(self.surface_step, self.rect_step)
        
        pygame.display.update()

    def surcharge(self, player):
        self.surface_step.fill((100, 150, 200))
        text = f'{player.name} подрался с работником налоговой и подвергся'
        text_2 = 'дополнительному налогооблажению'
        self.render_text(text, self.surface_step, (20, 60))
        self.render_text(text_2, self.surface_step, (20, 80))
        screen.blit(self.surface_step, self.rect_step)

        pygame.display.update()
    
    def start_position(self, player):
        self.surface_step.fill((100, 150, 200))
        text = f'{player.name} закончил ход!!!' 
        self.render_text(text, self.surface_step, (20, 60))
        screen.blit(self.surface_step, self.rect_step)

        pygame.display.update()

    def purchased_cell(self, player):
        self.surface_step.fill((100, 150, 200))
        text = f'эта клетка уже куплена игроком {player.name}' 
        self.render_text(text, self.surface_step, (20, 60))
        screen.blit(self.surface_step, self.rect_step)

        pygame.display.update()


class Player:
    def __init__(self, name):
        self.name = name
        self.money = 15000
        self.cell = 0
        self.cell_plus_1 = random.randint(1, 6)
        self.cell_plus_2 = random.randint(1, 6)
        self.skip = False
        self.properties = []

    def roll(self):
        self.cell_plus_1 = random.randint(1, 6)
        self.cell_plus_2 = random.randint(1, 6)

    def dice_roll(self):
        self.roll()
        self.cell = (self.cell + self.cell_plus_1 + self.cell_plus_2)
        if self.cell >= cells_count:
            self.money += 1000
            print(f'{self.name} вернулся на стартовую позицию и получил 1000!')
        self.cell %= cells_count

    def cost_for_another_players(self):
        temp_count = [0 for i in range(sphere_code)]
        for prop in self.properties:
            temp_count[prop[1]] += 1
        
        for i in range(len(temp_count)):
            coef = 1

            if temp_count[i] == 2:
                coef = 1.2
            if temp_count[i] >= 3:
                coef = 1.4

            for j in self.properties:
                if j[1] == i:
                    property_list[j[0]][2] = property_list[j[0]][0] // 10 * coef

    def transef_of_money(self, player_2, sum):
        self.money -= sum
        player_2.money += sum

    def read_choice(self):
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()

                elif i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_1:
                        return 1
                    if i.key == pygame.K_0:
                        return 0

    def in_cell(self, choice):
        property_name = list(property_list)[self.cell]
        property_price = property_list[property_name][0]
        owner = property_list[property_name][1]
        
        # cost_for_stand = property_list[property_name][2]
        # if owner != self.name and owner != None and cost_for_stand > 0:
        #     return owner, cost_for_stand

        # choice = self.read_choice()


        if choice and self.money > property_price and owner == None:
            property_list[property_name][1] = self.name
            property_list[property_name][2] = property_price // 10
            self.properties.append([property_name, property_list[property_name][3]])
            self.money -= property_price
            self.cost_for_another_players()
        
        #return None, 0
            

    def __str__(self):
        return self.name + ' ' +  str(self.money) + ' ' + str(self.cell)


class Game:
    def __init__(self, players_count=2):
        self.players_count = players_count
        self.players = []
        self.player_number = 0
        self.players_create()
        self.interface = Interface(self.players)

    def players_create(self):
        for i in range(self.players_count):
            name = input(f'Input {i + 1} player name: ')
            player = Player(name)
            self.players.append(player)

    def transaction(self, player_to, player_from, sum_):
        player_to.money += sum_
        player_from.money -= sum_

    def give_player_obj_from_name(self, name):
        for i in self.players:
            if i.name == name:
                return i

    def move(self):
        active_player = self.players[self.player_number]
        if not active_player.skip:
            property_name = list(property_list)[active_player.cell]
            if len(property_list[property_name]) == 1:
                if property_name in ['налоги', 'налоги1']:
                    r = random.randint(1, 2)
                    if r == 1:
                        special_cells.forfeit(active_player)
                        self.interface.forfeit(active_player)
                    else:
                        special_cells.surcharge(active_player)
                        self.interface.surcharge(active_player)
                elif property_name == 'отделение полиции':
                    special_cells.skip(active_player)
                    self.interface.skip(active_player)
                elif property_name in ['лотерея', 'лотерея1']:
                    special_cells.lotery(active_player)
                    self.interface.lotery(active_player)
                elif property_name in ['шанс', 'шанс1']:
                    special_cells.chance(active_player)
                    self.interface.chance(active_player)
            else:
                property_name = list(property_list)[active_player.cell]
                property_price = property_list[property_name][0]
                owner = property_list[property_name][1]
                
                cost_for_stand = property_list[property_name][2]
                player_to = self.give_player_obj_from_name(owner)
                if owner != active_player.name and player_to != None:
                    # owner, cost_for_stand
                # if player_to_name != None and sum != 0: 
                    self.transaction(player_to, active_player, cost_for_stand)
                    self.interface.transfer_print(active_player.name, owner, cost_for_stand)
                elif owner == active_player.name:
                    self.interface.purchased_cell(active_player)
                else:
                    self.interface.step(active_player)
                    choice = active_player.read_choice()
                
                    active_player.in_cell(choice)
                
            self.player_number = (self.player_number + 1) % self.players_count

        else:
            print('отдохни и пропусти ход')
            active_player.skip = False

    def active(self):
        for player in self.players:
            if player.money < 0:
                return False

        return True


class Image():
    def __init__(self, path):
        self.surf = pygame.image.load(path)
        self.rect = self.surf.get_rect()

    def resize(self, field_pieces=1):
        self.surf = pygame.transform.scale(self.surf, (self.surf.get_width() // field_pieces, self.surf.get_height() // field_pieces))
        self.rect = self.surf.get_rect()

    def rendering(self, x=0, y=0, center=None):
        if center:
            self.rect.centerx = x
            self.rect.centery = y
        else:
            self.rect.x = x
            self.rect.y = y
        screen.blit(self.surf, self.rect)
    

field = Image('D:\python_projects\\anya_python\monopoly\monopoly\imgs\\table.bmp')
field.rendering()

cube_1 = Image('D:\python_projects\\anya_python\monopoly\monopoly\imgs\die1.jpg')
cube_2 = Image('D:\python_projects\\anya_python\monopoly\monopoly\imgs\die2.jpg')
cube_1.resize(8)
cube_2.resize(8)
cube_1.rendering(600, 475)
cube_2.rendering(700, 475)

cubes = []
for i in range(1, 7):
    cube = Image(f'D:\python_projects\\anya_python\monopoly\monopoly\imgs\die{i}.jpg')
    cube.resize(8)
    cubes.append(cube)

field_pieces = HEIGHT / 15
icons = []
def append_player_icon(path):
    icon = Image(path)
    icon.resize(10)
    icon.rendering(field_pieces * 1.5, field_pieces * 1.5, True)
    icons.append(icon)

append_player_icon('D:\python_projects\\anya_python\monopoly\monopoly\imgs\hat.png')
append_player_icon('D:\python_projects\\anya_python\monopoly\monopoly\imgs\car.png')
append_player_icon('D:\python_projects\\anya_python\monopoly\monopoly\imgs\iron.png')
append_player_icon('D:\python_projects\\anya_python\monopoly\monopoly\imgs\ship.png')

pygame.display.update()
player_numbers = 2
game = Game()
k = 1
while game.active():
    if k:
        print('Press space for make move')
        k = 0

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                k = 1
                active_player = game.players[game.player_number]
                print('active player: ', active_player)
                if not active_player.skip:
                    active_player.dice_roll()
                game.interface.rendering()
                cube_1 = cubes[active_player.cell_plus_1 - 1]
                cube_2 = cubes[active_player.cell_plus_2 - 1]
                cube_1.rendering(700, 475)
                cube_2.rendering(600, 475)
                icon = icons[game.player_number]

                field.rendering()
                for i in range(player_numbers):
                    if i != game.player_number:
                        icons[i].rendering(icons[i].rect.x, icons[i].rect.y)

                #изменять в условия только координаты
                if active_player.cell // 10 == 0:
                    icon.rendering(field_pieces * 3.5 + field_pieces * (active_player.cell - 1), field_pieces * 1.5, True) 
                elif active_player.cell // 10 == 1:
                    icon.rendering(LENGHT - 425 - field_pieces * 1.5, HEIGHT - field_pieces * 3.5 - field_pieces * (9 - active_player.cell % 10),  True)
                elif active_player.cell // 10 == 2:
                    icon.rendering(HEIGHT - field_pieces * 3.5 - field_pieces * (active_player.cell % 10 - 1), HEIGHT - field_pieces * 1.5, True)
                elif active_player.cell // 10 == 3:
                    icon.rendering(field_pieces * 1.5, HEIGHT - 3.5 * field_pieces - field_pieces * (active_player.cell % 10 - 1), True)

                pygame.display.update()

                print(active_player.cell)
                print(active_player.cell_plus_1)
                print(active_player.cell_plus_2)
                game.move()



    pygame.display.flip()