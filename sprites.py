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

        self.xChange = 0
        self.yChange = 0

        self.image = pg.Surface([self.width, self.height])
        self.image.fill((255,0,0))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.move()

        self.rect.x += self.xChange
        self.rect.y += self.yChange

        self.yChange = 0
        self.xChange = 0


    def move(self):
        keys = pg.key.get_pressed()

        # LEFT AND RIGHT CONTROL
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.xChange -= playerControlSpeed
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.xChange += playerControlSpeed

        # UP AND DOWN CONTROL
        if keys[pg.K_w] or keys[pg.K_UP]:
            self.yChange -= playerControlSpeed
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            self.yChange += playerControlSpeed