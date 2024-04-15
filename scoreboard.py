import pygame
from gameImport import *
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


class Score:
    def __init__(self, score=0, max_distance=1, score_speed=1):
        self.score, self.max_distance, self.speed = score, max_distance, score_speed

    def get_board_info(self):
        return self.score, self.max_distance, self.speed

    def set_board_info(self, new_score, new_dist, new_speed):
        self.score = new_score
        self.max_distance = new_dist
        self.speed = new_speed

def mousePosScore():
    return pygame.mouse.get_pos()

def mouseButtonsScore():
    return pygame.mouse.get_pressed()

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

def setScore(s1):
    hold = Score(s1.score, s1.max_distance, s1.speed)
    return hold


# Updates scoreboard with new scores, based on score total alone.
def updateScoreboard(cur_score, cur_dist, cur_speed):
    s1 = getScores(0)
    s2 = getScores(1)
    s3 = getScores(2)
    s4 = getScores(3)
    s5 = getScores(4)

    # use when there are scores in all the 5 positions on the scoreboard

    if cur_score >= s1.score >= 0:
        holder1 = setScore(s1)
        s1.set_board_info(cur_score, cur_dist, cur_speed)
        holder2 = setScore(s2)
        s2 = holder1
        holder3 = setScore(s3)
        s3 = holder2
        holder4 = setScore(s4)
        s4 = holder3
        s5 = holder4

    elif cur_score >= s2.score > 0:
        holder1 = setScore(s2)
        s2.set_board_info(cur_score, cur_dist, cur_speed)
        holder2 = setScore(s3)
        s3 = holder1
        holder3 = setScore(s4)
        s4 = holder2
        s5 = holder3

    elif cur_score >= s3.score > 0:
        holder1 = setScore(s3)
        s3.set_board_info(cur_score, cur_dist, cur_speed)
        holder2 = setScore(s4)
        s4 = holder1
        s5 = holder2

    elif cur_score >= s4.score > 0:
        holder1 = setScore(s4)
        s4.set_board_info(cur_score, cur_dist, cur_speed)
        s5 = holder1

    elif cur_score >= s5.score > 0:
        s5.set_board_info(cur_score, cur_dist, cur_speed)

    setScores(s1, s2, s3, s4, s5)


