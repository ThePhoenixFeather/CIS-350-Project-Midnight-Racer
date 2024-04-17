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
        pygame.init()
        pygame.mixer.init()


def settingsRun(screen, Clock):

    # Variable that dictates if the settings menu should be open
    settingsActive = True

    # creates the display surface
    display_surface = pygame.display.set_mode(resolution)

    # Sets the window caption to be Scoreboard
    pygame.display.set_caption("Settings")

    # Sets the font that will be used in future text.
    font = pygame.font.Font('freesansbold.ttf', 17)

    # Generates a random background, just like the game.
    randbg = "imgs\pixelroad" + str(rand.randint(1, 2)) + ".png"
    bg = pygame.image.load(randbg).convert()
    bg = pygame.transform.scale(bg, resolution)
    screen.blit(bg, (0, 0))

    # TEXT STUFF HERE, IF ANY (Label the music and difficulty change buttons)

    # TOGGLEABLE BUTTONS FOR DIFFICULTY AND MUSIC HERE
    # debate if you want to include the car-swapping mechanic.

    # Creates the Exit Button for the settings menu
    exitB = Button((60, 40, 40), 0, 0, 125, 125, 'BACK', "imgs/button.PNG")
    exitB.draw(screen)
    exitbClick = False

    # DO NOT EDIT FOR NOW
    while settingsActive:
        Clock.tick(30)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settingsActive = False
                pygame.quit()

        pygame.display.update()

        if exitbClick and mouseButtonsScore()[0] is False:
            settingsActive = False

        if exitB.isOver(mousePosScore()) and mouseButtonsScore()[0]:
            exitbClick = True

    del exitB
    pygame.display.flip()
    # create a button that mutes/unmutes the song playing