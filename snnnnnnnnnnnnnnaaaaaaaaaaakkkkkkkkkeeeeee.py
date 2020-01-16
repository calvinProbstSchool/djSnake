# ___________
# By Calvin Probst calvin.probst@gmail.com
# https://github.com/calvinProbstSchool/djSnake

import pygame
import pygame.sprite
import sys
from pygame.sprite import *

class SnakePart(Sprite):
    def __init__(self, boardX, boardY, dIn, dOut):
        Sprite.__init__(self)

        DIRUP = 0.5
        DIRRIGHT = 1
        DIRDOWN = -0.5
        DIRLEFT = -1

        imageFilename = "snake_body_"

        dirIn = dIn
        dirOut = dOut

        if dirIn == DIRDOWN:
            imageFilename = imageFilename + "D"
        elif dirIn == DIRLEFT:
            imageFilename = imageFilename + "L"
        elif dirIn == DIRUP:
            imageFilename = imageFilename + "U"
        elif dirIn == DIRRIGHT:
            imageFilename = imageFilename + "R"

        if dirOut == DIRDOWN:
            imageFilename = imageFilename + "D.png"
        elif dirOut == DIRLEFT:
            imageFilename = imageFilename + "L.png"
        elif dirOut == DIRUP:
            imageFilename = imageFilename + "U.png"
        elif dirOut == DIRRIGHT:
            imageFilename = imageFilename + "R.png"

        return pygame.image.load(imageFilename)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

OGWINSIZE = 500
WINDOWSIZEX = 500
WINDOWSIZEY = 500
BORDER = 0.1
BOARDSIZE = 20
XBOXSIZE = (WINDOWSIZEX * (1 - (BORDER * 2))) / BOARDSIZE
YBOXSIZE = (WINDOWSIZEY * (1 - (BORDER * 2))) / BOARDSIZE
FONTSIZE = int(WINDOWSIZEX / 50)

FPS = 30
DIRUP = 0.5
DIRRIGHT = 1
DIRDOWN = -0.5
DIRLEFT = -1


def main():
    global DISPLAYSURF, SNAKEFONT, WINDOWSIZEX, WINDOWSIZEY, BOARDSIZE, BORDER, XBOXSIZE, YBOXSIZE, FONTSIZE, FPSCLOCK, GAMEBOARD, HEADPOS

    pygame.init()

    FPSCLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((WINDOWSIZEX, WINDOWSIZEY), pygame.RESIZABLE)

    SNAKEFONT = pygame.font.Font("./alba.TTF", FONTSIZE)

    keyDir = DIRRIGHT

    snekPos = [(BOARDSIZE / 2, BOARDSIZE / 2)]
    HEADPOS = snekPos

    GAMEBOARD = []

    for y in range(BOARDSIZE):
        row = []
        for x in range(BOARDSIZE):
            row.append(False)
        board.append(row)

    GAMEBOARD[snekPos[1]][snekPos[0]] = True

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if not keyDir * -1 == DIRLEFT:
                        keyDir = DIRLEFT
                elif event.key == pygame.K_RIGHT:
                    if not keyDir * -1 == DIRRIGHT:
                        keyDir = DIRRIGHT
                elif event.key == pygame.K_UP:
                    if not keyDir * -1 == DIRUP:
                        keyDir = DIRUP
                elif event.key == pygame.K_DOWN:
                    if not keyDir * -1 == DIRLEFT:
                        keyDir = DIRLEFT
            if event.type == pygame.VIDEORESIZE:
                DISPLAYSURF = pygame.display.set_mode((event.w, event.h),
                                                  pygame.RESIZABLE)
                WINDOWSIZEX = event.w
                WINDOWSIZEY = event.h

                XBOXSIZE = (WINDOWSIZEX * (1 - (BORDER * 2))) / BOARDSIZE
                YBOXSIZE = (WINDOWSIZEY * (1 - (BORDER * 2))) / BOARDSIZE

        drawGame((0,0), 0, (0, 0))

        newSquare = getBoxInDir(HEADPOS[0], HEADPOS[1], keyDir)
        if newSquare[1] == -1 or newSquare[0] == -1:
            gameLose()
        elif GAMEBOARD[newSquare[1]][newSquare[0]]:
            gameLose()
        else:
            GAMEBOARD[newSquare[1]][newSquare[0]] = True
            HEADPOS = newSquare
            snekPos.append(HEADPOS)


def gameLose():



def getBoxInDir(x, y, dir):
    global BOARDSIZE

    xnew = x
    ynew = y

    if dir == DIRDOWN:
        ynew = ynew + 1
    elif dir == DIRUP:
        ynew = ynew - 1
    elif dir == DIRRIGHT:
        xnew = xnew + 1
    elif dir == DIRLEFT:
        xnew = xnew - 1
    if (xnew < 0 or ynew < 0) or (xnew >= BOARDSIZE or ynew >= BOARDSIZE):
        return (-1, -1)
    return (xnew, ynew)


def drawGame(snekPoss, score, aaplPos):
    global DISPLAYSURF, SNAKEFONT, FPSCLOCK, FPS, HEADPOS, OGWINSIZE, WINDOWSIZEX, WINDOWSIZEY, BORDER, SNAKEFONT, YBOXSIZE, XBOXSIZE

    pygame.draw.rect(DISPLAYSURF, GREEN, (((WINDOWSIZEX * BORDER), (WINDOWSIZEY * BORDER)), ((WINDOWSIZEX * (1 - BORDER * 2)), (WINDOWSIZEY * (1 - BORDER * 2)))))

    pygame.display.update()
    FPSCLOCK.tick(FPS)

    DISPLAYSURF.fill(BLACK)

    for i in range(len(snekPoss)):
        if i == 0:
            pygame.draw

main()