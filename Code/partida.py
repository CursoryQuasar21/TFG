import random
import pygame
import time
import time
import sys
import numpy as np
import keyboard as kb

#modularizar, crear una clase, la clase partida va ha contener los elementos
from elemento import Elementos


class Partida():
    nxC = 0
    nyC = 0
    gameState=0
    score = 0
    nivel="facil"
    nombreJugador=""
    time=1
    elemento = 0
    #Creamos el constructor con todo lo que va ha intervenir en la partida
    def __init__(self, height, width, nxC, nyC, higscore):
        self.nxC = nxC
        self.nyC = nyC
        #self.nombreJugador=print(input("Introduce tu nombre, Jugador"))
        #nivel=print(int(input("Con que nivel quieres empezar:1-Facil 2-Medio 3-Dificil 4-Imposible")))
        nivel=4
        if nivel == 1:
            self.nivel = "facil"
            self.time = 0.15
        elif nivel == 2:
            self.nivel = "medio"
            self.time = 0.1
        elif nivel == 3:
            self.nivel = "dificil"
            self.time = 0.08
        elif nivel == 4:
            self.nivel = "imposible"
            self.time = 0.05

        self.gameState=np.zeros((nyC,nxC))
        self.elemento=Elementos(nxC,nyC,self.nivel)
        self.partida(height, width, higscore)

    def partida(self, height, width, higscore):
        inicial=self.elemento.slider.longitud
        #
        #
        #Configuramos los ajustes de la pantalla
        pygame.init()
        # Configuramos las dimensiones de la pantalla
        screen = pygame.display.set_mode((height, width))
        # Dimensiones de las celdas en funcion del numero y cantidad de las mismas
        dimCW = width / self.nxC
        dimCH = height / self.nyC
        # Congiguramos el color de fondo
        # Con una intensidad los canales de color(Para formar colores en funcion de los primarios)
        bg = 25, 25, 25
        # Cambiamos el color de fondo por el elegido
        screen.fill(bg)
        # Añadimos una fuente para

        #
        #
        #Configuramos los elementos a nivel visual de la partida
        #Pintamos los objetivos
        for i in range(len(self.elemento.lista_Objetivos)):
            self.gameState[self.elemento.lista_Objetivos[i].posicionEjeX, self.elemento.lista_Objetivos[i].posicionEjeY] = 1
        #Pintamos la slider
        for i in range(self.elemento.slider.longitud):
            self.gameState[self.elemento.slider.posicionEjeX[i], self.elemento.slider.posicionEjeY[i]] = 2
        #Pintamos los obstaculos
        for i in range(len(self.elemento.lista_Obstaculos)):
            self.gameState[self.elemento.lista_Obstaculos[i].posicionEjeX, self.elemento.lista_Obstaculos[i].posicionEjeY] = 3
        #
        #
        # Configuramos las variable clave como el estado de la partida
        partida = True
        pause = True
        #Iniciamos la partida, en un principio pausada hasta que el jugador toque por primera vez una tecla cualquiera
        while partida:
            # Para evitar cambios de forma secuencial, consiguiendo que todos los cambios
            newGameState = np.copy(self.gameState)
            # Añadir un tiempo de espera para que el programa vaya mas lento
            if self.nivel=="facil":
                time.sleep(0.2)
            if self.nivel=="medio":
                time.sleep(0.1)
            if self.nivel=="dificil":
                time.sleep(0.08)
            if self.nivel=="imposible":
                time.sleep(0.05)

            # Limpiamos la pantalla para que no se superponga los datos de la anterior iteracion
            screen.fill(bg)
            # Eventos de Teclado y raton
            ev = pygame.event.get()
            for event in ev:
                # Evento de cierre de ventana mediante raton
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Evento de teclado
                if event.type == pygame.KEYDOWN:
                    #Pausar el juego en mantenimiento
                    #if event.key == pygame.K_SPACE or event.key == pygame.K_p:
                       #print("---MANTENIMIENTO---")
                    # Filtramos de todas las teclas del teclado las que nos interesa para movernos(w,a,s,d,flechitas)
                    # Teclas W y Up
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        if self.elemento.slider.direccion != "arriba" and self.elemento.slider.direccion != "abajo":
                            self.elemento.slider.direccion = "arriba"
                            pause=False
                    # Teclas S y Down
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        if self.elemento.slider.direccion != "abajo" and self.elemento.slider.direccion != "arriba":
                            self.elemento.slider.direccion = "abajo"
                            pause = False
                    # Teclas A y Left
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        if self.elemento.slider.direccion != "izquierda" and self.elemento.slider.direccion != "derecha":
                            self.elemento.slider.direccion = "izquierda"
                            pause = False
                    # Teclas D y Right
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        if self.elemento.slider.direccion != "derecha" and self.elemento.slider.direccion != "izquierda":
                            self.elemento.slider.direccion = "derecha"
                            pause = False
            #
            #
            #Autmatizamos los movimientos
            #Automatizamos la direccion de los objetivos

            for i in range(len(self.elemento.lista_Objetivos)):
                newGameState[self.elemento.lista_Objetivos[i].posicionEjeX, self.elemento.lista_Objetivos[i].posicionEjeY] = 0
                self.elemento.lista_Objetivos[i].cambiaDireccion(self.elemento.lista_Objetivos[i].direccion)
                newGameState[self.elemento.lista_Objetivos[i].posicionEjeX, self.elemento.lista_Objetivos[i].posicionEjeY] = 1
            # Automatizamos la direccion de los obstaculos
            for i in range(len(self.elemento.lista_Obstaculos)):
                newGameState[self.elemento.lista_Obstaculos[i].posicionEjeX, self.elemento.lista_Obstaculos[i].posicionEjeY] = 0
                self.elemento.lista_Obstaculos[i].cambiaDireccion(self.elemento.lista_Obstaculos[i].direccion)
                newGameState[self.elemento.lista_Obstaculos[i].posicionEjeX,self.elemento.lista_Obstaculos[i].posicionEjeY] = 3
            # Automatizamos la direccion del slider, para que siga con la direccion establecida
            self.elemento.slider.objetivos=self.elemento.lista_Objetivos
            self.elemento.slider.obstaculos = self.elemento.lista_Obstaculos
            if self.elemento.slider.direccion != "ninguna":
                newGameState[self.elemento.slider.posicionEjeX[0], self.elemento.slider.posicionEjeY[0]] = 0
                self.elemento.slider.cambiaDireccion(0, self.elemento.slider.direccion)
                newGameState[self.elemento.slider.posicionEjeX[0], self.elemento.slider.posicionEjeY[0]] = 2
                self.elemento.lista_Objetivos=self.elemento.slider.objetivos
                self.elemento.lista_Obstaculos = self.elemento.slider.obstaculos
                if self.elemento.slider.estado == 0:
                    partida=False
                else:
                    if self.elemento.slider.longitud > 1 and self.elemento.slider.estado != 0:
                        varX = 0
                        varY = 0
                        for i in range(1, self.elemento.slider.longitud):
                            newGameState[self.elemento.slider.posicionEjeX[i], self.elemento.slider.posicionEjeY[i]] = 0
                            varX = self.elemento.slider.posicionEjeX[i]
                            varY = self.elemento.slider.posicionEjeY[i]
                            self.elemento.slider.posicionEjeX[i] = self.elemento.slider.colaX
                            self.elemento.slider.posicionEjeY[i] = self.elemento.slider.colaY
                            newGameState[self.elemento.slider.posicionEjeX[i], self.elemento.slider.posicionEjeY[i]] = 2
                            self.elemento.slider.colaX = varX
                            self.elemento.slider.colaY = varY
                    self.elemento.slider.colaX = self.elemento.slider.posicionEjeX[0]
                    self.elemento.slider.colaY = self.elemento.slider.posicionEjeY[0]

            #
            #
            # Dibujamos el tablero
            for y in range(0, self.nxC):
                for x in range(0, self.nyC):
                    # Implementamos la condicion del control del flujo
                    #if not pause:
                        # Creamos los cuadrados de cada celda a dibujar
                        poly = [((x) * dimCW, y * dimCH),
                                ((x + 1) * dimCW, y * dimCH),
                                ((x + 1) * dimCW, (y + 1) * dimCH),
                                ((x) * dimCW, (y + 1) * dimCH)]
                        #
                        #
                        # Reglas basicas de cada elemento en el mapa
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
            # Actualizamos el estado del juego
            self.gameState = np.copy(newGameState)
            # Actualizamos la pantalla
            pygame.display.flip()
            if self.elemento.lista_Objetivos==0:
                self.elemento.creadorObjetivos()
        self.score=self.elemento.slider.longitud-inicial