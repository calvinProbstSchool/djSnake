# ___________
# By Calvin Probst calvin.probst@gmail.com
# https://github.com/calvinProbstSchool/djSnake

import pygame
import pygame.sprite
import sys
from pygame.sprite import *
import random


WHITE = (255, 255, 255)
BGBG = (50, 163, 105)
GREEN = (26, 154, 168)
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
FONTSIZE = int(WINDOWSIZEX / 10)

FPS = 10
FPSBASE = 10
DIRUP = 0.5
DIRRIGHT = 1
DIRDOWN = -0.5
DIRLEFT = -1


def main():
    global DISPLAYSURF, SNAKEFONT, WINDOWSIZEX, WINDOWSIZEY, BOARDSIZE, BORDER, XBOXSIZE, YBOXSIZE, FONTSIZE, FPSCLOCK, GAMEBOARD, HEADPOS, XBORDER, YBORDER, APPLEPOS, POWERUPPOS, FPSBASE

    pygame.init()

    FPSCLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((WINDOWSIZEX, WINDOWSIZEY), pygame.RESIZABLE)

    SNAKEFONT = pygame.font.Font("./alba.TTF", FONTSIZE)

    score = 0

    keyDir = DIRRIGHT

    movingInDir = DIRRIGHT

    snekPos = [((int(BOARDSIZE / 2)) - 1, int(BOARDSIZE / 2) - 1), ((int(BOARDSIZE / 2)) - 1, int(BOARDSIZE / 2)), (int(BOARDSIZE / 2), int(BOARDSIZE / 2))]
    HEADPOS = (int(BOARDSIZE / 2), int(BOARDSIZE / 2))
    APPLEPOS = (random.randint(0, 19), random.randint(0, 19))
    POWERUPPOS = APPLEPOS
    while POWERUPPOS == APPLEPOS:
        POWERUPPOS = (random.randint(0, 19), random.randint(0, 19))

    GAMEBOARD = []

    for y in range(BOARDSIZE):
        row = []
        for x in range(BOARDSIZE):
            row.append(False)
        GAMEBOARD.append(row)

    for point in snekPos:
        GAMEBOARD[point[1]][point[0]] = True

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if not keyDir == DIRRIGHT:
                        movingInDir = DIRLEFT
                elif event.key == pygame.K_RIGHT:
                    if not keyDir == DIRLEFT:
                        movingInDir = DIRRIGHT
                elif event.key == pygame.K_UP:
                    if not keyDir == DIRDOWN:
                        movingInDir = DIRUP
                elif event.key == pygame.K_DOWN:
                    if not keyDir == DIRUP:
                        movingInDir = DIRDOWN
                elif event.key == pygame.K_SPACE:
                    main2p()
            if event.type == pygame.VIDEORESIZE:
                DISPLAYSURF = pygame.display.set_mode((event.w, event.h),
                                                  pygame.RESIZABLE)
                WINDOWSIZEX = event.w
                WINDOWSIZEY = event.h

                XBORDER = BORDER * WINDOWSIZEX
                YBORDER = BORDER * WINDOWSIZEY

                XBOXSIZE = int((WINDOWSIZEX * (1 - (BORDER * 2))) / BOARDSIZE)
                YBOXSIZE = int((WINDOWSIZEY * (1 - (BORDER * 2))) / BOARDSIZE)

        drawGame(snekPos, str(score))

        newSquare = getBoxInDir(HEADPOS[0], HEADPOS[1], movingInDir)
        if newSquare[1] == -1 or newSquare[0] == -1:
            gameLose()
        elif GAMEBOARD[newSquare[1]][newSquare[0]]:
            gameLose()
        else:
            GAMEBOARD[newSquare[1]][newSquare[0]] = True
            HEADPOS = newSquare
            snekPos.append(HEADPOS)

        GAMEBOARD[snekPos[0][1]][snekPos[0][0]] = False

        keyDir = movingInDir
        if not newSquare == APPLEPOS and not newSquare == POWERUPPOS:
            snekPos.remove(snekPos[0])
        elif newSquare == APPLEPOS:
            APPLEPOS = (random.randint(0, 19), random.randint(0, 19))
            score += 1
            FPS = int((abs(10 * (45 - score / 45))) * FPSBASE)
        else:
            snekPos.remove(snekPos[0])
            POWERUPPOS = APPLEPOS
            while POWERUPPOS == APPLEPOS:
                POWERUPPOS = (random.randint(0, 19), random.randint(0, 19))
            FPSBASE = int(FPSBASE * 1.1)



