import pygame
import numpy as np
import time
import keyboard as kb
from objetivo import ObjetivoSimple
#Importamos los elementos que necesia nuestro programa

#Crea la pantalla de nuestro juego
from sliders import Slider

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
#Creamos la estructura de datos para los estados de todas nuestras celdas
gameState=np.zeros((nxC,nyC))
#Estado de la celda. Muerta=0, Slider=1, Objetivo=2
#Creamos los objetivos
lista_Objetivos=[]
objetivo1=ObjetivoSimple()
objetivo1.constructor(1,1,0)
lista_Objetivos.append(objetivo1)
#Instanciar el slider
slider=Slider()
slider.constructor(2,2,1,1,1)


for i in range(0, slider.longitud):
    gameState[slider.posicionEjeX[i], slider.posicionEjeY[i]] = 1
#Flujo de ejecucion
pauseEcpect=False
while True:
    #Para evitar cambios de forma secuencial, consiguiendo que todos los cambios
    newGameState=np.copy(gameState)

    #Limpiamos la pantalla para que no se superponga los datos de la anterior iteracion
    screen.fill(bg)
    #Añadir un tiempo de espera para que el programa vaya mas lento
    time.sleep(0.1)
    #Eventos de Teclado y raton

    ev=pygame.event.get()
    for event in ev:
        # Evento de teclado
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w or event.key==pygame.K_UP:
                newGameState[slider.posicionEjeX[i], slider.posicionEjeY[i]] = 0
                slider.cambiaDireccion("arriba")
                for i in range(0,slider.longitud):
                    newGameState[slider.posicionEjeX[i], slider.posicionEjeY[i]]=1
            elif event.key==pygame.K_s or event.key==pygame.K_DOWN:
                newGameState[slider.posicionEjeX[i], slider.posicionEjeY[i]] = 0
                slider.cambiaDireccion("abajo")
                for i in range(0,slider.longitud):
                    newGameState[slider.posicionEjeX[i], slider.posicionEjeY[i]]=1
            elif event.key==pygame.K_a or event.key==pygame.K_LEFT:
                newGameState[slider.posicionEjeX[i], slider.posicionEjeY[i]] = 0
                slider.cambiaDireccion("izquierda")
                for i in range(0,slider.longitud):
                    newGameState[slider.posicionEjeX[i], slider.posicionEjeY[i]]=1
            elif event.key==pygame.K_d or event.key==pygame.K_RIGHT:
                newGameState[slider.posicionEjeX[i], slider.posicionEjeY[i]] = 0
                slider.cambiaDireccion("derecha")
                for i in range(0,slider.longitud):
                    newGameState[slider.posicionEjeX[i], slider.posicionEjeY[i]]=1

    #Estos bucles sirven para dibujar las celdas del juego
    for y in range(0, nxC):
        for x in range(0, nyC):
            #Implementamos la condicion del control del flujo
            if not pauseEcpect:
                #Calculamos el numero de vecinos
                #Tenemos en cuenta los sucesos ne los bordes, la estrategia toroidal o pacman
                n_neigh=gameState[(x - 1)%nxC, (y - 1)%nyC] + \
                        gameState[(x)    %nxC, (y - 1)%nyC] + \
                        gameState[(x + 1)%nxC, (y - 1)%nyC] + \
                        gameState[(x - 1)%nxC, (y)    %nyC] + \
                        gameState[(x + 1)%nxC, (y)    %nyC] + \
                        gameState[(x - 1)%nxC, (y + 1)%nyC] + \
                        gameState[(x)    %nxC, (y + 1)%nyC] + \
                        gameState[(x + 1)%nxC, (y + 1)%nyC]


            #Creamos el poligono(En este caso cuadro) de cada celda a dibujar
            poly=[((x)   * dimCW, y * dimCH),
                  ((x+1) * dimCW, y * dimCH),
                  ((x+1) * dimCW, (y+1) * dimCH),
                  ((x)   * dimCW, (y+1) * dimCH)]
            pygame.draw.polygon(screen,(128,128,18),poly,1)

            #Dibujamos la celda por cada par de x e y
            if newGameState[x,y]==0:
                pygame.draw.polygon(screen, (128, 18, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
    #Actualizamos el estado del juego
    gameState=np.copy(newGameState)
    #Actualizamos la pantalla
    pygame.display.flip()