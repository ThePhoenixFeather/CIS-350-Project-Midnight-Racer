import pygame
import time as tm
from config import *
import scoreboard as sb
import settings as setting

class Button:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text


    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('Times New Roman', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text,
                     (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x, y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False

def updatePhysics(startTime, accelerationConstant):
    timeReturn = tm.time() - startTime
    currentSpeedReturn = accelerationConstant * timeReturn
    distanceReturn = .5 * currentSpeedReturn * timeReturn

    return timeReturn, currentSpeedReturn, distanceReturn


def mainMenuState(screen, Clock):
    mainMenuRun = True
    startB = Button((60, 40, 40), 115, 120, 280, 100, "Start")
    scoreB = Button((60, 40, 40), 115, 230, 280, 100, "Scoreboard")
    settingsB = Button((60, 40, 40), 115, 340, 280, 100, "Settings")
    quitB = Button((60, 40, 40), 115, 450, 280, 100, "Quit")

    bg = pygame.image.load("imgs/option3.JPG").convert()
    bg = pygame.transform.scale(bg, resolution)
    screen.blit(bg, (0, 0))

    startB.draw(screen)
    scoreB.draw(screen)
    settingsB.draw(screen)
    quitB.draw(screen)

    while mainMenuRun:
        Clock.tick(30)

        mousePos = pygame.mouse.get_pos()
        pygame.display.flip()
        mouseButtons = pygame.mouse.get_pressed()  # (LEFT, MID, RIGHT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainMenuRun = False
                pygame.quit()

        if startB.isOver(mousePos):
            if mouseButtons[0]:
                mainMenuRun = False

        if scoreB.isOver(mousePos):
            if mouseButtons[0]:
                mainMenuRun = False
                sb.scoreboardRun(screen, Clock)
                mainMenuRun = True

        if settingsB.isOver(mousePos):
            if mouseButtons[0]:
                mainMenuRun = False
                setting.settingsRun()
                mainMenuRun = True

        if quitB.isOver(mousePos):
            if mouseButtons[0]:
                mainMenuRun = False
                pygame.quit()

    del startB
    del scoreB
    del settingsB
    del quitB

def gameOverState(screen, Clock):
    gameOverRun = True
    youCrashed = Button((255, 40, 40), 115, 100, 280, 100, "You Crashed!")
    mainMenuB = Button((60, 40, 40), 115, 220, 280, 100, "Main Menu")
    restartB = Button((60, 40, 40), 115, 330, 280, 100, "Restart")
    quitB = Button((60, 40, 40), 115, 450, 280, 100, "Quit")

    youCrashed.draw(screen)
    mainMenuB.draw(screen)
    restartB.draw(screen)
    quitB.draw(screen)

    while gameOverRun:
        Clock.tick(30)
        mousePos = pygame.mouse.get_pos()
        pygame.display.flip()
        mouseButtons = pygame.mouse.get_pressed()  # (LEFT, MID, RIGHT)

        if mainMenuB.isOver(mousePos):
            if mouseButtons[0]:
                return 0

        if restartB.isOver(mousePos):
            if mouseButtons[0]:
                return 1

        if quitB.isOver(mousePos):
            if mouseButtons[0]:
                pygame.quit()

        pygame.display.flip()