import pygame
import numpy as np
import time
#Crea la pantalla de nuestro juego
pygame.init()
#Configuramos las dimensiones de la pantalla
width,height=600,600
#Congiguramos el color de fondo
screen=pygame.display.set_mode((height,width))
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
#Estado de la celda. Viva=1, Muerta=0
gameState=np.zeros((nxC,nyC))
#Inicializar un automata, o elemento predefinido
gameState=np.zeros((nxC,nyC))
#Automata Palo
gameState[0,0]=1
gameState[0,1]=1
gameState[0,2]=1
#Automata Movil
'''gameState[21,21]=1
gameState[22,22]=1
gameState[22,23]=1
gameState[21,23]=1
gameState[20,23]=1'''

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
    #Evento de teclado
    #Evento del Espacio
    ev=pygame.event.get()
    for event in ev:
        if event.type==pygame.KEYDOWN:
            pauseEcpect=not  pauseEcpect
        mouseClick=pygame.mouse.get_pressed()
        #Nos debuelve un vector de tres valores
        #print(mouseClick)
        #Si clicamos, nos devuelve un valor superior a 0
        if sum(mouseClick)>0:
            #Obtenemos la posicion del eje x e y de lo pulsado
            posX,posY=pygame.mouse.get_pos()
            #Obtenemos la celda en relacion con las dimensiones
            celX,celY=int(np.floor(posX/dimCW)),int(np.floor(posY/dimCH))
            #Cambiamos el estado de la celda a "viva"
            #newGameState[celX,celY]=1
            #Cambiamos el estado de la celda si pulso el boton izquierdo del raton =0 y si pulso cualquier otro =1
            newGameState[celX, celY] = not mouseClick[2]
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
                #Rule 1:Una celula muerta con exactamente 3 vecinas vivas"revives"
                if gameState[x,y]==0 and n_neigh==3:
                    newGameState[x,y]=1
                # Rule 2:Una celula viva con menos de 2 o mas de 3 vecina vivas,"muere"
                elif gameState[x, y] == 1 and (n_neigh <2 or n_neigh>3):
                    newGameState[x, y] = 0
            #Creamos el poligono(En este caso cuadro) de cadda celda a dibujar
            poly=[((x)   * dimCW, y * dimCH),
                  ((x+1) * dimCW, y * dimCH),
                  ((x+1) * dimCW, (y+1) * dimCH),
                  ((x)   * dimCW, (y+1) * dimCH)]
            pygame.draw.polygon(screen,(128,128,18),poly,1)
            #Dibujamos la celda por cada par de x e y
            if newGameState[x,y]==0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
    #Actualizamos el estado del juego
    gameState=np.copy(newGameState)
    #Actualizamos la pantalla
    pygame.display.flip()