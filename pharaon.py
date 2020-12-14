from GamePhysics import *

score = 0
lifes = 3
level=1

paintBackground()
paintGameFrame()
while True:
    a = level

    if lifes < 0:
        print("Game over")
        break
    if a > 4: a = 4

    matrix(a)
    showLifes(lifes)
    showLevel(level,getGraph())
    while GameStillOn():
        showScore(score,getGraph())
        if lifes < 0: break
        paintMap()
        result = move(choose(), lifes)
        score += result[0]
        updateMap()
        if lifes != result[1]:
            lifes = result[1]
            showLifes(lifes)
    level+=1

exitGame()
ok_score_table = finalScore(score)
ok_score_table.getMouse()