# ___________
# By Calvin Probst calvin.probst@gmail.com
# https://github.com/calvinProbstSchool/djSnake

import pygame
import pygame.sprite
import sys
from pygame.sprite import *


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

OGWINSIZE = 500
WINDOWSIZEX = 500
WINDOWSIZEY = 500
BORDER = 0.1
XBORDER = BORDER * WINDOWSIZEX
YBORDER = BORDER * WINDOWSIZEY
BOARDSIZE = 20
XBOXSIZE = (WINDOWSIZEX * (1 - (BORDER * 2))) / BOARDSIZE
YBOXSIZE = (WINDOWSIZEY * (1 - (BORDER * 2))) / BOARDSIZE
FONTSIZE = int(WINDOWSIZEX / 50)

FPS = 10
DIRUP = 0.5
DIRRIGHT = 1
DIRDOWN = -0.5
DIRLEFT = -1


def main():
    global DISPLAYSURF, SNAKEFONT, WINDOWSIZEX, WINDOWSIZEY, BOARDSIZE, BORDER, XBOXSIZE, YBOXSIZE, FONTSIZE, FPSCLOCK, GAMEBOARD, HEADPOS, XBORDER, YBORDER

    pygame.init()

    FPSCLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((WINDOWSIZEX, WINDOWSIZEY), pygame.RESIZABLE)

    SNAKEFONT = pygame.font.Font("./alba.TTF", FONTSIZE)

    keyDir = DIRRIGHT

    snekPos = [((int(BOARDSIZE / 2)) - 1, int(BOARDSIZE / 2) - 1), ((int(BOARDSIZE / 2)) - 1, int(BOARDSIZE / 2)), (int(BOARDSIZE / 2), int(BOARDSIZE / 2))]
    HEADPOS = (int(BOARDSIZE / 2), int(BOARDSIZE / 2))

    GAMEBOARD = []

    for y in range(BOARDSIZE):
        row = []
        for x in range(BOARDSIZE):
            row.append(False)
        GAMEBOARD.append(row)

    GAMEBOARD[snekPos[0][1]][snekPos[0][0]] = True

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    keyDir = DIRLEFT
                elif event.key == pygame.K_RIGHT:
                    keyDir = DIRRIGHT
                elif event.key == pygame.K_UP:
                    keyDir = DIRUP
                elif event.key == pygame.K_DOWN:
                    keyDir = DIRLEFT
            if event.type == pygame.VIDEORESIZE:
                DISPLAYSURF = pygame.display.set_mode((event.w, event.h),
                                                  pygame.RESIZABLE)
                WINDOWSIZEX = event.w
                WINDOWSIZEY = event.h

                XBORDER = BORDER * WINDOWSIZEX
                YBORDER = BORDER * WINDOWSIZEY

                XBOXSIZE = int((WINDOWSIZEX * (1 - (BORDER * 2))) / BOARDSIZE)
                YBOXSIZE = int((WINDOWSIZEY * (1 - (BORDER * 2))) / BOARDSIZE)

        drawGame(snekPos, 0, (0, 0))

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
    print("loser")
    exit()


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


def getSnakeImage(dIn, dOut, head=False):
    imageFilename = "snake_body_"
    if head:
        imageFilename = "snake_head_"

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


def getDirBoxes(box, relBox):
    global DIRLEFT, DIRRIGHT, DIRDOWN, DIRUP
    if relBox[0] > box[0]:
        return DIRRIGHT
    elif relBox[1] > box[1]:
        return DIRDOWN
    elif relBox[0] < box[0]:
        return DIRLEFT
    elif relBox[1] < box[1]:
        return DIRUP


def drawGame(snekPoss, score, aaplPos):
    global DISPLAYSURF, SNAKEFONT, FPSCLOCK, FPS, OGWINSIZE, WINDOWSIZEX, WINDOWSIZEY, BORDER, SNAKEFONT, YBOXSIZE, XBOXSIZE, XBORDER, YBORDER

    pygame.draw.rect(DISPLAYSURF, GREEN, (((WINDOWSIZEX * BORDER), (WINDOWSIZEY * BORDER)), ((WINDOWSIZEX * (1 - BORDER * 2)), (WINDOWSIZEY * (1 - BORDER * 2)))))

    DISPLAYSURF.fill(BLACK)


    for i in range(len(snekPoss)):
        if i == 0:
            d = getDirBoxes(snekPoss[i], snekPoss[i + 1])

            snekImage = getSnakeImage(d, d)

        elif i == len(snekPoss) - 1:
            d = getDirBoxes(snekPoss[i], snekPoss[i - 1])

            snekImage = getSnakeImage(d, d, True)
        else:
            dIn = getDirBoxes(snekPoss[i], snekPoss[i - 1])
            dOut = getDirBoxes(snekPoss[i], snekPoss[i + 1])

            snekImage = getSnakeImage(dIn, dOut)

        snekImage = pygame.transform.scale(snekImage, (XBOXSIZE, YBOXSIZE))

        xCoord = XBORDER + (XBOXSIZE * snekPoss[i][0])

        yCoord = YBORDER + (YBOXSIZE * snekPoss[i][1])

        print(str(snekPoss[i][0]) + ", " + str(snekPoss[i][1]))

        DISPLAYSURF.blit(snekImage, (xCoord, yCoord))


    snekPoss.remove(snekPoss[0])

    pygame.display.update()
    FPSCLOCK.tick(FPS)

main()