def main2p():
    global DISPLAYSURF, SNAKEFONT, WINDOWSIZEX, WINDOWSIZEY, BOARDSIZE, BORDER, XBOXSIZE, YBOXSIZE, FONTSIZE, FPSCLOCK, GAMEBOARD, HEADPOS, XBORDER, YBORDER, APPLEPOS, POWERUPPOS, FPSBASE

    pygame.init()

    FPSCLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((WINDOWSIZEX, WINDOWSIZEY), pygame.RESIZABLE)

    SNAKEFONT = pygame.font.Font("./alba.TTF", FONTSIZE)

    score = 0
    score2 = 0

    keyDir1 = DIRRIGHT
    keyDir2 = DIRRIGHT
    movingInDir1 = DIRRIGHT
    movingInDir2 = DIRRIGHT

    snekPos = [((int(BOARDSIZE / 2)) - 1, int(BOARDSIZE / 2) - 1), ((int(BOARDSIZE / 2)) - 1, int(BOARDSIZE / 2)),
               (int(BOARDSIZE / 2), int(BOARDSIZE / 2))]
    snekPos2 = [((int(BOARDSIZE / 2)) - 1, int(BOARDSIZE / 2) - 5), ((int(BOARDSIZE / 2)) - 1, int(BOARDSIZE / 2) - 4),
               (int(BOARDSIZE / 2), int(BOARDSIZE / 2) - 4)]
    HEADPOS = (int(BOARDSIZE / 2), int(BOARDSIZE / 2))
    HEADPOS2 = (int(BOARDSIZE / 2), int(BOARDSIZE / 2) - 4)
    APPLEPOS = (random.randint(0, 19), random.randint(0, 19))
    POWERUPPOS = APPLEPOS
    while POWERUPPOS == APPLEPOS:
        POWERUPPOS = (random.randint(0, 19), random.randint(0, 19))

    GAMEBOARD = []

    for y in range(BOARDSIZE):
        row = []
        for x in range(BOARDSIZE):
            row.append(False)
        GAMEBOARD.append(row)

    for point in snekPos:
        GAMEBOARD[point[1]][point[0]] = True
    for point2 in snekPos2:
        GAMEBOARD[point2[1]][point2[0]] = True

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if not keyDir1 == DIRRIGHT:
                        movingInDir1 = DIRLEFT
                elif event.key == pygame.K_RIGHT:
                    if not keyDir1 == DIRLEFT:
                        movingInDir1 = DIRRIGHT
                elif event.key == pygame.K_UP:
                    if not keyDir1 == DIRDOWN:
                        movingInDir1 = DIRUP
                elif event.key == pygame.K_DOWN:
                    if not keyDir1 == DIRUP:
                        movingInDir1 = DIRDOWN
                if event.key == pygame.K_a:
                    if not keyDir2 == DIRRIGHT:
                        movingInDir2 = DIRLEFT
                elif event.key == pygame.K_d:
                    if not keyDir2 == DIRLEFT:
                        movingInDir2 = DIRRIGHT
                elif event.key == pygame.K_w:
                    if not keyDir2 == DIRDOWN:
                        movingInDir2 = DIRUP
                elif event.key == pygame.K_s:
                    if not keyDir2 == DIRUP:
                        movingInDir2 = DIRDOWN
                elif event.key == pygame.K_SPACE:
                    main()
            if event.type == pygame.VIDEORESIZE:
                DISPLAYSURF = pygame.display.set_mode((event.w, event.h),
                                                      pygame.RESIZABLE)
                WINDOWSIZEX = event.w
                WINDOWSIZEY = event.h

                XBORDER = BORDER * WINDOWSIZEX
                YBORDER = BORDER * WINDOWSIZEY

                XBOXSIZE = int((WINDOWSIZEX * (1 - (BORDER * 2))) / BOARDSIZE)
                YBOXSIZE = int((WINDOWSIZEY * (1 - (BORDER * 2))) / BOARDSIZE)

        drawGame(snekPos, str(score), snekPos2, str(score2))

        newSquare = getBoxInDir(HEADPOS[0], HEADPOS[1], movingInDir1)
        if newSquare[1] == -1 or newSquare[0] == -1:
            gameLose()
        elif GAMEBOARD[newSquare[1]][newSquare[0]]:
            gameLose()
        else:
            GAMEBOARD[newSquare[1]][newSquare[0]] = True
            HEADPOS = newSquare
            snekPos.append(HEADPOS)

        newSquare2 = getBoxInDir(HEADPOS2[0], HEADPOS2[1], movingInDir2)
        if newSquare2[1] == -1 or newSquare2[0] == -1:
            gameLose()
        elif GAMEBOARD[newSquare2[1]][newSquare2[0]]:
            gameLose()
        else:
            GAMEBOARD[newSquare2[1]][newSquare2[0]] = True
            HEADPOS2 = newSquare2
            snekPos2.append(HEADPOS2)

        GAMEBOARD[snekPos[0][1]][snekPos[0][0]] = False

        GAMEBOARD[snekPos2[0][1]][snekPos2[0][0]] = False

        keyDir2 = movingInDir2

        keyDir1 = movingInDir1
        if not newSquare == APPLEPOS and not newSquare == POWERUPPOS:
            snekPos.remove(snekPos[0])
        elif newSquare == APPLEPOS:
            APPLEPOS = (random.randint(0, 19), random.randint(0, 19))
            score += 1
            FPS = int((abs(10 * (45 - score / 45))) * FPSBASE)
        else:
            snekPos.remove(snekPos[0])
            POWERUPPOS = APPLEPOS
            while POWERUPPOS == APPLEPOS:
                POWERUPPOS = (random.randint(0, 19), random.randint(0, 19))
            FPSBASE = int(FPSBASE * 1.1)

        if not newSquare2 == APPLEPOS and not newSquare == POWERUPPOS:
            snekPos2.remove(snekPos2[0])
        elif newSquare2 == APPLEPOS:
            APPLEPOS = (random.randint(0, 19), random.randint(0, 19))
            score2 += 1
            FPS = int((abs(10 * (45 - score2 / 45))) * FPSBASE)
        else:
            snekPos2.remove(snekPos2[0])
            POWERUPPOS = APPLEPOS
            while POWERUPPOS == APPLEPOS:
                POWERUPPOS = (random.randint(0, 19), random.randint(0, 19))
            FPSBASE = int(FPSBASE * 1.1)

        for coord in snekPos:
            for coord2 in snekPos2:
                if coord == coord2:
                    gameLose()

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
    if xnew < 0 or xnew >= BOARDSIZE:
        return (-1, ynew)
    if ynew < 0 or ynew >= BOARDSIZE:
        return (xnew, -1)
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


