import pygame as pg
from config import *
import random as rand
import math as mt
import time as tm

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

        self.car = pg.image.load("imgs/race_car_0.png").convert()


        #self.car = pg.transform.scale(self.car, (self.width, self.height))
        #self.car = pg.Surface((self.width, self.height))

        self.image = self.car
        self.image = pg.Surface((playerPixelWidth, playerPixelHeight))
        self.image.set_colorkey((255,255,255))
        self.image.blit(self.car, (0,0))

        self.rect = self.car.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.move()
        #self.colideCheck()

        self.rect.x += self.xChange
        self.rect.y += self.yChange

        self.yChange = 0
        self.xChange = 0


    def move(self):
        keys = pg.key.get_pressed()
        self.checkColision()
        # LEFT AND RIGHT CONTROL

        if self.rect.x - self.width / 2 > 0:
            if keys[pg.K_a] or keys[pg.K_LEFT]:
                self.xChange -= playerControlSpeed + self.game.acceleration/5

        if self.rect.x + self.width * 1.5 < resolution[0]:
            if keys[pg.K_d] or keys[pg.K_RIGHT]:
                self.xChange += playerControlSpeed + self.game.acceleration/5

        # UP AND DOWN CONTROL

        if self.rect.y - self.height / 2 > 0:
            if (keys[pg.K_w] or keys[pg.K_UP]):
                self.yChange -= playerControlSpeed

        if self.rect.y + self.height * 1.5 < resolution[1]:
            if (keys[pg.K_s] or keys[pg.K_DOWN]):
                self.yChange += playerControlSpeed

        self.game.colision = False

    def checkColision(self):
        for i in range(len(self.game.yPosSlowCars)):
            if self.rect.y - playerPixelHeight <= self.game.yPosSlowCars[i] <= self.rect.y + playerPixelHeight and \
                    (self.game.xPosSlowCars[i] - playerPixelWidth + 10 <= self.rect.x <= self.game.xPosSlowCars[i] + playerPixelWidth - 10):
                self.game.gameIsOver = True

class SlowCar(pg.sprite.Sprite):
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

        self.car = pg.image.load("imgs/race_car_0.png").convert()
        self.image = self.car
        self.image = pg.Surface((playerPixelWidth, playerPixelHeight))
        self.image.set_colorkey((255,255,255))
        self.image.blit(self.car, (0,0))

        self.rect = self.car.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        # Moves car back up to top
        if self.rect.y >= resolution[1] + playerPixelHeight:
            self.respawn()
        self.move()

        self.rect.x += self.xChange
        self.rect.y += self.yChange

        self.yChange = 0
        self.xChange = 0



    def move(self):
        self.yChange += 2 + self.game.acceleration



    def respawn(self):
        t = 0
        while(True):
            y = rand.randint(-2800, -100)
            for i in self.game.yPosSlowCars:
                if not (-1*playerPixelHeight*2 + i <= y <= playerPixelHeight*2 + i):
                    t+=1
            if(t >= len(self.game.yPosSlowCars)):
                break
            else:
                t = 0
        self.rect.y = y