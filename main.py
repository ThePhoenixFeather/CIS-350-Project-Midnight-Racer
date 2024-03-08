import pygame as pg
import time as tm
from gameImport import *

carPosition = 1
speed = 1
points = 0
startTime = tm.time()
time = 0
distance = 0
accelConstant = 1.1


fps = 30
pg.init()
resolution = (1920,1080)
screen = pg.display.set_mode(resolution)
Clock = pygame.time.Clock()


mainMenuState(screen, Clock)




