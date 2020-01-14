# ___________
# By Calvin Probst calvin.probst@gmail.com
# https://github.com/calvinProbstSchool/djSnake

import pygame
import pygame.sprite
import sys
from pygame.sprite import *

class SnakePart(Sprite):
    def __init__(self, boardX, boardY, imageFilename, dIn, dOut):
        Sprite.__init__(self)


        self.dirIn = dIn
        self.dirOut = dOut

        if

        self.image = pygame.image.load(imageFilename)
        self.rect = self.image.get_rect()

        self.bX = boardX
        self.bY = boardY

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 0, 255)
BLUE = (0, 255, 0)
RED = (255, 0, 0)


WINDOWSIZEX = 500
WINDOWSIZEY = 500
BOARDER = 0.1
BOARDSIZE = 20
XBOXSIZE = (WINDOWSIZEX - (BOARDER * 2)) / BOARDSIZE
YBOXSIZE = (WINDOWSIZEY - (BOARDER * 2)) / BOARDSIZE
FONTSIZE = int(WINDOWSIZEX / 50)


DIRUP = 0.5
DIRRIGHT = 1
DIRDOWN = -0.5
DIRLEFT = -1


def main():
    global DISPLAYSURF, SNAKEFONT, WINDOWSIZEX, WINDOWSIZEY, XBOXSIZE, YBOXSIZE, FONTSIZE
    DISPLAYSURF = pygame.display.set_mode((WINDOWSIZEX, WINDOWSIZEY), pygame.RESIZABLE)
    #SNAKEFONT = pygame.font.Font("./alba.TTF", FONTSIZE)
    keyDir = 0

    snekPos = [(BOARDSIZE / 2, BOARDSIZE / 2)]

    while True:

        keyPress = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    keyPress = True
                    keyDir = DIRLEFT
                elif event.key == pygame.K_RIGHT:
                    keyPress = True
                    keyDir = DIRRIGHT
                elif event.key == pygame.K_UP:
                    keyPress = True
                    keyDir = DIRUP
                elif event.key == pygame.K_DOWN:
                    keyPress = True
                    keyDir = DIRDOWN
            if event.type == pygame.VIDEORESIZE:
                DISPLAYSURF = pygame.display.set_mode((event.w, event.h),
                                                  pygame.RESIZABLE)
                WINDOWSIZEX = event.w
                WINDOWSIZEY = event.h

            print(str(keyDir))


def drawGame(snekPos, score, aaplPos):
    global DISPLAYSURF, SNAKEFONT



main()