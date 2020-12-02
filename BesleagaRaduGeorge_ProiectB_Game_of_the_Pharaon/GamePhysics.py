from MapSystem import *



def choose():
    ok = 0
    while ok == 0:
        pointX = win.getMouse()
        point1Y = int((pointX.x.__int__() - 75) / 50)
        point1X = int((pointX.y.__int__() - 25) / 50)
        if Mapa[point1X][point1Y] != 0:
            ok = 1
        else:
            print("Try again!")
    return [point1X, point1Y]


def kill(row, column, color):
    if Mapa[row][column] == color:
        score = 1
        Mapa[row][column] = 0
        if row > 0:
            score += kill(row - 1, column, color)
        if row < sizeX - 1:
            score += kill(row + 1, column, color)
        if column > 0:
            score += kill(row, column - 1, color)
        if column < sizeY - 1:
            score += kill(row, column + 1, color)
    else:
        score = 0
    return score


def move(the_move, lifes):
    score = kill(the_move[0], the_move[1], Mapa[the_move[0]][the_move[1]])
    if score == 1: lifes -= 1
    return score, lifes


def updateMap():
    for column in range(0, sizeY):
        updateColumns(column)
    updateRows()


def updateRows():
    for i in range(0, 7):
        if columnEmpty(i) == True:
            for j in range(i, 0, -1):
                swapColumns(j, j - 1)


def swapColumns(column1, column2):
    for row in range(0, 8):
        aux = Mapa[row][column1]
        Mapa[row][column1] = Mapa[row][column2]
        Mapa[row][column2] = aux


def columnEmpty(row):
    for column in range(0, 8):
        if Mapa[column][row] != 0:
            return False
    return True


def updateColumns(row):
    ok = 0
    while ok == 0:
        aux = 0
        for i in reversed(range(0, 8)):
            if Mapa[i][row] == 0:
                aux = i
                break

        if aux != 0:
            ok = 1
            for i in range(0, aux):
                if Mapa[i][row] != 0:
                    ok = 0
                    break
            if ok == 0:
                shiftColumn(aux, row)
        else:
            ok = 1


def shiftColumn(index, row):
    for i in reversed(range(0, index + 1)):
        Mapa[i][row] = Mapa[i - 1][row]
    Mapa[0][row] = 0


def showScore(score, lifes):
    if lifes>0:
        for i in range(0,lifes):
            hearts=Image(Point(100+i*50,465),"forme/heart32.png")
            hearts.draw(win)
    # text = Text(Point(150, 475), "Nr of lifes:" + str(lifes))
    # text.setTextColor('yellow')
    # text.draw(win)
    # text = Text(Point(250, 475), "The score:" + str(score))
    # text.setTextColor('yellow')
    # text.draw(win)


def finalScore(score):
    win = GraphWin("TheScore", 200, 100)
    text = Text(Point(100, 50), "The score:" + str(score))
    text.setTextColor('black')
    text.draw(win)

