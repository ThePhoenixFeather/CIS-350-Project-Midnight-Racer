from sprites import *
from gameImport import *
from scoreboard import *
import math as mt


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

        # RNG Cars
        self.car1 = SlowCar(self, lane1, -600)
        self.car2 = SlowCar(self, lane2, -800)
        self.car3 = SlowCar(self, lane2, -100)
        self.car4 = SlowCar(self, lane3, -1600)
        self.car5 = SlowCar(self, lane1, -800)
        self.car6 = SlowCar(self, lane3, -1400)
        self.car7 = SlowCar(self, lane2, -1600)

        self.yPosSlowCars = [self.car1.rect.y, self.car2.rect.y, self.car3.rect.y, self.car4.rect.y, self.car5.rect.y]


        self.bgHeight= self.bg.get_height()
        self.bgNeeded = mt.ceil(resolution[1]/self.bgHeight) + 1
        self.scroll = 0

    def events(self):
        for events in pg.event.get():
            if events.type == pygame.QUIT:
                self.playing = False
                self.running = False


    def update(self):
        self.allSprites.update()
        self.yPosSlowCars = [self.car1.rect.y, self.car2.rect.y, self.car3.rect.y, self.car4.rect.y, self.car5.rect.y, self.car6.rect.y, self.car7.rect.y]
        self.xPosSlowCars = [self.car1.rect.x, self.car2.rect.x, self.car3.rect.x, self.car4.rect.x, self.car5.rect.x, self.car6.rect.x, self.car7.rect.x]


    def draw(self):
        #self.screen.blit(self.bg, (0,0))

        # draw scrolling background
        for i in range(0, self.bgNeeded):
            self.screen.blit(self.bg, (0, i * -1*self.bgHeight + self.scroll))

        # scroll background
        self.scroll += 7

        #reset scroll

        if abs(self.scroll) > self.bgHeight:
            self.scroll = 0

        self.allSprites.draw(self.screen)
        self.Clock.tick(fps)
        pg.display.update()


    def main(self):
        while self.playing:

            self.events()
            self.update()
            self.draw()
        self.running = False


flag = 0
game = Game()
while flag != 1:
    game.mainMenu()
    game.newGame()

    while game.running:
        game.main()

    updateScoreboard(points, carPosition, speed)