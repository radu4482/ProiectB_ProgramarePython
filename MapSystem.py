import random
from graphics import *

win = GraphWin("My Game", 500, 500)
win.setBackground('black')
Mapa = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
culori = ['black', 'red', 'cyan', 'yellow', 'green', 'orange']

sizeX = 8
sizeY = 7


def matrix(level):
    for i in range(0, 8):
        for j in range(0, 7):
            Mapa[i][j] = random.randint(1, level + 1)


def paintMap():
    background = Rectangle(Point(150, 460), Point(300, 480))
    background.setFill('black')
    background.draw(win)
    for i in range(0, sizeX):
        for j in range(0, sizeY):
            cir = Rectangle(Point(j * 50 + 5, i * 50 + 5), Point(j * 50 + 55, i * 50 + 55))
            cir.setFill(culori[Mapa[i][j]])
            cir.draw(win)


def GameStillOn():
    for i in Mapa:
        for j in i:
            if j != 0:
                return True
    return False