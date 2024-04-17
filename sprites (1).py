import pygame as pg
from config import *
import random as rand

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        """
        Initialize the Player object.

        Parameters:
            game (Game): The Game object instance.
            x (int): The initial x-coordinate of the player's car.
            y (int): The initial y-coordinate of the player's car.
        """
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

        # Load and scale the player's car image
        self.car = pg.image.load("imgs/race_car_12.png").convert()
        self.car = pg.transform.scale(self.car, (playerPixelWidth,playerPixelHeight))

        self.image = self.car
        self.image = pg.Surface((playerPixelWidth, playerPixelHeight))
        self.image.set_colorkey((255,255,255))
        self.image.blit(self.car, (0,0))

        # Set the rectangle to the car's dimensions and position
        self.rect = self.car.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        """
        Update the player's position based on user input.
        """
        self.move()
        self.rect.x += self.xChange
        self.rect.y += self.yChange
        self.yChange = 0
        self.xChange = 0

    def move(self):
        """
        Move the player's car based on keyboard input.
        """
        keys = pg.key.get_pressed()
        self.checkCollision()

        # Control the player's movement
        if self.rect.x - self.width / 2 > 0:
            if keys[pg.K_a] or keys[pg.K_LEFT]:
                self.xChange -= playerControlSpeed + self.game.acceleration/3

        if self.rect.x + self.width * 1.5 < resolution[0]:
            if keys[pg.K_d] or keys[pg.K_RIGHT]:
                self.xChange += playerControlSpeed + self.game.acceleration/3

        if self.rect.y - self.height / 2 > 0:
            if (keys[pg.K_w] or keys[pg.K_UP]):
                self.yChange -= playerControlSpeed

        if self.rect.y + self.height < resolution[1]:
            if (keys[pg.K_s] or keys[pg.K_DOWN]):
                self.yChange += playerControlSpeed + self.game.acceleration/3

        self.game.colision = False

    def checkCollision(self):
        """
        Check for collisions between the player's car and slow-moving cars.
        """
        for i in range(len(self.game.yPosSlowCars)):
            if self.rect.y - playerPixelHeight + self.game.colBoundaries <= self.game.yPosSlowCars[i] <= self.rect.y + playerPixelHeight - self.game.colBoundaries and \
                    (self.game.xPosSlowCars[i] - playerPixelWidth + self.game.colBoundaries <= self.rect.x <= self.game.xPosSlowCars[i] + playerPixelWidth - self.game.colBoundaries):
                pass
                self.game.gameIsOver = True

class SlowCar(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        """
        Initialize the SlowCar object.

        Parameters:
            game (Game): The Game object instance.
            x (int): The initial x-coordinate of the slow-moving car.
            y (int): The initial y-coordinate of the slow-moving car.
        """
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

        # Load and scale the slow-moving car image
        self.car = pg.image.load("imgs/race_car_" + str(rand.randint(0,36)) + ".png").convert()
        self.car = pg.transform.scale(self.car, (playerPixelWidth,playerPixelHeight))
        self.image = self.car
        self.image = pg.Surface((playerPixelWidth, playerPixelHeight))
        self.image.set_colorkey((255,255,255))
        self.image.blit(self.car, (0,0))

        # Set the rectangle to the car's dimensions and position
        self.rect = self.car.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.nextTo = False

    def update(self):
        """
        Update the slow-moving car's position.
        """
        if self.rect.y >= resolution[1] + playerPixelHeight/2:
            self.respawn()
        self.move()

        self.rect.x += self.xChange
        self.rect.y += self.yChange
        self.yChange = 0
        self.xChange = 0

    def move(self):
        """
        Move the slow-moving car downwards.
        """
        self.yChange += slowCarSpeed + self.game.acceleration

    def respawn(self):
        """
        Respawn the slow-moving car at a random position.
        """
        t = 0
        x = 0
        y = 0
        posCheck = False
        while(True):
            x+=1
            y = rand.randint(-5200, -100)
            for i in self.game.carList:
                if not (-1*playerPixelHeight*2.5 + i.rect.y <= y <= playerPixelHeight*2.5 + i.rect.y):
                    t+=1

                elif(i.rect.x != self.rect.x and posCheck == False and i.nextTo == False and self.nextTo == False):
                    t+=1
                    posCheck = True
                    i.nextTo = True
            if(t >= len(self.game.carList)):
                break
            if(x>=4000):
                y = rand.randint(-4700, -3300)
            else:
                t = 0
        if posCheck == True:
            self.nextTo = True
        else:
            self.nextTo = False
        self.rect.y = y
        self.car = pg.image.load("imgs/race_car_" + str(rand.randint(0, 36)) + ".png").convert()
        self.car = pg.transform.scale(self.car, (playerPixelWidth, playerPixelHeight))
        self.image = self.car
        self.image = pg.Surface((playerPixelWidth, playerPixelHeight))
        self.image.set_colorkey((255, 255, 255))
        self.image.blit(self.car, (0, 0))
        self.game.score += 1


