import pygame
from gameImport import *

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

class Score:
    def __init__(self):
        self.score, self.max_distance, self.speed = 0, 1, 1

    def get_board_info(self):
        return self.score, self.max_distance, self.speed

    def set_board_info(self, new_score, new_dist, new_speed):
        self.score = new_score
        self.max_distance = new_dist
        self.speed = new_speed


scores = [Score(), Score(), Score(), Score(), Score()]

# Used to retrieve the scores variable array
def getScores(a):
    return scores[a]

# Used to set the scores in scores variable array
def setScores(s1, s2, s3, s4, s5):
    scores[0] = s1
    scores[1] = s2
    scores[2] = s3
    scores[3] = s4
    scores[4] = s5

# Updates scoreboard with new scores, based on score total alone.
def updateScoreboard(cur_score, cur_dist, cur_speed):
    s1 = getScores(0)
    s2 = getScores(1)
    s3 = getScores(2)
    s4 = getScores(3)
    s5 = getScores(4)

    # use when there are scores in all the 5 positions on the scoreboard
    holder1 = Score()
    holder2 = Score()
    holder3 = Score()
    holder4 = Score()

    if cur_score >= s1.score > 0:
        holder1 = s1
        s1.set_board_info(cur_score, cur_dist, cur_speed)
        holder2 = s2
        s2 = holder1
        holder3 = s3
        s3 = holder2
        holder4 = s4
        s4 = holder3
        s5 = holder4

    elif cur_score >= s2.score > 0:
        holder1 = s2
        s2.set_board_info(cur_score, cur_dist, cur_speed)
        holder2 = s3
        s3 = holder1
        holder3 = s4
        s4 = holder2
        s5 = holder3

    elif cur_score >= s3.score > 0:
        holder1 = s3
        s3.set_board_info(cur_score, cur_dist, cur_speed)
        holder2 = s4
        s4 = holder1
        s5 = holder2

    elif cur_score >= s4.score > 0:
        holder1 = s4
        s4.set_board_info(cur_score, cur_dist, cur_speed)
        s5 = holder1

    elif cur_score >= s5.score > 0:
        s5.set_board_info(cur_score, cur_dist, cur_speed)

    setScores(s1, s2, s3, s4, s5)


def scoreboardRun(screen, Clock):
    scoreBoardActive = True
    Clock.tick(30)

    pygame.display.flip()
    mouseButtons = pygame.mouse.get_pressed()
    mousePos = pygame.mouse.get_pos()

    exitb = Button((60, 40, 40), 1, 1, 50, 50)

    exitb.draw(screen)

    scoreboard = [getScores(0), getScores(1), getScores(2), getScores(3), getScores(4)]
    if scoreboard[0].score == 0:
        # Make this display the message on the display later. Include a button to return to end the scoreboardRun section.
        print("There are no scores to display yet.")
    else:
        # Print out the scoreboard information here (on the display). Include a button to return to end the scoreboardRun section.
        print("There are scores here yay!")

    while scoreBoardActive:
        if exitb.isOver(mousePos):
            if mouseButtons[0]:
                scoreBoardActive = False

    del exitb
    screen.fill((0, 0, 0))
    pygame.display.flip()