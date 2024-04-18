import pygame
import random as rand
from config import *


class Button:
    def __init__(self, color, x, y, width, height, text='', imageLocation=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.imageLocation = imageLocation

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(
                win,
                outline,
                (self.x - 2,
                 self.y - 2,
                 self.width + 4,
                 self.height + 4),
                0)

        if self.imageLocation == '':
            pygame.draw.rect(
                win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.imageLocation != '':
            image = pygame.image.load(self.imageLocation).convert()
            image.set_colorkey((255, 255, 255))
            image = pygame.transform.scale(image, (self.width, self.height))
            font = pygame.font.Font('font/ARCADECLASSIC.TTF', 50)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(image, (self.x, self.y))

        if self.text != '':
            font = pygame.font.Font('font/ARCADECLASSIC.TTF', 40)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text,
                     (self.x + (self.width / 2 - text.get_width() / 2),
                      self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x, y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


def mousePosScore():
    return pygame.mouse.get_pos()


def mouseButtonsScore():
    return pygame.mouse.get_pressed()


class Settings:
    def __init__(self):
        self.car_type = "12"
        self.n = 12
        self.accelConstantHolder = 0.0015

    def get_car(self):
        return self.car_type

    def set_car(self, a):
        self.car_type = a

    def get_n(self):
        return self.n

    def set_n(self, num):
        self.n = num

    def add_n(self, num):
        self.n = self.n + num

    def subtract_n(self, num):
        self.n = self.n - num

    def get_accConst(self):
        return self.accelConstantHolder

    def set_accConst(self, num):
        self.accelConstantHolder = num


def accelEquals(x, y):
    x = y
    return x


def settingsRun(screen, Clock, game, s):

    # Variable that dictates if the settings menu should be open
    settingsActive = True

    pygame.display.set_caption("Settings")

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    volume = True  # temporary variable for volume
    difficulty = True  # temporary variable for difficulty
    hold = rand.randint(1, 2)

    # Color tuples
    white = (255, 255, 255)
    black = (0, 0, 0)

    # creates the display surface
    display_surface = pygame.display.set_mode(resolution)

    # Sets the window caption to be Scoreboard
    pygame.display.set_caption("Settings")

    # Sets the font that will be used in future text.
    font = pygame.font.Font('freesansbold.ttf', 17)

    # Generates a random background, just like the game.
    randbg = "imgs\\pixelroad" + str(hold) + ".png"
    bg = pygame.image.load(randbg).convert()
    bg = pygame.transform.scale(bg, resolution)
    screen.blit(bg, (0, 0))

    # TEXT STUFF HERE, IF ANY (Label the music and difficulty change buttons)
    text1 = font.render("Toggle Music: ", True, white, black)
    textRect1 = text1.get_rect()
    textRect1.center = (150, 150)

    text2 = font.render("Toggle Difficulty: ", True, white, black)
    textRect2 = text2.get_rect()
    textRect2.center = (150, 350)

    text3 = font.render("Change Player Model: ", True, white, black)
    textRect3 = text3.get_rect()
    textRect3.center = (150, 550)

    # Create black backgrounds for each text box
    text1bg = Button(black, 85, 130, 130, 40, '', "")
    text1bg.draw(screen)

    text2bg = Button(black, 70, 330, 160, 40, '', "")
    text2bg.draw(screen)

    text3bg = Button(black, 50, 530, 200, 40, '', "")
    text3bg.draw(screen)

    display_surface.blit(text1, textRect1)
    display_surface.blit(text2, textRect2)
    display_surface.blit(text3, textRect3)

    # Creates the Exit Button for the settings menu
    exitB = Button((60, 40, 40), 0, 0, 125, 125, 'BACK', "imgs/button.PNG")
    exitB.draw(screen)
    exitbClick = False

    # Creates the initial volume button
    if pygame.mixer.music.get_volume() == 0:
        vol = Button(black, 350, 100, 100, 100, 'OFF', "imgs/xit.png")
        volClick = True
    else:
        vol = Button(black, 350, 100, 100, 100, 'ON', "imgs/button.png")
        volClick = False

    # Creates the initial difficulty button
    if s.get_accConst() == 0.0015:
        dif = Button(black, 350, 300, 100, 100, 'EASY', "imgs/button.png")
        difClick = False
    else:
        dif = Button(black, 350, 300, 100, 100, 'HARD', "imgs/xit.png")
        difClick = True

    # Creates the right scroll button for the character selection
    right = Button(black, 350, 750, 100, 100, 'R', "imgs/button.png")
    rightClick = False
    right.draw(screen)

    # Creates the left scroll button for the character selection
    left = Button(black, 50, 750, 100, 100, 'L', "imgs/button.png")
    leftClick = False
    left.draw(screen)

    # BUGGED - Displays other previous displays. Does not delete.
    car_display = Button((60, 40, 40), 150, 580, 200, 275,
                         '', f"imgs/race_car_{s.get_n()}.png")

    # The main display loop for the settings area
    while settingsActive:
        Clock.tick(30)
        pygame.display.flip()

        # draws the buttons inside the loop so that they can be updated each
        # time they are hit
        vol.draw(screen)
        dif.draw(screen)
        car_display.draw(screen)

        # debate if you want to include the car-swapping mechanic.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settingsActive = False
                pygame.quit()

        # updates the pygame display
        pygame.display.update()

        # if the button was pressed and released, do this.
        # exit button interaction
        if exitbClick and mouseButtonsScore()[0] is False:
            settingsActive = False

         # Car Selection Right Click interaction
        if rightClick and mouseButtonsScore()[0] is False:
            rightClick = False
            if s.get_n() + 1 > 37:
                s.set_car("0")
                s.set_n(0)
                del car_display

                randbg = "imgs\\pixelroad" + str(hold) + ".png"
                bg = pygame.image.load(randbg).convert()
                bg = pygame.transform.scale(bg, resolution)
                screen.blit(bg, (0, 0))

                text1bg.draw(screen)
                text2bg.draw(screen)
                text3bg.draw(screen)

                display_surface.blit(text1, textRect1)
                display_surface.blit(text2, textRect2)
                display_surface.blit(text3, textRect3)

                exitB.draw(screen)
                right.draw(screen)
                left.draw(screen)

                car_display = Button(
                    (60, 40, 40), 150, 580, 200, 275, '', f"imgs/race_car_0.png")

            else:
                s.add_n(1)
                s.set_car(f"{s.get_n()}")
                del car_display

                randbg = "imgs\\pixelroad" + str(hold) + ".png"
                bg = pygame.image.load(randbg).convert()
                bg = pygame.transform.scale(bg, resolution)
                screen.blit(bg, (0, 0))

                text1bg.draw(screen)
                text2bg.draw(screen)
                text3bg.draw(screen)

                display_surface.blit(text1, textRect1)
                display_surface.blit(text2, textRect2)
                display_surface.blit(text3, textRect3)

                exitB.draw(screen)
                right.draw(screen)
                left.draw(screen)

                car_display = Button(
                    (60, 40, 40), 150, 580, 200, 275, '', f"imgs/race_car_{s.get_n()}.png")

        if leftClick and mouseButtonsScore()[0] is False:
            leftClick = False
            if s.get_n() - 1 < 0:
                s.set_car("37")
                s.set_n(37)
                del car_display

                randbg = "imgs\\pixelroad" + str(hold) + ".png"
                bg = pygame.image.load(randbg).convert()
                bg = pygame.transform.scale(bg, resolution)
                screen.blit(bg, (0, 0))

                text1bg.draw(screen)
                text2bg.draw(screen)
                text3bg.draw(screen)

                display_surface.blit(text1, textRect1)
                display_surface.blit(text2, textRect2)
                display_surface.blit(text3, textRect3)

                exitB.draw(screen)
                right.draw(screen)
                left.draw(screen)

                car_display = Button(
                    (60, 40, 40), 150, 580, 200, 275, '', f"imgs/race_car_37.png")

            else:
                s.subtract_n(1)
                s.set_car(f"{s.get_n()}")
                del car_display

                randbg = "imgs\\pixelroad" + str(hold) + ".png"
                bg = pygame.image.load(randbg).convert()
                bg = pygame.transform.scale(bg, resolution)
                screen.blit(bg, (0, 0))

                text1bg.draw(screen)
                text2bg.draw(screen)
                text3bg.draw(screen)

                display_surface.blit(text1, textRect1)
                display_surface.blit(text2, textRect2)
                display_surface.blit(text3, textRect3)

                exitB.draw(screen)
                right.draw(screen)
                left.draw(screen)

                car_display = Button(
                    (60, 40, 40), 150, 580, 200, 275, '', f"imgs/race_car_{s.get_n()}.png")

        # Volume Button interaction
        if volClick and mouseButtonsScore()[0] is False:
            if volume:
                volume = False
                del vol
                vol = Button(black, 350, 100, 100, 100, 'OFF', "imgs/xit.png")
                pygame.mixer.music.set_volume(0)
                volClick = False

            elif not volume:
                volume = True
                del vol
                vol = Button(
                    black,
                    350,
                    100,
                    100,
                    100,
                    'ON',
                    "imgs/button.png")
                pygame.mixer.music.set_volume(audio)
                volClick = False

        # Difficulty Button interaction
        if difClick and mouseButtonsScore()[0] is False:
            if difficulty:
                difficulty = False
                del dif
                dif = Button(black, 350, 300, 100, 100, 'HARD', "imgs/xit.png")
                game.colBoundaries = 3
                s.set_accConst(0.015)
                difClick = False

            elif not difficulty:
                difficulty = True
                del dif
                dif = Button(black, 350, 300, 100, 100,
                             'EASY', "imgs/button.png")
                game.colBoundaries = 20
                s.set_accConst(0.0015)
                difClick = False

        # If key is pressed
        if exitB.isOver(mousePosScore()) and mouseButtonsScore()[0]:
            exitbClick = True

        if vol.isOver(mousePosScore()) and mouseButtonsScore()[0]:
            volClick = True

        if dif.isOver(mousePosScore()) and mouseButtonsScore()[0]:
            difClick = True

        if right.isOver(mousePosScore()) and mouseButtonsScore()[0]:
            rightClick = True

        if left.isOver(mousePosScore()) and mouseButtonsScore()[0]:
            leftClick = True
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # BUTTON INTERACTION HERE

    del exitB
    pygame.display.flip()