def drawGame(snekPoss, score, snekPoss2=None, score2 = ""):
    global DISPLAYSURF, SNAKEFONT, FPSCLOCK, FPS, OGWINSIZE, WINDOWSIZEX, WINDOWSIZEY, BORDER, SNAKEFONT, YBOXSIZE, XBOXSIZE, XBORDER, YBORDER, APPLEPOS, POWERUPPOS

    DISPLAYSURF.fill(BGBG)

    pygame.draw.rect(DISPLAYSURF, GREEN,
                     (XBORDER, YBORDER, (WINDOWSIZEX - (2 * XBORDER)), (WINDOWSIZEY - (2 * YBORDER))))

    scoreCard = SNAKEFONT.render(str(score), True, RED)

    scoreCard2 = SNAKEFONT.render(str(score2), True, (0, 0, 0))

    DISPLAYSURF.blit(scoreCard, (0, 0))

    DISPLAYSURF.blit(scoreCard2, ((WINDOWSIZEX - scoreCard2.get_width()), 0))

    glassMeal = pygame.image.load("sanekFood.png")

    glassMeal = pygame.transform.scale(glassMeal, (XBOXSIZE, YBOXSIZE))

    xCoordApple = XBORDER + (XBOXSIZE * APPLEPOS[0])

    yCoordApple = YBORDER + (YBOXSIZE * APPLEPOS[1])

    DISPLAYSURF.blit(glassMeal, (xCoordApple, yCoordApple))

    powerUpSurf = glassMeal

    powerUpSurf.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    xCoordPower = XBORDER + (XBOXSIZE * POWERUPPOS[0])

    yCoordPower = YBORDER + (YBOXSIZE * POWERUPPOS[1])

    DISPLAYSURF.blit(glassMeal, (xCoordPower, yCoordPower))

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

    if not snekPoss2 is None:
        for i in range(len(snekPoss2)):
            if i == 0:
                d = getDirBoxes(snekPoss2[i], snekPoss2[i + 1])

                snekImage = getSnakeImage(d, d)

            elif i == len(snekPoss2) - 1:
                d = getDirBoxes(snekPoss2[i], snekPoss2[i - 1])

                snekImage = getSnakeImage(d, d, True)
            else:
                dIn = getDirBoxes(snekPoss2[i], snekPoss2[i - 1])
                dOut = getDirBoxes(snekPoss2[i], snekPoss2[i + 1])

                snekImage = getSnakeImage(dIn, dOut)

            snekImage = pygame.transform.scale(snekImage, (XBOXSIZE, YBOXSIZE))

            snekImage.set_alpha(128)

            xCoord = XBORDER + (XBOXSIZE * snekPoss2[i][0])

            yCoord = YBORDER + (YBOXSIZE * snekPoss2[i][1])

            print(str(snekPoss2[i][0]) + ", " + str(snekPoss2[i][1]))

            DISPLAYSURF.blit(snekImage, (xCoord, yCoord))

    pygame.display.update()
    FPSCLOCK.tick(FPS)

main()