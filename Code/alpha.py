import pygame
import numpy as np
import random
import time
import keyboard as kb
from objetivo import ObjetivoSimple
from obstaculo import ObstaculoSimple
from sliders import Slider
import sys


pygame.init()
#Configuramos las dimensiones de la pantalla
width,height=600,600
screen=pygame.display.set_mode((height,width))
#Congiguramos el color de fondo
#Con una intensidad los canales de color(Para formar colores en funcion de los primarios)
bg=25,25,25
#Cambiamos el color de fondo por el elegido
screen.fill(bg)
#Numero de celdas en los ejes x e y
nxC,nyC=10,10
#Dimensiones de las celdas en funcion del numero y cantidad de las mismas
dimCW=width/nxC
dimCH=height/nyC
#Iniciamos todas las celdas del juego con un valor de 0, es decir, muerta.
gameState=np.zeros((nyC,nxC))
#Instanciamos el marcador
score=0
highScore=0
fuente=pygame.font.SysFont("Arial",30)
puntuacion=fuente.render("Score: "+str(score)+"      High Score: "+ str(highScore),0,(255,255,255))
while True:
    #Estado de la celda. Muerta=0, Objetivo=1, Slider=2
    #Instanciar el slider
    slider=Slider(nxC//2,nyC//2,2,1)
    slider.celdasX = nxC
    slider.celdasY = nyC
    slider.posicionEjeX.append(slider.posicionEjeX[0]-1)
    slider.posicionEjeY.append(slider.posicionEjeY[0])
    linicial=slider.longitud
    #Pintamos el slider
    for i in range(0, slider.longitud):
        gameState[slider.posicionEjeX[i], slider.posicionEjeY[i]] = 2

    #Creamos los objetivos
    lista_Objetivos=[]

    lista_Obstaculos=[]

    for obj in range((nxC*nyC)//10):
        verificarCordenada=True
        while verificarCordenada:
            ejeX = random.randrange(nxC)
            ejeY = random.randrange(nyC)
            if len(lista_Objetivos)==0:
                contador = 0
                for s in range(slider.longitud):
                    if ejeX!=slider.posicionEjeX[s] or ejeY!=slider.posicionEjeY[s]:
                        contador+=1
                if contador==slider.longitud:
                    lista_Objetivos.append(ObjetivoSimple(ejeX, ejeY))
                    verificarCordenada = False
                    gameState[lista_Objetivos[obj].posicionEjeX, lista_Objetivos[obj].posicionEjeY] = 1
            else:
                for s in range(slider.longitud):
                    contador = 0
                    for objz in range(len(lista_Objetivos)):
                        if (ejeX!=slider.posicionEjeX[s] or ejeY!=slider.posicionEjeY[s]) and (ejeX!=lista_Objetivos[objz].posicionEjeX or ejeY!=lista_Objetivos[objz].posicionEjeY):
                          contador+=1
                if contador == len(lista_Objetivos):
                    lista_Objetivos.append(ObjetivoSimple(ejeX, ejeY))
                    verificarCordenada = False
                    gameState[lista_Objetivos[obj].posicionEjeX, lista_Objetivos[obj].posicionEjeY] = 1

    for obs in range((nxC*nyC)//10):
        verificarCordenada=True
        while verificarCordenada:
            ejeX = random.randrange(nxC)
            ejeY = random.randrange(nyC)
            if len(lista_Obstaculos)==0:
                contador = 0
                for s in range(slider.longitud):
                    for obj in range(len(lista_Objetivos)):
                        if (ejeX!=slider.posicionEjeX[s] or ejeY!=slider.posicionEjeY[s]) and (ejeX!=lista_Objetivos[obj].posicionEjeX or ejeY!=lista_Objetivos[obj].posicionEjeY):
                            contador+=1
                if contador==(slider.longitud*len(lista_Objetivos)):
                    lista_Obstaculos.append(ObjetivoSimple(ejeX, ejeY))
                    verificarCordenada = False
                    gameState[lista_Obstaculos[obs].posicionEjeX, lista_Obstaculos[obs].posicionEjeY] = 3
            else:
                for s in range(slider.longitud):
                    contador = 0
                    for obj in range(len(lista_Objetivos)):
                        for obsz in range(len(lista_Obstaculos)):
                            if (ejeX!=slider.posicionEjeX[s] or ejeY!=slider.posicionEjeY[s]) \
                                    and (ejeX!=lista_Objetivos[objz].posicionEjeX or ejeY!=lista_Objetivos[objz].posicionEjeY) \
                                    and (ejeX!=lista_Obstaculos[obsz].posicionEjeX or ejeY!=lista_Obstaculos[obsz].posicionEjeY):
                                contador+=1
                if contador == len(lista_Objetivos):
                    lista_Obstaculos.append(ObstaculoSimple(ejeX, ejeY))
                    verificarCordenada = False
                    gameState[lista_Obstaculos[obs].posicionEjeX, lista_Obstaculos[obs].posicionEjeY] = 3


    slider.objetivos=lista_Objetivos
    slider.obstaculos=lista_Obstaculos
    #Flujo de ejecucion
    #En desarrollo, para poder pararlo en un futuro
    pauseEcpect=False
    while True:
        # Para evitar cambios de forma secuencial, consiguiendo que todos los cambios
        newGameState = np.copy(gameState)
        # Añadir un tiempo de espera para que el programa vaya mas lento
        time.sleep(0.1)
        #Limpiamos la pantalla para que no se superponga los datos de la anterior iteracion
        screen.fill(bg)
        #Eventos de Teclado y raton
        ev=pygame.event.get()
        for event in ev:
            #Evento de cierre de ventana mediante raton
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Evento de teclado
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pauseEcpect=not  pauseEcpect
                #Filtramos de todas las teclas del teclado las que nos interesa para movernos(w,a,s,d,flechitas)
                #Teclas W y Up
                if event.key==pygame.K_w or event.key==pygame.K_UP:
                    if slider.direccion!="arriba" and slider.direccion!="abajo":
                        slider.direccion="arriba"
                #Teclas S y Down
                elif event.key==pygame.K_s or event.key==pygame.K_DOWN:
                    if slider.direccion != "abajo" and slider.direccion!="arriba":
                        slider.direccion="abajo"
                #Teclas A y Left
                elif event.key==pygame.K_a or event.key==pygame.K_LEFT:
                    if slider.direccion != "izquierda" and slider.direccion!="derecha":
                        slider.direccion="izquierda"
                #Teclas D y Right
                elif event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                    if slider.direccion != "derecha" and slider.direccion!="izquierda":
                        slider.direccion="derecha"

        # Automatizamos la direccion, para que el slider siga con la direccion establecida
        if slider.direccion != "ninguna":
            newGameState[slider.posicionEjeX[0], slider.posicionEjeY[0]] = 0
            slider.cambiaDireccion(0, slider.direccion)
            newGameState[slider.posicionEjeX[0], slider.posicionEjeY[0]] = 2
            if slider.estado == 0:
                break
            else:
                if slider.longitud > 1 and slider.estado!=0:
                    varX = 0
                    varY = 0
                    for i in range(1, slider.longitud):
                        newGameState[slider.posicionEjeX[i], slider.posicionEjeY[i]] = 0
                        varX = slider.posicionEjeX[i]
                        varY = slider.posicionEjeY[i]
                        slider.posicionEjeX[i] = slider.colaX
                        slider.posicionEjeY[i] = slider.colaY
                        newGameState[slider.posicionEjeX[i], slider.posicionEjeY[i]] = 2
                        slider.colaX = varX
                        slider.colaY = varY
                slider.colaX = slider.posicionEjeX[0]
                slider.colaY = slider.posicionEjeY[0]


        # Dibujamos el tablero
        for y in range(0, nxC):
            for x in range(0, nyC):
                # if not pauseEcpect:
                # Creamos los cuadrados de cada celda a dibujar
                poly = [((x) * dimCW, y * dimCH),
                        ((x + 1) * dimCW, y * dimCH),
                        ((x + 1) * dimCW, (y + 1) * dimCH),
                        ((x) * dimCW, (y + 1) * dimCH)]
                # Dibujamos la celda por cada par de x e y
                # Celda muerta
                if newGameState[x, y] == 0:
                    pygame.draw.polygon(screen, (128, 18, 128), poly, 1)
                # Objetivo
                elif newGameState[x, y] == 1:
                    pygame.draw.polygon(screen, (0, 255, 0), poly, 0)
                # Slider
                elif newGameState[x, y] == 2:
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
                else:
                    pygame.draw.polygon(screen, (255, 0, 0), poly, 0)
        #Actualizamos la puntuacion
        if slider.longitud!=linicial:
            score=slider.longitud-linicial
            if score>highScore:
                highScore=score
            puntuacion=fuente.render("Score: "+str(slider.longitud-linicial)+"      High Score: "+ str(highScore),0,(255,255,255))

        screen.blit(puntuacion, (65, 40))
        #Actualizamos el estado del juego
        gameState=np.copy(newGameState)
        #Actualizamos la pantalla
        pygame.display.flip()
    print("ESTAS......!!!!!")
    print("MUERTO!!!!!")
    print("MUERTO!!!!!")
    print("MUERTO!!!!!")
    print("puto gilipollas")
    score=0
    puntuacion=fuente.render("Score: "+str(slider.longitud-linicial)+"      High Score: "+ str(highScore),0,(255,255,255))
    gameState=np.zeros((nyC,nxC))