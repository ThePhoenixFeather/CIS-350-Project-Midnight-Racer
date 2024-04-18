import math as mt
from sprites import Player, pg, rand, SlowCar
from gameImport import mainMenuState, Button, gameOverState, sc
from settings import Settings, accelEquals
from config import accelConstant, resolution, playerPixelHeight, playerPixelWidth, lane1, lane2, lane3, audio, fps



class Game:


    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode(resolution)
        self.clock = pg.time.Clock()
        self.running = True
        self.choice = 0
        self.col_boundaries = 20
        self.accel_constant = accelConstant
        self.player = Player

        self.car1 = None
        self.car2 = None
        self.car3 = None
        self.car4 = None
        self.car5 = None
        self.car6 = None
        self.car7 = None
        self.car8 = None
        self.car9 = None

        self.playing = False
        self.b_g = None

        self.c_score = None
        self.all_sprites = None
        self.walls = None

        self.slow_cars = None
        self.player = None
        self.acceleration = None
        self.car_list = None
        self.score = None
        self.y_pos_slowcars = None
        self.x_pos_slowcars = None
        self.bg_height = None
        self.bg_needed = None
        self.scroll = None
        self.game_is_over = False

    def gameOver(self):
        return gameOverState(self.screen, self.clock)

    def setAccConstGame(self, num):
        self.accel_constant = num

    def mainMenu(self, s):
        mainMenuState(
            self.screen,
            self.clock,
            self.player,
            s,
            self.accel_constant)

    def newGame(self, s_in):  # A NEW GAME BEGINS
        self.playing = True
        # Load Background
        randbg = "imgs\\pixelroad" + str(rand.randint(1, 2)) + ".png"
        # self.bg = pg.transform.rotate(self.bg, 90)
        self.b_g = pg.transform.scale(pg.image.load(randbg).convert(), resolution)

        self.c_score = Button((255, 255, 255), 0, 920, 300, 80, "Score ")

        self.all_sprites = pg.sprite.LayeredUpdates()  # OBJECT CONTAINING ALL SPRITES
        self.walls = pg.sprite.LayeredUpdates()  # OBJECT CONTAINING ALL WALL SPRITES
        # OBJECT CONTAINING ALL SLOW CAR SPRITES
        self.slow_cars = pg.sprite.LayeredUpdates()
        self.player = Player(
            self,
            resolution[0] /
            2 -
            playerPixelWidth /
            2,
            resolution[1] -
            playerPixelHeight -
            playerPixelHeight /
            2,
            s_in)

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

        self.car_list = [
            self.car1,
            self.car2,
            self.car3,
            self.car4,
            self.car5,
            self.car6,
            self.car7,
            self.car8,
            self.car9]
        self.score = -1 * len(self.car_list)

        self.y_pos_slowcars = [
            self.car1.rect.y,
            self.car2.rect.y,
            self.car3.rect.y,
            self.car4.rect.y,
            self.car5.rect.y,
            self.car6.rect.y,
            self.car7.rect.y,
            self.car8.rect.y,
            self.car9.rect.y]
        self.x_pos_slowcars = [
            self.car1.rect.x,
            self.car2.rect.x,
            self.car3.rect.x,
            self.car4.rect.x,
            self.car5.rect.x,
            self.car6.rect.x,
            self.car7.rect.x,
            self.car8.rect.x,
            self.car9.rect.x]

        self.bg_height = self.b_g.get_height()
        self.bg_needed = mt.ceil(resolution[1] / self.bg_height) + 1
        self.scroll = 0
        self.game_is_over = False
        # self.respawnAllCars()

    def respawnAllCars(self):
        for i in self.car_list:
            i.respawn()
            self.update()

    def events(self):
        for events in pg.event.get():
            if events.type == pg.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()
        self.y_pos_slowcars = [
            self.car1.rect.y,
            self.car2.rect.y,
            self.car3.rect.y,
            self.car4.rect.y,
            self.car5.rect.y,
            self.car6.rect.y,
            self.car7.rect.y,
            self.car8.rect.y,
            self.car9.rect.y]
        self.x_pos_slowcars = [
            self.car1.rect.x,
            self.car2.rect.x,
            self.car3.rect.x,
            self.car4.rect.x,
            self.car5.rect.x,
            self.car6.rect.x,
            self.car7.rect.x,
            self.car8.rect.x,
            self.car9.rect.x]

    def draw(self):

        # draw scrolling background
        for i in range(0, self.bg_needed):
            self.screen.blit(
                self.b_g, (0, i * -1 * self.bg_height + self.scroll))

        # scroll background
        self.scroll += 5 + self.acceleration

        # reset scroll

        if abs(self.scroll) > self.bg_height:
            self.scroll = 0

        self.all_sprites.draw(self.screen)
        if self.acceleration <= 12.5:
            self.acceleration += self.accel_constant
        else:
            self.acceleration += self.accel_constant / 10

        self.clock.tick(fps)

        self.c_score.text = "Score " + str(self.score)
        self.c_score.draw(self.screen)

        pg.display.update()

  #  def restart(self):
  #      self.main()

    def main(self):
        s_in = Settings()
        restart = True
        while restart:
            if self.choice == 0:
                game.mainMenu(s_in)
            self.accel_constant = accelEquals(
                self.accel_constant, s_in.accelConstantHolder)
            self.col_boundaries = accelEquals( # Works in this case as well
                self.col_boundaries, s_in.boundaryHolder)
            game.newGame(s_in.get_car())
            self.respawnAllCars()
            while self.playing:
                self.events()
                self.update()
                self.draw()
                pg.display.set_caption("Score: " + str(self.score))
                if self.game_is_over:
                    sc.updateScoreboard(
                        self.score,
                        self.score * self.acceleration * 8,
                        self.acceleration)
                    self.choice = self.gameOver()
                    self.playing = False
        self.running = False


game = Game()

pg.mixer.music.load("audio\\Juval - Play Your Game.mp3")
pg.mixer.music.set_volume(audio)
pg.mixer.music.play(loops=-1)

game.main()

pg.quit()