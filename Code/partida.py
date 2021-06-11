import pygame
import sys
from mapa import *

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

        # Creo todo tipo de elementos que se van a interferir en el juego
        self.elemento = Elemento(nxC, nyC, self.nivel)

        # Inicializamos el estado de la partida
        self.estado = True

        # Lanzamos el metodo que va a iniciar la partida
        self.partida(height, width)

    def dificultad(self, movimiento):
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

    def cambioNivel(self):
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
                self.elemento.mapa.mapa = np.zeros((self.nyC, self.nxC))
                for i in self.elemento.snake.cuerpo:
                    self.elemento[i[0], i[1]] = 2
                self.elemento.creadorObstaculos(self.nivel, self.nxC, self.nyC)

    def partida(self, height, width):
        '''
        :param height: La altura que va a tener la ventana
        :param width: La anchura que va a tener la ventana
        :param highscore: La mejor puntuacion
        :return: No devuelve nada de manera explicita pero se lleva a cabo toda la partida y modifica ciertos atributos de clase
        '''
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
        self.elemento.mapa.actualizarMapa(self.elemento.lista_Objetivos, self.elemento.lista_Obstaculos, self.elemento.snake)
        #
        #
        # Configuramos las variable clave como el estado de la partida
        pause = True
        # Iniciamos la partida, en un principio pausada hasta que el jugador toque por primera vez una tecla cualquiera
        movimiento=False
        newMapa = np.copy(self.elemento.mapa.mapa)
        while self.estado:
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
                        if self.elemento.snake.direccion != "Arriba" and not self.elemento.snake.direccion == "Abajo":
                            self.elemento.snake.direccion = "Arriba"
                            pause=False
                    # Teclas S y Down
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        movimiento = True
                        if self.elemento.snake.direccion != "Abajo" and not self.elemento.snake.direccion == "Arriba":
                            self.elemento.snake.direccion = "Abajo"
                            pause = False
                    # Teclas A y Left
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        movimiento = True
                        if self.elemento.snake.direccion != "Izquierda" and not self.elemento.snake.direccion == "Derecha":
                            self.elemento.snake.direccion = "Izquierda"
                            pause = False
                    # Teclas D y Right
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        movimiento = True
                        if self.elemento.snake.direccion != "Derecha" and not self.elemento.snake.direccion == "Izquierda":
                            self.elemento.snake.direccion = "Derecha"
                            pause = False
            #
            #
            # Autmatizamos los movimientos
            newMapa = self.elemento.movimiento(newMapa)
            #
            screen.fill(bg)
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
                        if newMapa[x, y] == 0:
                            pygame.draw.polygon(screen, (128, 18, 128), poly, 1)
                        # Objetivo
                        elif newMapa[x, y] == 1:
                            pygame.draw.polygon(screen, (0, 255, 0), poly, 0)
                        # Slider
                        elif newMapa[x, y] == 2:
                            pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
                        else:
                            pygame.draw.polygon(screen, (255, 0, 0), poly, 0)
            if self.elemento.snake.estado == 0:
                self.estado = False
            # Actualizamos la pantalla
            self.elemento.mapa.mapa=np.copy(newMapa)
            pygame.display.flip()

            # Para pruebas
            #print(np.transpose(self.elemento.mapa.mapa))
        # Modificamos la puntuacion
        self.score = len(self.elemento.snake.cuerpo)-1
        pygame.quit()