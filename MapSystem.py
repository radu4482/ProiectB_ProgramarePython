import random
from graphics import *

win = GraphWin("My Game", 500, 500)
win.setBackground('black')
Mapa = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

culori = ['black', 'red', 'cyan', 'yellow', 'green', 'orange']
forme = ["forme/red.png", "forme/cyan.png", "forme/yellow.png", "forme/green.png", "forme/purple.png"]
sizeX = 8
sizeY = 7


def matrix(level):
    for i in range(0, 8):
        for j in range(0, 7):
            Mapa[i][j] = random.randint(1, level + 1)


def getGraph():
    return win

def paintBackground():
    gameBackground = Image(Point(250, 250), "forme/piramide.gif")
    gameBackground.draw(win)


def paintGameFrame():
    setBlackBackground(73, 23,427, 427)
    setBlackBackground(0, 440,500, 500)

def setBlackBackground(x1,y1,x2,y2):
    background = Rectangle(Point(x1, y1), Point(x2, y2))
    background.setFill('black')
    background.draw(win)

def setWhiteText(x,y,theText):
    text = Text(Point(x, y), theText)
    text.setTextColor('white')
    text.draw(win)

def paintMap():
    for j in range(0, sizeY):
        for i in range(0, sizeX):
            formia = Mapa[i][j] - 1
            if formia > -1:
                cir = Image(Point(j * 50 + 100, i * 50 + 50), forme[Mapa[i][j] - 1])
                cir.draw(win)
            else:
                setBlackBackground(j * 50 + 75, i * 50 + 25, j * 50 + 125, i * 50 + 75)


def GameStillOn():
    for i in Mapa:
        for j in i:
            if j != 0:
                return True
    return False


def exitGame():
    win.close()


def paint():
    paintBackground()
    paintGameFrame()
    paintMap()
