import pygame as pg
from config import *
import random as rand
import math as mt

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = playerLayer
        self.groups = self.game.allSprites
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = playerPixelWidth
        self.height = playerPixelHeight

        self.image = pg.Surface([self.width, self.height])
        self.image.fill((255,0,0))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass