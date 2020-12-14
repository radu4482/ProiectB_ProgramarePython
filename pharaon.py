from GamePhysics import *
#initializam scorul ca fiind 0
score = 0
#initializam numarul de vieti cu 3
lifes = 3
#initializam levelul ca fiind 1
level=1

#in pagina cream un background specific temei
paintBackground()
#in pagina cream un "table" in vor fi incadrate piesele
paintGameFrame()

while True:
    #se va face de joc pana cand nu vor mai fi vieti de jucat
    if lifes < 0:
        print("Game over")
        break
    
    # termenul a este folosit pentru numarul de piese
    a = level
    if a > 4: a = 4
    
    #initializam matriea de piese cu a+1 elemente (maxim 5)
    matrix(a)
    #afisam numarul de vieti
    showLifes(lifes)
    #afisam levelul o data pe meci
    showLevel(level,getGraph())
    
    while GameStillOn():
        #in cazul in care nu mai exista vieti , se va iesi din bucla 
        if lifes < 0: break
            
        #afisam scorul curent
        showScore(score,getGraph())
        #se va repopula tabla de joc cu piesele din starea curenta
        paintMap()
        #se va executa o eliminare in lant bazata pe piesa aleasa de catre client,
        #de pe urma eliminari se va returna in variabila result pe prima pozitie 
        #scorul strans de pe urma numarul de piese eliminate si pe a doua , numarul de vieti 
        #ramase (in cazul in care se va alege o eliminare cu o singura piesa se va scade o viata)
        result = move(choose(), lifes)
        score += result[0]
        #piesele ramase vor cobor in jos pe coloana pana cand nu vor mai fi spatii goale
        updateMap()
        #in cazul in care se va pierde o viata, in variabila lifes se va corecta numarul 
        #de vieti si se vor reafisa acestea in joc
        if lifes != result[1]:
            lifes = result[1]
            showLifes(lifes)
    #cand se va termina nivelul , se va incrementa variabila level , crescand dificultatea
    level+=1
# in final , cand jocul s-a sfarsit, vom deschide o noua pagina cu scorul final
exitGame()
ok_score_table = finalScore(score)
ok_score_table.getMouse()
