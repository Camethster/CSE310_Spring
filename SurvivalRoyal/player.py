from random import randint
from pygame.constants import K_DOWN, K_LEFT, K_UP, K_a, K_s, K_w
from item import Item
import pygame as pg
import random
from settings import *

class Player(pg.sprite.Sprite):
    """ This is the basic character class and stats
    It will inherit pygames Sprite characteristics
    img:  image from image file
    ht: hieght of movement
    strength gets apllied to strength weapons and melee
    speed how far you can travel and applies to speed weapons
    constitution increases health
    sanity can limit you options as a character and improve persuasion resistance
    intelligence can limit or improve you options as a character
    persuasion can help against computers and events
    temp is important for freezing and dehydration
    x is x placement on map
    y is y placement on map
    graphic how your character will look 
    items in inventory"""
    def __init__(self,game,x,y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.health = 10
        self.strength = 10
        self.speed = 72
        self.constitution = 10
        self.sanity = 10
        self.intelligence = 10
        self.persuasion = 10
        self.temp = 96
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.items =  []
        self._collide = 0
        self.x = x
        self.y = y
        self.game = game
        self.rect = self.image.get_rect()
        self.alive = 1
    
    def move(self,dx=0,dy=0):
        """ Moves  position at set speed.
         if right too much it changes direction? Checks for collision first"""
        if not self.collide_with_walls(dx,dy) and not self.collide_with_cont(dx,dy):
            self.x += dx
            self.y += dy

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def collide_with_walls(self,dx=0,dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                self._collide = 1 
                return True
        return False
    
    def collide_with_cont(self,dx=0,dy=0):
        for cont in self.game.contestants:
            if cont.x == self.x + dx and cont.y == self.y + dy:
                self.to_battle(cont)
                return True
        return False
    
    def game_over(self):
        self.alive = 0
        print("game_over")
        return True

    def to_battle(self,con2):
        while  self.health > 0 and con2.health > 0:
            self_strike = self.strength * int(round(random.random()*.2),0)
            con2_strike = con2.strength * int(round(random.random()*.2),0)
            if self_strike > con2_strike:
                con2.health -=  (self_strike - con2_strike)
            if con2_strike > self_strike:
                self.health -= (con2_strike - self_strike)
            else:
                pass
        if self.health == 0:
            self.game_over()
        elif con2.health == 0:
            con2.game_over()



class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE   

class Computer(Player):
    def __init__(self, game, x, y):
        super.__init__(self,game,x,y)
        pg.sprite.Sprite.__init__(self, self.groups)
        self.groups = game.all_sprites, game.computer
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE   

    def move(self,dx=0,dy=0):
        """ Moves  position at set speed.
         if right too much it changes direction? Checks for collision first"""
        if not self.collide_with_walls(dx,dy):
            self.x += dx
            self.y += dy

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def collide_with_walls(self,dx=0,dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                self._collide = 1 
                return True
        return False