Test = [0,3, 2, 6, 0, 7, 54, 3, 0, 8, 6]


def algTest(lista):
    ok = 0
    while ok == 0:
        print(lista)
        aux = 0
        for i in reversed(range(0, len(lista))):
            if lista[i] == 0:
                aux = i
                break
        if aux != 0:
            ok = 1
            for i in range(0, aux):
                if lista[i] != 0:
                    ok = 0
                    break
            if ok == 0:
                lista = shiftTest(lista, aux)
        else:
            ok = 1
    return lista


def shiftTest(lista, index):
    for i in reversed(range(0,index+1)):
        lista[i]=lista[i-1]
    lista[0]=0
    return lista

print(algTest(Test))

