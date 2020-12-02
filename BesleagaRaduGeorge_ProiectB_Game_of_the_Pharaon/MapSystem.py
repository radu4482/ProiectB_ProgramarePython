import random
from graphics import *

win = GraphWin("My Game", 500, 500)
win.setBackground('black')
Mapa = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
culori = ['black', 'red', 'cyan', 'yellow', 'green', 'orange']
forme = ["forme/red.png","forme/cyan.png","forme/yellow.png","forme/green.png","forme/purple.png"]
sizeX = 8
sizeY = 7


def matrix(level):
    for i in range(0, 8):
        for j in range(0, 7):
            Mapa[i][j] = random.randint(1, level + 1)

def paintMap():
    gameBackground = Image(Point(250, 250), "forme/piramide.gif")
    gameBackground.draw(win)
    background = Rectangle(Point(73, 23), Point(427, 427))
    background.setFill('black')
    background.draw(win)
    for i in range(0, sizeX):
        for j in range(0, sizeY):
            formia=Mapa[i][j]-1
            if formia>=0:
                cir=Image(Point(j*50+100,i*50+50),forme[Mapa[i][j]-1])
                cir.draw(win)


def GameStillOn():
    for i in Mapa:
        for j in i:
            if j != 0:
                return True
    return False