import pygame

if __name__ == '__main__':
    # Add pygame implementation later
    choice = 0
    while choice != 4:
        
        print('Please enter a number to play (1), check scoreboard (2), go to settings (3), or quit (4): ')
        input(choice)
        while choice > 4 or choice < 1:
            print('Invalid input, please reenter')
        
        if choice == 1:
            # game section here
        
        if choice == 2:
            # scoreboard section here
        
        if choice == 3:
            # settings section here
