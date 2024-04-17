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
    def __init__(self, game):
        pygame.init()
        pygame.mixer.init()

def settingsRun(screen, Clock, game):

    # Variable that dictates if the settings menu should be open
    settingsActive = True

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    volume = True # temporary variable for volume
    difficulty = True # temporary variable for difficulty
    n = 0 # variable to track which car is currently selected

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
    randbg = "imgs\pixelroad" + str(rand.randint(1, 2)) + ".png"
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
    vol = Button(black, 350, 100, 100, 100, 'ON', "imgs/button.png")
    volClick = False

    # Creates the initial difficulty button
    dif = Button(black, 350, 300, 100, 100, 'EASY', "imgs/button.png")
    difClick = False

    # Creates the right scroll button for the character selection
    right = Button(black, 350, 750, 100, 100, 'R', "imgs/button.png")
    rightClick = False
    right.draw(screen)

    # Creates the left scroll button for the character selection
    left = Button(black, 50, 750, 100, 100, 'L', "imgs/button.png")
    leftClick = False
    left.draw(screen)

    # The main display loop for the settings area
    while settingsActive:
        Clock.tick(fps)
        pygame.display.flip()

        # draws the buttons inside the loop so that they can be updated each time they are hit
        vol.draw(screen)
        dif.draw(screen)

        # debate if you want to include the car-swapping mechanic.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settingsActive = False
                pygame.quit()

        pygame.display.update()

        if exitbClick and mouseButtonsScore()[0] is False:
            settingsActive = False

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
                vol = Button(black, 350, 100, 100, 100, 'ON', "imgs/button.png")
                pygame.mixer.music.set_volume(audio)
                volClick = False

        # Difficulty Button interaction
        if difClick and mouseButtonsScore()[0] is False:
            if difficulty:
                difficulty = False
                del dif
                dif = Button(black, 350, 300, 100, 100, 'HARD', "imgs/xit.png")
                game.colBoundaries = 3
                game.accelConstant = 0.015
                difClick = False

            elif not difficulty:
                difficulty = True
                del dif
                dif = Button(black, 350, 300, 100, 100, 'EASY', "imgs/button.png")
                game.colBoundaries = 20
                game.accelConstant = accelConstant
                difClick = False

        # Car Selection Right Click interaction
        if rightClick and mouseButtonsScore()[0] is False:
            rightClick = False

            # add the right scroll feature here playercar = f"imgs/race_car_{n+1}" or something like that. go to 0 at 37

        if leftClick and mouseButtonsScore()[0] is False:
            leftClick = False

            # add the left scroll feature here playercar = f"imgs/race_car_{n-1}" or something like that. go to 37 at 0

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # BUTTON INTERACTION HERE

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

    # TO DO LIST
    # create a button that mutes/unmutes the song playing
    # create a button that swaps difficulty (increase/decrease acceleration)
    # create a section that allows the player to swap player car to a different option