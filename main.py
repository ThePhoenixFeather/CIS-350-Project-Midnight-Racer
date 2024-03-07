import pygame


# Game class
class Game:
    ph = 0


# Scoreboard class
class Scoreboard:
    currScore = 0
    currTime = 0
    currAccel = 0

    savedScore_1 = 0
    savedScore_2 = 0
    savedScore_3 = 0
    savedScore_4 = 0
    savedScore_5 = 0

    savedTime_1 = 0
    savedTime_2 = 0
    savedTime_3 = 0
    savedTime_4 = 0
    savedTime_5 = 0

    savedAccel_1 = 0
    savedAccel_2 = 0
    savedAccel_3 = 0
    savedAccel_4 = 0
    savedAccel_5 = 0


# Settings Class
class Settings:
    ph = 0


if __name__ == '__main__':
    # Add pygame implementation later
    choice = 0
    while choice != 4:

        print('Please enter a number to play (1), check scoreboard (2), go to settings (3), or quit (4): ')
        input(choice)
        while choice > 4 or choice < 1:
            print('Invalid input, please reenter')

        # game section here
        if choice == 1:


        # scoreboard section here
        if choice == 2:


        # settings section here
        if choice == 3:
            
