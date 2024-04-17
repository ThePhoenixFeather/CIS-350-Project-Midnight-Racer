from sprites import *
from gameImport import *
import math as mt


class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode(resolution)
        self.Clock = pg.time.Clock()
        self.running = True
        self.choice = 0


    def gameOver(self):
        return gameOverState(self.screen, self.Clock)


    def mainMenu(self):
        mainMenuState(self.screen, self.Clock)


    def newGame(self):  # A NEW GAME BEGINS
        self.playing = True
        # Load Background
        randbg = "imgs\pixelroad" + str(rand.randint(1, 2)) + ".png"
        self.bg = pg.image.load(randbg).convert()
        #self.bg = pg.transform.rotate(self.bg, 90)
        self.bg = pg.transform.scale(self.bg, resolution)

        pg.mixer.music.load("audio\Juval - Play Your Game.mp3")
        pg.mixer.music.set_volume(0.05)
        pg.mixer.music.play(loops=-1)

        self.cScore = Button((255,255,255),0,920,300,80,"Score ")

        self.allSprites  = pg.sprite.LayeredUpdates() # OBJECT CONTAINING ALL SPRITES
        self.walls = pg.sprite.LayeredUpdates() # OBJECT CONTAINING ALL WALL SPRITES
        self.slowCars = pg.sprite.LayeredUpdates() # OBJECT CONTAINING ALL SLOW CAR SPRITES
        self.player = Player(self, resolution[0]/2-playerPixelWidth/2, resolution[1]-playerPixelHeight-playerPixelHeight/2)

        # RNG Cars
        self.car1 = SlowCar(self, lane1, 0)
        self.car2 = SlowCar(self, lane2, 0)
        self.car3 = SlowCar(self, lane2, 0)
        self.car4 = SlowCar(self, lane3, 0)
        self.car5 = SlowCar(self, lane1, 0)
        self.car6 = SlowCar(self, lane3, 0)
        self.car7 = SlowCar(self, lane2, 0)
        self.car8 = SlowCar(self, lane1, 0)
        self.car9 = SlowCar(self, lane3, 0)

        self.acceleration = 0

        self.carList = [self.car1, self.car2, self.car3, self.car4, self.car5, self.car6, self.car7, self.car8, self.car9]
        self.score = -1 * len(self.carList)

        self.yPosSlowCars = [self.car1.rect.y, self.car2.rect.y, self.car3.rect.y, self.car4.rect.y, self.car5.rect.y, self.car6.rect.y, self.car7.rect.y, self.car8.rect.y, self.car9.rect.y]
        self.xPosSlowCars = [self.car1.rect.x, self.car2.rect.x, self.car3.rect.x, self.car4.rect.x, self.car5.rect.x, self.car6.rect.x, self.car7.rect.x, self.car8.rect.x, self.car9.rect.x]


        self.bgHeight= self.bg.get_height()
        self.bgNeeded = mt.ceil(resolution[1]/self.bgHeight) + 1
        self.scroll = 0
        self.gameScore = 0
        self.gameIsOver = False
        #self.respawnAllCars()


    def respawnAllCars(self):
        for i in self.carList:
            i.respawn()
            self.update()


    def events(self):
        for events in pg.event.get():
            if events.type == pygame.QUIT:
                self.playing = False
                self.running = False


    def update(self):
        self.allSprites.update()
        self.yPosSlowCars = [self.car1.rect.y, self.car2.rect.y, self.car3.rect.y, self.car4.rect.y, self.car5.rect.y, self.car6.rect.y, self.car7.rect.y, self.car8.rect.y, self.car9.rect.y]
        self.xPosSlowCars = [self.car1.rect.x, self.car2.rect.x, self.car3.rect.x, self.car4.rect.x, self.car5.rect.x, self.car6.rect.x, self.car7.rect.x, self.car8.rect.x, self.car9.rect.x]


    def draw(self):

        # draw scrolling background
        for i in range(0, self.bgNeeded):
            self.screen.blit(self.bg, (0, i * -1*self.bgHeight + self.scroll))

        # scroll background
        self.scroll += 5 + self.acceleration

        #reset scroll

        if abs(self.scroll) > self.bgHeight:
            self.scroll = 0

        self.allSprites.draw(self.screen)
        if self.acceleration <= 12.5:
            self.acceleration += accelConstant
        else:
            self.acceleration += accelConstant / 10

        self.Clock.tick(fps)

        self.cScore.text = "Score " + str(self.score)
        self.cScore.draw(self.screen)

        pg.display.update()


    def restart(self):
        self.main()


    def main(self):
        if self.choice == 0:
            game.mainMenu()
        game.newGame()
        self.respawnAllCars()
        while self.playing:
            self.events()
            self.update()
            self.draw()
            pygame.display.set_caption("Score: " + str(self.score))
            if self.gameIsOver:
                sc.updateScoreboard(self.score, self.score * self.acceleration * 8, self.acceleration)
                self.choice = self.gameOver()
                self.playing = False
                self.restart()

        self.running = False


game = Game()
game.main()

pygame.quit()