import pygame
import time as tm

class Button():
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
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

def updatePhysics(startTime, accelConstant):
    timeReturn = tm.time() - startTime
    currentSpeedReturn = accelConstant * timeReturn
    distanceReturn = .5 * (currentSpeedReturn) * timeReturn

    return timeReturn, currentSpeedReturn, distanceReturn


def mainMenuState(screen, Clock):
    mainMenuRun = True
    startB = Button((60, 40, 40), 90, 90, 170, 100, "Start")
    quitB = Button((60, 40, 40), 90, 200, 170, 100, "Quit")
    startB.draw(screen)
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

        if (startB.isOver(mousePos) == True):
            if (mouseButtons[0] == True):
                mainMenuRun = False

        if (quitB.isOver(mousePos) == True):
            if (mouseButtons[0] == True):
                mainMenuRun = False
                pygame.quit()

    del(startB)
    del(quitB)
    screen.fill((0, 0, 0))
    pygame.display.flip()