from partida import Partida

'''
Esta clase es la encargada de poner todo en marcha(La partida, sus elementos y el funcionamiento y mecanicas de los mismos)
'''
lista_Puntuaciones=[]
highscore=0

def puntuaciones(partida):
    '''
    :param partida: El parametro partida contiene la puntuacion de la partida y el nivel al que ha llegado
    :return: El metodo no devuelve nada de manera explicita pero si que modifica las variables de clase "lista_Puntuaciones" y "highscore"
    '''
    contador=len(lista_Puntuaciones)
    #En funcion del nivel se le aplicara un bonus de pntuacion en base al nivel
    if partida.nivel=="facil":
        partida.score=partida.score*1.25
    if partida.nivel=="Medio":
        partida.score=partida.score*1.5
    if partida.nivel=="Dificil":
        partida.score=partida.score*3
    else:
        partida.score=partida.score*5

    # Esta condicion sirve para ordenar la lista de la mejor a la 5 mejor puntuacion
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
    '''
    Este es un bucle infinito que se encargara de iniciar partidas y mostrar la tabla de puntuaciones
    '''
    partida=Partida(600, 600, 50, 50)
    puntuaciones(partida)
    print("=======================================================")
    print("SCORES:            HIGHSCORE: "+str(lista_Puntuaciones[0].nombreJugador)+"---"+str(lista_Puntuaciones[0].score)+"---")
    print("")
    for i in range(len(lista_Puntuaciones)):
        print(str(i+1)+"º."+str(lista_Puntuaciones[i].nombreJugador)+"-----"+str(lista_Puntuaciones[i].score))
    print("=======================================================")
