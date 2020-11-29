import random

from graphics import *

win = GraphWin("My Game", 500, 500)
win.setBackground('black')
Mapa = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
culori = ['black', 'red', 'cyan', 'yellow', 'green', 'orange']

sizeX=8
sizeY=7

def matrix(level):
    for i in range(0,8):
        for j in range(0,7):
            Mapa[i][j]=random.randint(1,level+1)
    print(Mapa)


def paintMap():
    for i in range(0, sizeX):
        for j in range(0, sizeY):
            cir = Rectangle(Point(j * 50+5, i* 50+5), Point(j* 50+55, i* 50+55))
            cir.setFill(culori[Mapa[i][j]])
            cir.draw(win)


def choose():
    ok = 0
    while ok == 0:
        print("First Choose:")
        pointX = win.getMouse()
        point1Y = int((pointX.x.__int__() - 5) / 50)
        point1X = int((pointX.y.__int__() - 5) / 50)
        if Mapa[point1X][point1Y] != 0:
            ok = 1
        else:
            print("Try again!")
    return [point1X, point1Y]


def kill(x, y, color):
    score=1
    Mapa[x][y] = 0
    if x > 0:
        if Mapa[x - 1][y] == color: score+=kill(x - 1, y, color)
    if x < sizeX-1:
        if Mapa[x + 1][y] == color: score+=kill(x + 1, y, color)
    if y > 0:
        if Mapa[x][y - 1] == color: score+=kill(x, y - 1, color)
    if y < sizeY-1:
        if Mapa[x][y + 1] == color: score+=kill(x, y + 1, color)
    return score


def move(the_move):
    score=kill(the_move[0], the_move[1], Mapa[the_move[0]][the_move[1]])


def updateMap():
    for i in range(0, sizeY):
        updateColumns(i)
    #updateRows()

def updateRows():
    for i in range(0,7):
        if rowEmpty(i)==True :
            for j in range(i,0,-1):
                swapRows(j,j-1)

def swapRows(row1,row2):
    print(row1,row2)
    for i in range(0,8):
        aux=Mapa[i][row1]
        Mapa[i][row1]=Mapa[i][row2]
        Mapa[i][row2]=aux

def rowEmpty(index):
    for i in range(0,8):
        if Mapa[i][index]!=0:
            return False
    return True

def updateColumns(row):
    ok=0
    while ok==0:
        print(Mapa)
        aux=0
        for i in reversed(range(0,8)):
            if Mapa[i][row]==0:
                aux=i
                break

        if aux!=0:
            ok = 1
            for i in range(0, aux):
                if Mapa[i][row] != 0:
                    ok = 0
                    break
            if ok==0:
                shiftColumn(aux,row)
        else: ok=1

def shiftColumn(index,row):
    for i in reversed(range(0,index+1)):
        Mapa[i][row]=Mapa[i-1][row]
    Mapa[0][row]=0


a = 1
matrix(1)
while True:
    paintMap()
    the_choose = choose()
    move(the_choose)
    updateMap()
