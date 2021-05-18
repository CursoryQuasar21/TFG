
from partida import Partida




lista_Puntuaciones=[]
highscore=0

def puntuaciones(partida):
    contador=len(lista_Puntuaciones)
    if len(lista_Puntuaciones)==0:
        lista_Puntuaciones.append(partida)
    else:
        for i in lista_Puntuaciones:
            if i.score<partida.score:
                contador-=1
        if contador<5:
            lista_Puntuaciones.insert(contador, partida)
            if len(lista_Puntuaciones)>5:
                lista_Puntuaciones.pop()

while True:
    partida=Partida(600,600,50,50, highscore)
    puntuaciones(partida)
    print("=======================================================")
    print("SCORES:            HIGHSCORE: "+str(lista_Puntuaciones[0].nombreJugador)+"---"+str(lista_Puntuaciones[0].score)+"---")
    print("")
    for i in range(len(lista_Puntuaciones)):
        print(str(i+1)+"º."+str(lista_Puntuaciones[i].nombreJugador)+"-----"+str(lista_Puntuaciones[i].score))
    print("=======================================================")
