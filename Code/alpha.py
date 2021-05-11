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
#Estado de la celda. Muerta=0, Objetivo=1, Slider=2
#Creamos los objetivos
lista_Objetivos=[]
lista_Obstaculos=[]
for i in range(0,random.randrange(round((nxC*nyC)/10))):
    objetivo=ObjetivoSimple(random.randrange(nxC),random.randrange(nyC),0)
    lista_Objetivos.append(objetivo)
for i in range(0, random.randrange(round((nxC * nyC) / 10))):
    obstaculo = ObstaculoSimple(random.randrange(nxC), random.randrange(nyC), 0)
    lista_Obstaculos.append(obstaculo)

#Instanciar el slider
slider=Slider(3,3,3,1)
slider.celdasX = nxC
slider.celdasY = nyC
slider.colaX=slider.posicionEjeX[0]
slider.colaY=slider.posicionEjeY[0]
slider.posicionEjeX.append(3)
slider.posicionEjeY.append(2)
slider.posicionEjeX.append(3)
slider.posicionEjeY.append(1)
slider.posicionEjeX.append(3)
slider.posicionEjeY.append(0)

#Pintamos el slider
for i in range(0, slider.longitud):
    gameState[slider.posicionEjeX[i], slider.posicionEjeY[i]] = 2

#Pintamos los objetivo
for i in range(0, len(lista_Objetivos)):
    gameState[lista_Objetivos[i].posicionEjeX, lista_Objetivos[i].posicionEjeY] = 1
    slider.objetivos.append(lista_Objetivos[i])
#Pintamos los obstaculos
for i in range(0, len(lista_Obstaculos)):
    gameState[lista_Obstaculos[i].posicionEjeX, lista_Obstaculos[i].posicionEjeY] = 3
    slider.obstaculos.append(lista_Obstaculos[i])
#Flujo de ejecucion
#En desarrollo, para poder pararlo en un futuro
pauseEcpect=False
while True:

    #Bucle que gestiona el cierre de la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            
    #Para evitar cambios de forma secuencial, consiguiendo que todos los cambios
    newGameState=np.copy(gameState)

    # Añadir un tiempo de espera para que el programa vaya mas lento
    time.sleep(0.1)
    #Limpiamos la pantalla para que no se superponga los datos de la anterior iteracion
    screen.fill(bg)
    #Eventos de Teclado y raton
    ev=pygame.event.get()
    for event in ev:
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
        if slider.longitud > 1:
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
        newGameState[slider.colaX, slider.colaY] = 0
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

            pygame.draw.polygon(screen, (128, 128, 18), poly, 1)






    #Método que gestiona colisiones del slider con objetivos
    slider.objetivo_alcanzado()
            #Actualizamos el estado del juego
    gameState=np.copy(newGameState)
    #Actualizamos la pantalla
    
    
    
    pygame.display.flip()