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


class Score:
    def __init__(self, score=0, max_distance=1, score_speed=1):
        self.score, self.max_distance, self.speed = score, max_distance, score_speed

    def get_board_info(self):
        return self.score, self.max_distance, self.speed

    def set_board_info(self, new_score, new_dist, new_speed):
        self.score = new_score
        self.max_distance = new_dist
        self.speed = new_speed

# Gets an input on where the mouse cursor is at on the screen
def mousePosScore():
    return pygame.mouse.get_pos()

# Gets a bool input on whether a certain mouse button has been pressed
def mouseButtonsScore():
    return pygame.mouse.get_pressed()

# Array of scores
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

# Used to unsure that ONLY values are being copied to a holder variable as opposed to the reference to a score variable.
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

    # This if / elif section helps to sort the scores that are received. Only score is the de
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

    # Sets the updated and sorted scores to the scoreboard array
    setScores(s1, s2, s3, s4, s5)

# This is essentially the main function of scoreboard. This is the meat and potatoes of scoreboard's display.
def scoreboardRun(screen, Clock):
    # Flips the Pygame display and creates a boolean value that tracks if the scoreboard should remain active.
    scoreBoardActive = True
    pygame.display.flip()

    # Value to tell the program if a score has been recorded at least once.
    isScores = 0

    # Various Color Tuples
    white = (255, 255, 255)
    black = (0, 0, 0)
    # green = (0, 255, 0)
    # blue = (0, 0, 128)

    # Array that holds score class variables.
    scoreboard = [getScores(0), getScores(1), getScores(2), getScores(3), getScores(4)]

    # checks if the score is at 0 or below in case of an error
    if scoreboard[0].score == 0 or scoreboard[0].score < 0:

        # Creates a surface that is the size of our resolution config size.
        display_surface = pygame.display.set_mode(resolution)

        # Sets the display caption to Scoreboard
        pygame.display.set_caption("Scoreboard")

        # Initializes the font type and size
        font = pygame.font.Font('freesansbold.ttf', 25)

        # Initializes the text that will be displayed, as well as the text and background color.
        text = font.render('There are no scores to display yet', True, white, black)

        # Creates the text in a rectangle form.
        textRect = text.get_rect()

        # Sets the text to be placed at the center of the display
        textRect.center = (500//2, 1000//2)

    # if there is a score and there is no out-of-bounds type of error, does this
    else:

        # Print out the scoreboard information here (on the display). Includes a button to end the scoreboardRun section.
        display_surface = pygame.display.set_mode(resolution)

        # Sets the window caption to be Scoreboard
        pygame.display.set_caption("Scoreboard")

        # Sets the font that will be used in future text.
        font = pygame.font.Font('freesansbold.ttf', 20)

        # Gets the scores of each individual score in the array and stores it into the 5 different values.
        scores1 = getScores(0)
        scores2 = getScores(1)
        scores3 = getScores(2)
        scores4 = getScores(3)
        scores5 = getScores(4)

        # Displays the Current Highest Score
        scoreDisplay1 = f"The Highest score is {scores1.score}"
        scoreDisplay2 = f"with a distance of {scores1.max_distance:.2f}"
        scoreDisplay3 = f"and an acceleration of {scores1.speed:.2f}"

        # if there is a score in second place, do this.
        if scores2.score > 0:
            scoreDisplay4 = f"Second Place score is {scores2.score}"
            scoreDisplay5 = f"with a distance of {scores2.max_distance:.2f}"
            scoreDisplay6 = f"and an acceleration of {scores2.speed:.2f}"

        # if there is a score in third place, do this.
        if scores3.score > 0:
            scoreDisplay7 = f"Third Place score is {scores3.score}"
            scoreDisplay8 = f"with a distance of {scores3.max_distance:.2f}"
            scoreDisplay9 = f"and an acceleration of {scores3.speed:.2f}"

        # if there is a score in fourth place, do this.
        if scores4.score > 0:
            scoreDisplay10 = f"Fourth Place score is {scores4.score}"
            scoreDisplay11 = f"with a distance of {scores4.max_distance:.2f}"
            scoreDisplay12 = f"and an acceleration of {scores4.speed:.2f}"

        # if there is a score in fifth place, do this.
        if scores5.score > 0:
            scoreDisplay13 = f"Fifth Place score is {scores5.score}"
            scoreDisplay14 = f"with a distance of {scores5.max_distance:.2f}"
            scoreDisplay15 = f"and an acceleration of {scores5.speed:.2f}"

        # All below sections create the text display backgrounds for each text object. This creates the text display, but not on the screen.
        text1 = font.render(scoreDisplay1, True, white, black)
        textRect1 = text1.get_rect()
        textRect1.center = (360, 80)

        text2 = font.render(scoreDisplay2, True, white, black)
        textRect2 = text2.get_rect()
        textRect2.center = (360, 140)

        text3 = font.render(scoreDisplay3, True, white, black)
        textRect3 = text3.get_rect()
        textRect3.center = (360, 200)

        # Does this if there is a score in scores2.
        if scores2.score > 0:
            textspacer1 = font.render("------------------------------------------", True, white, black)
            textRectSpacer1 = textspacer1.get_rect()
            textRectSpacer1.center = (360, 230)

            text4 = font.render(scoreDisplay4, True, white, black)
            textRect4 = text4.get_rect()
            textRect4.center = (360, 260)

            text5 = font.render(scoreDisplay5, True, white, black)
            textRect5 = text5.get_rect()
            textRect5.center = (360, 320)

            text6 = font.render(scoreDisplay6, True, white, black)
            textRect6 = text6.get_rect()
            textRect6.center = (360, 380)

        # Does this if there is a score in scores3.
        if scores3.score > 0:
            textspacer2 = font.render("------------------------------------------", True, white, black)
            textRectSpacer2 = textspacer2.get_rect()
            textRectSpacer2.center = (360, 410)

            text7 = font.render(scoreDisplay7, True, white, black)
            textRect7 = text7.get_rect()
            textRect7.center = (360, 440)

            text8 = font.render(scoreDisplay8, True, white, black)
            textRect8 = text8.get_rect()
            textRect8.center = (360, 500)

            text9 = font.render(scoreDisplay9, True, white, black)
            textRect9 = text9.get_rect()
            textRect9.center = (360, 560)

        # Does this if there is a score in scores4.
        if scores4.score > 0:
            textspacer3 = font.render("------------------------------------------", True, white, black)
            textRectSpacer3 = textspacer3.get_rect()
            textRectSpacer3.center = (360, 590)

            text10 = font.render(scoreDisplay10, True, white, black)
            textRect10 = text10.get_rect()
            textRect10.center = (360, 620)

            text11 = font.render(scoreDisplay11, True, white, black)
            textRect11 = text11.get_rect()
            textRect11.center = (360, 680)

            text12 = font.render(scoreDisplay12, True, white, black)
            textRect12 = text12.get_rect()
            textRect12.center = (360, 740)

        # Does this if there is a score in scores5.
        if scores5.score > 0:
            textspacer4 = font.render("------------------------------------------", True, white, black)
            textRectSpacer4 = textspacer4.get_rect()
            textRectSpacer4.center = (360, 770)

            text13 = font.render(scoreDisplay13, True, white, black)
            textRect13 = text13.get_rect()
            textRect13.center = (360, 800)

            text14 = font.render(scoreDisplay14, True, white, black)
            textRect14 = text14.get_rect()
            textRect14.center = (360, 860)

            text15 = font.render(scoreDisplay15, True, white, black)
            textRect15 = text15.get_rect()
            textRect15.center = (360, 920)

        # increments isScore if the else statement was activated.
        if isScores == 0:
            isScores = isScores + 1

    # Makes the display surface black
    display_surface.fill(black)

    # Creates a background over the black surface
    bg = pygame.image.load("imgs/option3.jpg").convert()
    bg = pygame.transform.scale(bg, resolution)
    screen.blit(bg, (0, 0))

    # All of these below accurately displays the information on top of the previous surface based on whether there is a score or not as well.
    if isScores == 0:

        # Creates a black section of on the image where the scores will be displayed.
        scorebg = Button(black, 30, 480, 440, 40, '', "")
        scorebg.draw(screen)

        display_surface.blit(text, textRect)
    else:

        # Creates a black section of on the image where the scores will be displayed.
        scorebg = Button(black, 210, 35, 290, 920, '', "")
        scorebg.draw(screen)

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

    # Creates the exit button in the top left
    exitb = Button((60, 40, 40), 1, 1, 125, 125, 'BACK', "imgs/button.png")
    exitb.draw(screen)
    exitbClick = False

    # This is essentially the 'main' file part of the file, as it creates the opportunity for the player to interact with the scoreboard menu.
    while scoreBoardActive:
        Clock.tick(30)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scoreBoardActive = False
                pygame.quit()

        pygame.display.update()

        # Check if mouse is pressed and released
        if exitbClick and mouseButtonsScore()[0] is False:
            scoreBoardActive = False

        if exitb.isOver(mousePosScore()) and mouseButtonsScore()[0]:
            exitbClick = True

    del exitb
    pygame.display.flip()