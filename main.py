from GamePhysics import *
from graphics import *

a = 0
score = 0
lifes = 3
clear = lambda: os.system('cls')

while True:
    if lifes == 0:
        print("out of lifes")
        break
    a += 1
    matrix(a)
    while GameStillOn():
        if lifes == 0: break
        paintMap()
        showScore(score,lifes)
        the_choose = choose()
        the_score, lifes = move(the_choose, lifes)
        score += the_score
        updateMap()