def scoreboardRun(screen, Clock):

    scoreBoardActive = True
    pygame.display.flip()

    isScores = 0

    black = (0, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    scoreboard = [getScores(0), getScores(1), getScores(2), getScores(3), getScores(4)]

    if scoreboard[0].score == 0 or scoreboard[0].score < 0:
        display_surface = pygame.display.set_mode(resolution)

        pygame.display.set_caption("Scoreboard")

        font = pygame.font.Font('freesansbold.ttf', 20)

        text = font.render('There are no scores to display yet.', True, green, blue)

        textRect = text.get_rect()

        textRect.center = (500//2, 1000//2)

    else:
        # Print out the scoreboard information here (on the display). Includes a button to end the scoreboardRun section.
        display_surface = pygame.display.set_mode(resolution)

        pygame.display.set_caption("Scoreboard")

        font = pygame.font.Font('freesansbold.ttf', 16)

        scores1 = getScores(0)
        scores2 = getScores(1)
        scores3 = getScores(2)
        scores4 = getScores(3)
        scores5 = getScores(4)

        scoreDisplay1 = "The Highest score is " + str(scores1.score // 1)
        scoreDisplay2 = "with a distance of " + str(scores1.max_distance // 1)
        scoreDisplay3 = "and an acceleration of " + str(scores1.speed // 1)

        if scores2.score > 0:
            scoreDisplay4 = "Second Place score is " + str(scores2.score // 1)
            scoreDisplay5 = "with a distance of " + str(scores2.max_distance // 1)
            scoreDisplay6 = "and an acceleration of " + str(scores2.speed // 1)

        if scores3.score > 0:
            scoreDisplay7 = "Third Place score is " + str(scores3.score // 1)
            scoreDisplay8 = "with a distance of " + str(scores3.max_distance // 1)
            scoreDisplay9 = "and an acceleration of " + str(scores3.speed // 1)

        if scores4.score > 0:
            scoreDisplay10 = "Fourth Place score is " + str(scores4.score // 1)
            scoreDisplay11 = "with a distance of " + str(scores4.max_distance // 1)
            scoreDisplay12 = "and an acceleration of " + str(scores4.speed // 1)

        if scores5.score > 0:
            scoreDisplay13 = "Fifth Place score is " + str(scores5.score // 1)
            scoreDisplay14 = "with a distance of " + str(scores5.max_distance // 1)
            scoreDisplay15 = "and an acceleration of " + str(scores5.speed // 1)

        text1 = font.render(scoreDisplay1, True, green, blue)
        textRect1 = text1.get_rect()
        textRect1.center = (500 // 2, 80)

        text2 = font.render(scoreDisplay2, True, green, blue)
        textRect2 = text2.get_rect()
        textRect2.center = (500 // 2, 140)

        text3 = font.render(scoreDisplay3, True, green, blue)
        textRect3 = text3.get_rect()
        textRect3.center = (500 // 2, 200)

        if scores2.score > 0:
            textspacer1 = font.render("------------------------------------------", True, green, blue)
            textRectSpacer1 = textspacer1.get_rect()
            textRectSpacer1.center = (500 // 2, 230)

            text4 = font.render(scoreDisplay4, True, green, blue)
            textRect4 = text4.get_rect()
            textRect4.center = (500 // 2, 260)

            text5 = font.render(scoreDisplay5, True, green, blue)
            textRect5 = text5.get_rect()
            textRect5.center = (500 // 2, 320)

            text6 = font.render(scoreDisplay6, True, green, blue)
            textRect6 = text6.get_rect()
            textRect6.center = (500 // 2, 380)

        if scores3.score > 0:
            textspacer2 = font.render("-----------------------------------------", True, green, blue)
            textRectSpacer2 = textspacer2.get_rect()
            textRectSpacer2.center = (500 // 2, 410)

            text7 = font.render(scoreDisplay7, True, green, blue)
            textRect7 = text7.get_rect()
            textRect7.center = (500 // 2, 440)

            text8 = font.render(scoreDisplay8, True, green, blue)
            textRect8 = text8.get_rect()
            textRect8.center = (500 // 2, 500)

            text9 = font.render(scoreDisplay9, True, green, blue)
            textRect9 = text9.get_rect()
            textRect9.center = (500 // 2, 560)

        if scores4.score > 0:
            textspacer3 = font.render("------------------------------------------", True, green, blue)
            textRectSpacer3 = textspacer3.get_rect()
            textRectSpacer3.center = (500 // 2, 590)

            text10 = font.render(scoreDisplay10, True, green, blue)
            textRect10 = text10.get_rect()
            textRect10.center = (500 // 2, 620)

            text11 = font.render(scoreDisplay11, True, green, blue)
            textRect11 = text11.get_rect()
            textRect11.center = (500 // 2, 680)

            text12 = font.render(scoreDisplay12, True, green, blue)
            textRect12 = text12.get_rect()
            textRect12.center = (500 // 2, 740)

        if scores5.score > 0:
            textspacer4 = font.render("------------------------------------------", True, green, blue)
            textRectSpacer4 = textspacer4.get_rect()
            textRectSpacer4.center = (500 // 2, 770)

            text13 = font.render(scoreDisplay13, True, green, blue)
            textRect13 = text13.get_rect()
            textRect13.center = (500 // 2, 800)

            text14 = font.render(scoreDisplay14, True, green, blue)
            textRect14 = text14.get_rect()
            textRect14.center = (500 // 2, 860)

            text15 = font.render(scoreDisplay15, True, green, blue)
            textRect15 = text15.get_rect()
            textRect15.center = (500 // 2, 920)

        isScores = isScores + 1

    display_surface.fill(black)

    bg = pygame.image.load("imgs/pixelroad.PNG").convert()
    bg = pygame.transform.scale(bg, resolution)
    screen.blit(bg, (0, 0))

    if scoreboard[0].score <= 0:
        scorebg = Button((128, 40, 40), 75, 475, 350, 50, '', "")
        scorebg.draw(screen)
    else:
        scorebg = Button((128, 40, 40), 130, 60, 240, 870, '', "")
        scorebg.draw(screen)

    if isScores == 0:
        display_surface.blit(text, textRect)
    else:
        display_surface.blit(text1, textRect1)
        display_surface.blit(text2, textRect2)
        display_surface.blit(text3, textRect3)
        if scores2.score > 0:
            display_surface.blit(textspacer1, textRectSpacer1)
            display_surface.blit(text4, textRect4)
            display_surface.blit(text5, textRect5)
            display_surface.blit(text6, textRect6)
        if scores3.score > 0:
            display_surface.blit(textspacer2, textRectSpacer2)
            display_surface.blit(text7, textRect7)
            display_surface.blit(text8, textRect8)
            display_surface.blit(text9, textRect9)
        if scores4.score > 0:
            display_surface.blit(textspacer3, textRectSpacer3)
            display_surface.blit(text10, textRect10)
            display_surface.blit(text11, textRect11)
            display_surface.blit(text12, textRect12)
        if scores5.score > 0:
            display_surface.blit(textspacer4, textRectSpacer4)
            display_surface.blit(text13, textRect13)
            display_surface.blit(text14, textRect14)
            display_surface.blit(text15, textRect15)

    exitb = Button((60, 40, 40), 1, 1, 120, 120, 'BACK', "imgs/button.png")

    exitb.draw(screen)
    exitbClick = False

    while scoreBoardActive:
        Clock.tick(30)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scoreBoardActive = False
                pygame.quit()

        pygame.display.update()

        if exitbClick and mouseButtonsScore()[0] is False:
            scoreBoardActive = False

        if exitb.isOver(mousePosScore()) and mouseButtonsScore()[0]:
            exitbClick = True

    del exitb
    pygame.display.flip()
