import pygame
import time
import sys
import numpy as np

#modularizar, crear una clase, la clase partida va ha contener los elementos
from elemento import Elemento

class Partida():
    #Creamos el constructor con todo lo que va ha intervenir en la partida
    def __init__(self, height, width, nxC, nyC, nombre, nivel):
        '''
        :param height: La altura que va a tener la ventana
        :param width: La anchura que va a tener la ventana
        :param nxC: La cantidad de celdas en el ejeX
        :param nyC: La cantidad de celdas en el ejeY
        '''
        # Guardamos las celdas de los dos ejes
        self.nxC = nxC
        self.nyC = nyC

        # Inicializamos el nombre de usuario
        self.nombreJugador = nombre

        # Filtramos e inicializamos el nivel
        if nivel == 1:
            self.nivel = "facil"
        elif nivel == 2:
            self.nivel = "medio"
        elif nivel == 3:
            self.nivel = "dificil"
        else:
            self.nivel = "imposible"

        # Manejamos el timing del juego
        self.fps = pygame.time.Clock()

        # Creo y guardo una matriz poniendo todos los valores a cero
        self.gameState = np.zeros((nyC, nxC))

        # Creo todo tipo de elementos que se van a interferir en el juego
        self.elemento = Elemento(nxC,nyC,self.nivel)

        # Inicializamos el estado de la partida
        self.estado = True

        # Lanzamos el metodo que va a iniciar la partida
        self.partida(height, width)

    def dificultad(self,movimiento):
        '''
        :param movimiento: El parametro movimiento es el que determina si ha empezado la partida para el jugador
        :return: No devuelve nada de manera explicita, pero modifica el timing de la ejecucion
        '''
        if movimiento == True:
            if self.nivel == "facil":
                self.fps.tick(4)
            elif self.nivel == "medio":
                self.fps.tick(12)
            elif self.nivel == "dificil":
                self.fps.tick(16)
            elif self.nivel == "imposible":
                self.fps.tick(24)
        else:
            if self.nivel == "facil" or self.nivel == "medio":
                self.fps.tick(40)
            else:
                self.fps.tick(100)

    def inicializarMapa(self):
        '''
        :return: No devuelve nada de manera explicita, pero modifica los valores del atributo gamestate
        '''
        for i in self.elemento.lista_Objetivos:
            self.gameState[i.posicion[0], i.posicion[1]] = 1
        # Pintamos la slider
        for i in self.elemento.slider.posicion:
            self.gameState[i[0], i[1]] = 2
        # Pintamos los obstaculos
        for i in self.elemento.lista_Obstaculos:
            self.gameState[i.posicion[0], i.posicion[1]] = 3

    def actualizarMapa(self, movimiento, newGameState):
        # Automatizamos la direccion de los objetivos
        impacto = None
        contador = 0
        for i in self.elemento.lista_Objetivos:
            newGameState[i.posicion[0], i.posicion[1]] = 0
            self.elemento.lista_Objetivos[contador].cambiaDireccion()
            obj = self.elemento.lista_Objetivos[contador]
            newGameState[obj.posicion[0], obj.posicion[1]] = 1
            if obj.posicion == self.elemento.slider.posicion[0] and movimiento == True:
                objetivo_Impactado = contador
                impacto = True
            contador += 1

        if impacto != None:
            self.elemento.slider.objetivo_alcanzado(objetivo_Impactado)
        contador = 0
        # Automatizamos la direccion de los obstaculos
        for i in self.elemento.lista_Obstaculos:
            newGameState[i.posicion[0], i.posicion[1]] = 0
            self.elemento.lista_Obstaculos[contador].cambiaDireccion()
            obs = self.elemento.lista_Obstaculos[contador]
            newGameState[obs.posicion[0], obs.posicion[1]] = 3
            if obs.posicion == self.elemento.slider.posicion[0] and movimiento == True:
                self.estado = False
            contador += 1

        self.elemento.lista_Objetivos = self.elemento.slider.objetivos

        # Automatizamos la direccion del slider, para que siga con la direccion establecida
        if self.elemento.slider.direccion != "Ninguna" and self.elemento.slider.estado != 0:
            newGameState[self.elemento.slider.posicion[0][0], self.elemento.slider.posicion[0][1]] = 0
            self.elemento.slider.cambiaDireccion()
            newGameState[self.elemento.slider.posicion[0][0], self.elemento.slider.posicion[0][1]] = 2
            self.elemento.lista_Objetivos = self.elemento.slider.objetivos
            self.elemento.lista_Obstaculos = self.elemento.slider.obstaculos
            # Si la slider a chocado con un obstaculo, pasa de estar viva a muerta
            if self.elemento.slider.estado == 0:
                self.estado = False
            else:
                # Condicion si la slider tiene mas de una celda de longitud
                if self.elemento.slider.longitud > 1 and self.elemento.slider.estado != 0:
                    # Hacemos que todo el cuerpo de la slider siga a la cabeza
                    contador = 0
                    for i in self.elemento.slider.posicion:
                        if contador > 0:
                            # Se necesita variables arbitrarias que aislen el valor de la cola para que no apunten varios a la vez
                            colaX = self.elemento.slider.cola[0]
                            colaY = self.elemento.slider.cola[1]
                            newGameState[i[0], i[1]] = 0
                            varX = i[0]
                            varY = i[1]
                            self.elemento.slider.posicion[contador] = [colaX,colaY]
                            newGameState[self.elemento.slider.posicion[contador][0], self.elemento.slider.posicion[contador][1]] = 2
                            self.elemento.slider.cola[0] = varX
                            self.elemento.slider.cola[1] = varY
                        contador += 1
                self.elemento.slider.cola = self.elemento.slider.posicion[0]
        return newGameState

    def cambioNivel(self, newGameState):
        if len(self.elemento.lista_Objetivos) == 0:
            # Coindiciones que en funcione del nivel actual, determina el proximo nivel
            if self.nivel == "facil":
                self.nivel = "medio"
            elif self.nivel == "medio":
                self.nivel = "dificil"
            elif self.nivel == "dificil":
                self.nivel = "imposible"
            else:
                self.nivel = "imposible"

            self.elemento.lista_Objetivos = []
            self.elemento.lista_Obstaculos = []
            # Creamos de nuevo todos los obstaculos
            self.elemento.creadorObjetivos(self.nivel, self.nxC, self.nyC)
            if self.nivel == "imposible":
                self.elemento.creadorObstaculos(self.nivel, self.nxC, self.nyC)
            else:
                self.gameState = np.zeros((self.nyC, self.nxC))
                for i in self.elemento.slider.posicion:
                    newGameState[i[0], i[1]] = 2
                self.elemento.creadorObstaculos(self.nivel, self.nxC, self.nyC)
        return newGameState

    def partida(self, height, width):
        '''
        :param height: La altura que va a tener la ventana
        :param width: La anchura que va a tener la ventana
        :param highscore: La mejor puntuacion
        :return: No devuelve nada de manera explicita pero se lleva a cabo toda la partida y modifica ciertos atributos de clase
        '''
        # Guardamos en una veriable autilizar la longitud inicial
        inicial = self.elemento.slider.longitud
        #
        #
        # Configuramos los ajustes de la pantalla
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
        #
        #
        # Configuramos los elementos a nivel visual de la partida
        self.inicializarMapa()
        #
        #
        # Configuramos las variable clave como el estado de la partida
        pause = True
        # Iniciamos la partida, en un principio pausada hasta que el jugador toque por primera vez una tecla cualquiera
        v=True
        movimiento=False
        while self.estado:
            newGameState = np.copy(self.gameState)
            # Para evitar cambios de forma secuencial, consiguiendo que todos los cambios
            # Añadir un tiempo de espera para que el programa vaya mas lento
            self.dificultad(movimiento)
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
                    # Pausar el juego en mantenimiento
                    # if event.key == pygame.K_SPACE or event.key == pygame.K_p:
                       # print("---MANTENIMIENTO---")
                    # Filtramos de todas las teclas del teclado las que nos interesa para movernos(w,a,s,d,flechitas)
                    # Teclas W y Up
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        movimiento = True
                        if self.elemento.slider.direccion != "Arriba" and self.elemento.slider.direccion != "Abajo":
                            self.elemento.slider.direccion = "Arriba"
                            pause=False
                    # Teclas S y Down
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        movimiento = True
                        if self.elemento.slider.direccion != "Abajo" and self.elemento.slider.direccion != "Arriba":
                            self.elemento.slider.direccion = "Abajo"
                            pause = False
                    # Teclas A y Left
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        movimiento = True
                        if self.elemento.slider.direccion != "Izquierda" and self.elemento.slider.direccion != "Derecha":
                            self.elemento.slider.direccion = "Izquierda"
                            pause = False
                    # Teclas D y Right
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        movimiento = True
                        if self.elemento.slider.direccion != "Derecha" and self.elemento.slider.direccion != "Izquierda":
                            self.elemento.slider.direccion = "Derecha"
                            pause = False
            #
            #
            # Autmatizamos los movimientos
            newGameState = self.actualizarMapa(movimiento,newGameState)
            #
            # Dibujamos el tablero
            for x in range(self.nxC):
                for y in range(self.nyC):
                    # Implementamos la condicion del control del flujo
                    # if not pause:
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
            self.gameState = np.copy(self.cambioNivel(newGameState))
            # Actualizamos la pantalla
            pygame.display.flip()
            # Para pruebas
            # print(np.transpose(newGameState))
        # Modificamos la puntuacion
        self.score = self.elemento.slider.longitud - inicial
        pygame.quit()