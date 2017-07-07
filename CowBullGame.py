#Importing Required Modules
import pygame, random, sys
from pygame.locals import *

#Initialising PyGame Module
pygame.init()

#Initialising Global Variables
Canvas = pygame.display.set_mode((1100, 700))
pygame.display.set_caption("Cow Bull Game")
white = (255, 255, 255)
black = (0, 0, 0)
font1 = "Times New Roman"
font2 = "Arial"

#Function To Show Text As Per The Required Parameters
def text(string, size, color, top, left, fonttype = None, bold = False, italic = False):
    font = pygame.font.SysFont(fonttype, size, bold, italic)
    textobj = font.render(string, 1, color)
    textrect = textobj.get_rect()
    textrect.top = top
    textrect.left = left
    Canvas.blit(textobj, textrect)
    pygame.display.update()

#Function To Set A Word From The Database
def set_word():
    file = open("Wordlist.txt", "r")
    ran = random.randrange(124)
    s = ""
    for i in range(ran):
        s = file.readline()
    file.close()
    return(s[0:4])

#Function To Display Alphabets
def alph():
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l = 30
    for i in alpha:
        text(i, 55, black, 50, l)
        l = l + 40

#Function To Wait For An Input At Certain Screens
def waitforkey():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == MOUSEBUTTONDOWN:
                return

#Function To Kill The Program
def terminate():
    pygame.quit()
    sys.exit()

#Function To Display/Refresh The Game Screen
def dispGame(turn, words):
    Canvas.fill(white)
    alph()
    text("Your word has been chosen.", 25, black, 110, 30, font2, False, True)
    text("Choose from the above alphabets to guess the word.", 25, black, 140, 30, font2, False, True)
    a = "Turn : " + str(turn)
    text(a, 23, black, 15, 30, font1, False, True)
    for i in range(4):
        text("_", 140, black, 330, i*100+100)
    for i in range(len(words)):
        text(str(i+1) + ". " + words[i][0], 22, black, 107+i*55, 930, font1)
        b = "B: " + str(words[i][1]) + " / C: " + str(words[i][2])
        text(b, 19, black, 130+i*55, 950, font1)

#Function To Display/Refresh User Input
def updateguess(guess = ""):
    
    #Command To Clear Old Input By Overlapping It With A Rectangle Of Background Color
    pygame.draw.rect(Canvas, white, (100 , 320, 400, 70))
    
    #Command To Display Updated Input
    for i in range(len(guess)):
        text(guess[i], 120, black, 320, i*100+100)
    pygame.display.update()

#Main Game Loop
def startGame():
    turn = 1
    words = []
    word = set_word()
    while len(word)!=4:
        word=set_word()
    dispGame(turn, words)
    pygame.display.update()

    #'Turn' Loop
    while turn<11:
        letter = 1
        B = 0
        C = 0
        guess = ""
        submit = True
        sub = True
        erase = True

        #'Letter' Loop
        while submit:
            while erase:
                text("Erase", 50, black, 620, 950, font2)
                erase = False

            #Detect Certain Events Such As Mouse Motion And Mouse Clicks
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()

                #Underline The Alphabet That The Mouse Cursor Is Hovering On
                if event.type == MOUSEMOTION:
                    if event.pos[0]>30 and event.pos[0]<1070 and event.pos[1]>50 and event.pos[1]<100:
                        x = int((event.pos[0] - 30)/40)
                        pygame.draw.line(Canvas, white, (1, 90), (1099, 90), 2)
                        pygame.draw.line(Canvas, black, (x*40+25, 90), (x*40 + 60, 90), 2)
                        pygame.display.update()

                #Detect Click On Erase Button
                if event.type == MOUSEBUTTONDOWN:
                    if letter>1 and event.pos[0]>950 and event.pos[0]<1070 and event.pos[1]>620 and event.pos[1]<670:
                        letter = letter - 1
                        guess = guess[0:-1]
                        updateguess(guess)
                        
                    #Detect Click On A Certain Alphabet
                    if event.pos[0]>30 and event.pos[0]<1070 and event.pos[1]>50 and event.pos[1]<100:
                        x = int((event.pos[0] - 30)/40)
                        string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                        if letter == 1:
                            guess = guess + string[x]
                            updateguess(guess)
                            letter = letter + 1
                        else:
                            #Avoid Any Alphabet From Being Re-entered
                            if string[x] in guess:
                                pass
                            else:
                                guess = guess + string[x]
                                updateguess(guess)
                                letter = letter + 1
                if letter == 5:
                    if sub:
                        text("Submit", 60, black, 550, 80, font2)
                        sub = False

                    #Detect Click On Submit Button And Exit The 'Letter' Loop
                    if event.type == MOUSEBUTTONDOWN:
                        if event.pos[0]>80 and event.pos[0]<270 and event.pos[1]>550 and event.pos[1]<600:
                            submit = False

        #Analysing The Input
        for i in range(4):
            if guess[i] in word:
                if word.index(guess[i]) == i:
                    B = B + 1
                else:
                    C = C + 1
                    
        #End Game If User Wins Else Restart
        if B == 4:
            return endGame(word, True, turn)
        else:
            turn = turn + 1
            words.append([guess, B, C])
            dispGame(turn, words)

    #End Game Once All 10 Turns Are Used Up
    return endGame(word, False, turn)

#Function To Display The End Game Screen
def endGame(word, result, turn):
    Canvas.fill(black)
    text("The required answer was", 50, white, 150, 200)
    text(word, 100, white, 225, 325)
    if result:
        text("Congratulations! You guessed the word correctly.", 50, white, 350, 200)
        text("Score: " + str(11 - turn), 75, white, 450, 320)
    else:
        text("Oops! You failed to guess the word correctly.", 50, white, 350, 200)
        text("Score : 0", 75, white, 450, 320)

    #To Detect 'Escape' Key Being Pressed And Restart The Game
    text("To play again, press Escape key.", 50, white, 550, 200)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True

#Main Function
text("Welcome to the Cow Bull Game", 60, white, 300, 160, font1, True)
text("Click to Start!", 40, white, 400, 400, font2)
waitforkey()
start = startGame()
while start:
    start = startGame()
