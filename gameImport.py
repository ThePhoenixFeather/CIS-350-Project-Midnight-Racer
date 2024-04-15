import pygame
import time as tm
import scoreboard as sc
#import settings as setting
from config import *


def mousePos():
    return pygame.mouse.get_pos()

def mouseButtons():
    return pygame.mouse.get_pressed()


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
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        if self.imageLocation == '':
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.imageLocation != '':
            image = pygame.image.load(self.imageLocation).convert()
            image.set_colorkey((255, 255, 255))
            image = pygame.transform.scale(image, (self.width, self.height))
            font = pygame.font.Font('font/ARCADECLASSIC.TTF', 50)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(image, (self.x, self.y))

        if self.text != '':
            font = pygame.font.Font('font/ARCADECLASSIC.TTF', 50)
            #font = pygame.font.SysFont('Times New Roman', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text,
                     (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x, y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


def updatePhysics(startTime, accelConstant_Import):
    timeReturn = tm.time() - startTime
    currentSpeedReturn = accelConstant_Import * timeReturn
    distanceReturn = .5 * currentSpeedReturn * timeReturn

    return timeReturn, currentSpeedReturn, distanceReturn


def mainMenuState(screen, Clock):
    mainMenuRun = True

    pygame.display.set_caption("Main Menu")

    startB = Button((60, 40, 40), resolution[0]/2-310/2, 290, 310, 100, "START", "imgs/startB.png")    # Allows for buttons to display images
    scoreB = Button((60, 40, 40), resolution[0]/2-310/2, 410, 310, 100, "Scoreboard", "imgs/button.png")
    settingsB = Button((60, 40, 40), resolution[0]/2-310/2, 530, 310, 100, "Settings", "imgs/button.png")
    quitB = Button((60, 40, 40), resolution[0]/2-310/2, 750, 310, 100, "Quit", "imgs/xit.png")

    bg = pygame.image.load("imgs/option3.JPG").convert()
    bg = pygame.transform.scale(bg, resolution)
    screen.blit(bg, (0, 0))

    titleScreen = pygame.image.load("imgs/titleScreen.png").convert()
    titleScreen.set_colorkey((0, 0, 0))
    titleScreen = pygame.transform.scale(titleScreen, (350, 250))
    screen.blit(titleScreen, (80, 20))

    startB.draw(screen)
    scoreB.draw(screen)
    settingsB.draw(screen)
    quitB.draw(screen)

    startBClick = False
    scoreBClick = False
    settingsBClick = False
    quitBClick = False


    while mainMenuRun:
        Clock.tick(30)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainMenuRun = False
                pygame.quit()

        # Checks if button is pressed has been pressed and then released.
        if startBClick and mouseButtons()[0] is False:
            mainMenuRun = False

        if scoreBClick and mouseButtons()[0] is False:
            pass

        if settingsBClick and mouseButtons()[0] is False:
            pass

        if quitBClick and mouseButtons()[0] is False:
            mainMenuRun = False
            pygame.quit()
            quit()


        # Checks if button has been pressed
        if startB.isOver(mousePos()) and mouseButtons()[0]:
            startBClick = True
        else:
            startBClick = False

        if scoreB.isOver(mousePos()) and mouseButtons()[0]:
            scoreBClick = True
        else:
            scoreBClick = False

        if settingsB.isOver(mousePos()) and mouseButtons()[0]:
            settingsBClick = True
        else:
            settingsBClick = False

        if quitB.isOver(mousePos()) and mouseButtons()[0]:
            quitBClick = True
        else:
            quitBClick = False

        if scoreBClick:
            del startB
            del scoreB
            del settingsB
            del quitB

            sc.scoreboardRun(screen, Clock)

            mainMenuRun = True
            scoreBClick = False
            startB = Button((60, 40, 40), resolution[0] / 2 - 310 / 2, 290, 310, 100, "START",
                            "imgs/startB.png")  # Allows for buttons to display images
            scoreB = Button((60, 40, 40), resolution[0] / 2 - 310 / 2, 410, 310, 100, "Scoreboard", "imgs/button.png")
            settingsB = Button((60, 40, 40), resolution[0] / 2 - 310 / 2, 530, 310, 100, "Settings", "imgs/button.png")
            quitB = Button((60, 40, 40), resolution[0] / 2 - 310 / 2, 750, 310, 100, "Quit", "imgs/xit.png")

            bg = pygame.image.load("imgs/option3.JPG").convert()
            bg = pygame.transform.scale(bg, resolution)
            screen.blit(bg, (0, 0))

            titleScreen = pygame.image.load("imgs/titleScreen.png").convert()
            titleScreen.set_colorkey((0, 0, 0))
            titleScreen = pygame.transform.scale(titleScreen, (350, 250))
            screen.blit(titleScreen, (80, 20))

            startB.draw(screen)
            scoreB.draw(screen)
            settingsB.draw(screen)
            quitB.draw(screen)

        if settingsBClick:
            del startB
            del scoreB
            del settingsB
            del quitB

            setting.settingsRun()  # finish later

            mainMenuRun = True
            settingsBClick = False
            startB = Button((60, 40, 40), resolution[0] / 2 - 310 / 2, 290, 310, 100, "START",
                            "imgs/startB.png")  # Allows for buttons to display images
            scoreB = Button((60, 40, 40), resolution[0] / 2 - 310 / 2, 410, 310, 100, "Scoreboard", "imgs/button.png")
            settingsB = Button((60, 40, 40), resolution[0] / 2 - 310 / 2, 530, 310, 100, "Settings", "imgs/button.png")
            quitB = Button((60, 40, 40), resolution[0] / 2 - 310 / 2, 750, 310, 100, "Quit", "imgs/xit.png")

            bg = pygame.image.load("imgs/option3.JPG").convert()
            bg = pygame.transform.scale(bg, resolution)
            screen.blit(bg, (0, 0))

            titleScreen = pygame.image.load("imgs/titleScreen.png").convert()
            titleScreen.set_colorkey((0, 0, 0))
            titleScreen = pygame.transform.scale(titleScreen, (350, 250))
            screen.blit(titleScreen, (80, 20))

            startB.draw(screen)
            scoreB.draw(screen)
            settingsB.draw(screen)
            quitB.draw(screen)

    del startB
    del scoreB
    del settingsB
    del quitB

    pygame.display.flip()

def gameOverState(screen, Clock):
    gameOverRun = True

    font = pygame.font.Font('font/ARCADECLASSIC.TTF', 70)
    smallFont = pygame.font.Font('font/ARCADECLASSIC.TTF', 50)
    gameOver = font.render("GAME  OVER!", True, (255, 0, 0))
    youCrashed = smallFont.render("YOU CRASHED", True, (0, 0, 0))
    mainMenuB = Button((60, 40, 40), 115, 370, 280, 100, "Main Menu", "imgs/button.png")
    restartB = Button((60, 40, 40), 115, 480, 280, 100, "Restart", "imgs/button.png")
    quitB = Button((60, 40, 40), 115, 600, 280, 100, "Quit", "imgs/xit.png")

    #youCrashed.draw(screen)
    mainMenuB.draw(screen)
    restartB.draw(screen)
    quitB.draw(screen)
    screen.blit(gameOver, (85, 50))
    screen.blit(youCrashed, (105, 130))
    choice = 0

    mainMenuBClick = False
    restartBClick = False
    quitBClick = False


    while gameOverRun:
        Clock.tick(30)
        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOverRun = False
                pygame.quit()


        if mainMenuBClick and mouseButtons()[0] is False:
            choice = 0
            break

        if restartBClick and mouseButtons()[0] is False:
            choice = 1
            break

        if quitBClick and mouseButtons()[0] is False:
            pygame.quit()
            quit()

        if mainMenuB.isOver(mousePos()) and mouseButtons()[0]:
            mainMenuBClick = True

        if restartB.isOver(mousePos()) and mouseButtons()[0]:
            restartBClick = True

        if quitB.isOver(mousePos()) and mouseButtons()[0]:
            quitBClick = True

    del youCrashed
    del mainMenuB
    del restartB
    del quitB
    pygame.display.flip()
    return choice