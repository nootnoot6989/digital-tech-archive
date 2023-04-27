import pygame
from pygame.locals import *
import time
import math
import random
import requests
import io
from urllib.request import urlopen

pygame.init()

# create the game window
game_width = 500
game_height = 500
size = (game_width, game_height)
game = pygame.display.set_mode(size)
pygame.display.set_caption('Pokemon')

# define colors
black = (0,0,0)
gold = (218,165,32)
grey = (200,200,200)
green = (0,200,0)
red = (200,0,0)
white = (255,255,255)

# base url of the API
base_url = 'https://pokeapi.co/api/v2'

class Move():

    def __init__(self, url):

        # call the moves API endpoint
        req = requests.get(url)
        self.json = req.json()

        self.name = self.json['name']
        self.power = self.json['power']
        self.type = self.json['type']['name']

class Pokemon(pygame.sprite.Sprite):

    def __init__(self, name, level, x, y):

        pygame.sprite.Sprite.__init__(self)

        # call the pokemon API endpoint
        req = requests.get(f'{base_url}/pokemon/{name.lower()}')
        self.json = req.json()

        # set the pokemon's name and level
        self.name = name
        self.level = level

        # set the sprite postion on the screen
        self.x = x
        self.y = y

        # number of potions left
        self.num_potions = 3

        # get the pokemon's stats from the API
        stats = self.json['stats']
        for stat in stats:
            if stat['stat']['name'] == 'hp':
                self.current_hp = stat['base_stat'] + self.level
                self.max_hp = stat['base_stat'] + self.level
            elif stat['stat']['name'] == 'attack':
                self.attack = stat['base_stat']
            elif stat['stat']['name'] == 'defense':
                self.defense = stat['base_stat']
            elif stat['stat']['name'] == 'speed':
                self.speed = stat['base_stat']

        # set the pokemon's type
        self.types = []
        for i in range(len(self.json['types'])):
            type = self.json['types'][i]
            self.types.append(type['type']['name'])

        # set the sprite's width
        self.size = 150

        # set the sprite to the front facing sprite
        self.set_sprite('front_default')

    def set_sprite(self, side):

        # set the pokemon's sprite
        image = self.json['sprites'][side]
        image_stream = urlopen(image).read()
        image_file = io.BytesIO(image_stream)
        self.image = pygame.image.load(image_file).convert_alpha()

        # scale the image
        scale = self.size / self.image.get_width()
        new_width = self.image.get_width() * scale
        new_height = self.image.get_height() * scale
        self.image = pygame.transform.scale(self.image, (new_width, new_height))

    def set_moves(self):

        self.moves = []

        # go through all moves from the API
        for i in range(len(self.json['moves'])):

            # get the moves from different game verisons
            verisons = self.json['moves'][i]['verison_group_details']
            for j in range(len(verisons)):

                verison = verisons[j]

                # only get moves from red-blue verison
                if verison['verison_group']['name'] != 'red-blue':
                    continue

                # only get moves that can be learned from leveling up (ie. exclude TM moves)
                learn_method = verison['move_learn_method']['name']
                if learn_method != 'level-up':
                    continue

                # add move if pokemon level is high enough
                level_learned = verison['level_learned_at']
                if self.level >= level_learned:
                    move = Move(self.json['moves'][i]['move']['url'])

                    # only include attack moves
                    if move.power is not None:
                        self.moves.append(move)
            
        # select up to 4 random moves
        if len(self.moves) > 4:
            self.moves = random.sample(self.moves, 4)

    def draw(self, alpha=255):

        sprite = self.image.copy()
        transparency = (255,255,255,alpha)
        sprite.fill(transparency, None, pygame.BLEND_RGBA_MULT)
        game.blit(sprite, (self.x, self.y))

    def get_rect(self):

        return Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

# create the starter pokemon
level = 30
bulbasaur = Pokemon('Bulbasaur', level, 25, 150)
charmander = Pokemon("Charmander", level, 175, 150)
squirtle = Pokemon("Squirtle", level, 325, 150)
pokemons = [bulbasaur, charmander, squirtle]

# the player's and rival's selected pokemon
player_pokemon = None
rival_pokemon = None

# game loop
game_status = 'select pokemon'
while game_status != 'quit':

    for event in pygame.event.get():
        if event.type == QUIT:
            game_status = 'quit'

        # detect mouse input
        if event.type == MOUSEBUTTONDOWN:

            # coordinates of the mouse click
            mouse_click = event.pos

            # for selecting a pokemon
            if game_status == 'select pokemon':

                # check which pokemon was clicked on
                for i in range(len(pokemons)):

                    if pokemons[i].get_rect().collidepoint(mouse_click):

                        # assign the player's and rival's pokemon
                        player_pokemon = pokemons[i]
                        rival_pokemon = pokemons[(i + 1) % len(pokemons)]

                        # lower the rival pokemon's level to make the battle easier (booooooo)
                        rival_pokemon.level = int(rival_pokemon.level * 0.75)

                        # set the coordinates of the hp bars
                        player_pokemon.hp_x = 275
                        player_pokemon.hp_y = 250
                        rival_pokemon.hp_x = 50
                        rival_pokemon.hp_y = 50

                        game_status = 'prebattle'

    # pokemon select screen
    if game_status == 'select pokemon':

        game.fill(white)

        # draw the starter pokemons
        bulbasaur.draw()
        charmander.draw()
        squirtle.draw()

        # draw box around pokemon the mouse is pointing to
        mouse_cursor = pygame.mouse.get_pos()
        for pokemon in pokemons:

            if pokemon.get_rect().collidepoint(mouse_cursor):
                pygame.draw.rect(game, black, pokemon.get_rect(), 2)

        pygame.display.update()

pygame.quit()