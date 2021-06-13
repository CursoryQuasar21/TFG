import pygame
from mapa import *
from elemento import Elemento

class Partida:
    """
    Esta clase se encarga de iniciar la partida, crear los elementos y gestionar la dificultad
    """

    def __init__(self, height, width, nxC, nyC, nombre, nivel):
        """
        :param height: La altura que va a tener la ventana
        :param width: La anchura que va a tener la ventana
        :param nxC: La cantidad de celdas en el ejeX
        :param nyC: La cantidad de celdas en el ejeY
        """

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

        # Inicializamos todos los elementos que intervienen en el partida
        self.elemento = Elemento(nxC, nyC, self.nivel)

        # Inicializamos el estado de la partida
        self.estado = True

        # Lanzamos el metodo que va a iniciar la partida
        self.partida(height, width)

        # Modificamos la puntuacion
        self.score = len(self.elemento.snake.cuerpo) - 1
        pygame.quit()

    def dificultad(self, movimiento):
        """
        :param movimiento: El parametro movimiento es el que determina si ha empezado la partida para el jugador
        :return: No devuelve nada de manera explicita, pero modifica el timing de la ejecucion
        """

        # Condicion que determina si la snake se ha movido y de ser asi, en funcion del nivel, el timing es uno u otro
        if movimiento != "Ninguna":
            if self.nivel == "facil":
                self.fps.tick(4)
            elif self.nivel == "medio":
                self.fps.tick(12)
            elif self.nivel == "dificil":
                self.fps.tick(16)
            elif self.nivel == "imposible":
                self.fps.tick(24)
        # Condicion que mantiene el juego en un timing superior al establecido por el nivel por una razon
        # Para evitar que el jugador sea capaz de encontrar patrones
        else:
            if self.nivel == "facil" or self.nivel == "medio":
                self.fps.tick(40)
            else:
                self.fps.tick(100)

    def cambioNivel(self, newMapa):
        """
        :param newMapa: El mapa de la partida en un momento concreto
        :return: El metodo devuelve el mapa segun unos posibles cambios
        """

        # Condicion que verifica si se han capturado todos los objetivos
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

            # Vaciamos las listas de los objetivos y de los obstaculos
            self.elemento.lista_Objetivos = []
            self.elemento.lista_Obstaculos = []

            # Creamos de nuevo todos los objetivos
            self.elemento.creadorObjetivos(self.nivel, self.nxC, self.nyC)
            # Condicion que determina si el nivel esta en imposible, crea señuelos que aumenta la dificultad del juego
            if self.nivel == "imposible":
                # Creamos de nuevo todos los obstaculos
                self.elemento.creadorObstaculos(self.nivel, self.nxC, self.nyC)
            else:
                # Creamos un nuevo mapa
                self.elemento.mapa.mapa = np.zeros((self.nyC, self.nxC))
                # Creamos de nuevo todos los obstaculos
                self.elemento.creadorObstaculos(self.nivel, self.nxC, self.nyC)

        return newMapa

    def juegoPausado(self):
        pausa = np.zeros((self.nxC, self.nyC))
        return pausa

    def partida(self, height, width):
        """
        :param height: La altura que va a tener la ventana
        :param width: La anchura que va a tener la ventana
        :return: No devuelve nada de manera explicita pero se lleva a cabo toda la partida
        """

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

        # Configuramos los elementos a nivel visual de la partida
        self.elemento.mapa.actualizarMapa(self.elemento.lista_Objetivos,
                                          self.elemento.lista_Obstaculos,
                                          self.elemento.snake)

        # Creamos un mapa identico al original, con el objetivo de que no tenga en cuenta un factor importante,
        # No tener en cuenta las operaciones de la iteracion anterior
        newMapa = np.copy(self.elemento.mapa.mapa)

        # Variable que controla si el juego esta pausado o no
        pause = False

        # Iniciamos el bucle que pondra la partida en marcha
        while self.estado:
            # Meotodo encargado de controlar el timing del juego
            self.dificultad(self.elemento.snake.direccion)

            # Limpiamos la pantalla para que no se superponga los datos de la anterior iteracion
            screen.fill(bg)

            # Eventos de Teclado y raton
            ev = pygame.event.get()
            for event in ev:
                # Evento de cierre de ventana mediante raton
                if event.type == pygame.QUIT:
                    pygame.quit()
                # Evento de teclado
                if event.type == pygame.KEYDOWN:
                    # Filtramos de todas las teclas del teclado las que nos interesa para pausar el juego
                    if event.key == pygame.K_SPACE or event.key == pygame.K_p:
                        pause = not pause
                    # Filtramos de todas las teclas del teclado las que nos interesa para movernos(w,a,s,d,flechitas)
                    # Teclas W y Up
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        if self.elemento.snake.direccion != "Arriba" and not self.elemento.snake.direccion == "Abajo":
                            self.elemento.snake.direccion = "Arriba"
                    # Teclas S y Down
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        if self.elemento.snake.direccion != "Abajo" and not self.elemento.snake.direccion == "Arriba":
                            self.elemento.snake.direccion = "Abajo"
                    # Teclas A y Left
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        if self.elemento.snake.direccion != "Izquierda" and not self.elemento.snake.direccion == "Derecha":
                            self.elemento.snake.direccion = "Izquierda"
                    # Teclas D y Right
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        if self.elemento.snake.direccion != "Derecha" and not self.elemento.snake.direccion == "Izquierda":
                            self.elemento.snake.direccion = "Derecha"
            #
            #

            # Dibujamos el tablero
            for x in range(self.nxC):
                for y in range(self.nyC):
                    # Dibujo de un poligono cuadrilatero regular
                    poly = [(x * dimCW, y * dimCH),
                            ((x + 1) * dimCW, y * dimCH),
                            ((x + 1) * dimCW, (y + 1) * dimCH),
                            (x * dimCW, (y + 1) * dimCH)]
                    # Reglas basicas de cada elemento en el mapa
                    # Dibujamos la celda por cada par de x e y
                    # Celda muerta
                    if newMapa[x, y] == 0:
                        pygame.draw.polygon(screen, (128, 18, 128), poly, 1)
                    # Objetivo
                    elif newMapa[x, y] == 1:
                        pygame.draw.polygon(screen, (0, 255, 0), poly, 0)
                    # Snake
                    elif newMapa[x, y] == 2:
                        pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
                    # Obstaculo
                    else:
                        pygame.draw.polygon(screen, (255, 0, 0), poly, 0)
            # Condicion que determina si el juego esta en pausa o no
            if pause:
                newMapa = self.juegoPausado()
            else:
                # Autmatizamos los movimientos
                newMapa = self.elemento.autmoatizarMovimietno(newMapa)

            # Condicion que determina el estaddo de la partida en funcion del estado de la snake
            if self.elemento.snake.estado == 0:
                self.estado = False

            # Actualizamos el estado del juego
            self.elemento.mapa.mapa = np.copy(self.cambioNivel(newMapa))

            # Actualizamos la pantalla
            pygame.display.flip()
