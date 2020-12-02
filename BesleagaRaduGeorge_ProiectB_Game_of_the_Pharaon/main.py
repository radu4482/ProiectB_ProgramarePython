from GamePhysics import *
from graphics import *

a = 0
score = 0
lifes = 3
clear = lambda: os.system('cls')

while True:
    a += 1
    if lifes <0 or a==6:
        print("Game over")
        break
    matrix(a)
    while GameStillOn():
        if lifes < 0: break
        paintMap()
        showScore(score,lifes)
        the_score, lifes = move(choose(), lifes)
        score += the_score
        updateMap()
finalScore(score)