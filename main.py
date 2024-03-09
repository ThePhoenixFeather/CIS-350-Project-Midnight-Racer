import pygame as pg
from config import *
import time as tm
from sprites import *
from gameImport import *
import sys



class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(resolution)
        self.Clock = pg.time.Clock()
        self.running = True


    def mainMenu(self):
        mainMenuState(self.screen, self.Clock)


    def newGame(self):  # A NEW GAME BEGINS
        self.playing = True

        # Load Background

        self.bg = pg.image.load("imgs\pixelroad.PNG").convert()
        self.bg = pg.transform.rotate(self.bg, 90)
        self.bg = pg.transform.scale(self.bg, resolution)

        self.allSprites  = pg.sprite.LayeredUpdates() # OBJECT CONTAINING ALL SPRITES
        self.walls = pg.sprite.LayeredUpdates() # OBJECT CONTAINING ALL WALL SPRITES
        self.slowCars = pg.sprite.LayeredUpdates() # OBJECT CONTAINING ALL SLOW CAR SPRITES
        self.player = Player(self, resolution[0]/2-playerPixelWidth/2, resolution[1]-playerPixelHeight-playerPixelHeight/2)


    def events(self):
        for events in pg.event.get():
            if events.type == pygame.QUIT:
                self.playing = False
                self.running = False


    def update(self):
        self.allSprites.update()


    def draw(self):
        self.screen.blit(self.bg, (0,0))
        self.allSprites.draw(self.screen)
        self.Clock.tick(fps)
        pg.display.update()


    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False




game = Game()
game.mainMenu()
game.newGame()

while game.running:
    game.main()