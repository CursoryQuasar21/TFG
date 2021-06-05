import pygame
import time
import sys
import numpy as np

#modularizar, crear una clase, la clase partida va ha contener los elementos
from elemento import Elementos

class Partida():
    #Creamos el constructor con todo lo que va ha intervenir en la partida
    def __init__(self, height, width, nxC, nyC):
        '''
        :param height: La altura que va a tener la ventana
        :param width: La anchura que va a tener la ventana
        :param nxC: La cantidad de celdas en el ejeX
        :param nyC: La cantidad de celdas en el ejeY
        '''
        # Guardamos las celdas de los dos ejes
        self.nxC = nxC
        self.nyC = nyC
        #prueba
        #self.nombreJugador=print(input("Introduce tu nombre, Jugador"))
        self.nombreJugador=""
        #nivel=print(int(input("Con que nivel quieres empezar:1-Facil 2-Medio 3-Dificil 4-Imposible")))
        nivel=1
        if nivel == 1:
            self.nivel = "facil"
        elif nivel == 2:
            self.nivel = "medio"
        elif nivel == 3:
            self.nivel = "dificil"
        else:
            self.nivel = "imposible"


        # Creo y guardo una matriz poniendo todos los valores a cero
        self.gameState=np.zeros((nyC,nxC))
        # Creo todo tipo de elementos que se van a interferir en el juego
        self.elemento=Elementos(nxC,nyC,self.nivel)
        # Lanzamos el metodo que va a iniciar la partida
        self.partida(height, width)

    def dificultad(self,movimiento):
        if movimiento == True:
            if self.nivel == "facil":
                self.fps.tick(4)
            elif self.nivel == "medio":
                self.fps.tick(12)
            elif self.nivel == "dificil":
                self.fps.tick(24)
            elif self.nivel == "imposible":
                self.fps.tick(32)
        else:
            if self.nivel == "facil" or self.nivel == "medio":
                self.fps.tick(40)
            else:
                self.fps.tick(100)

    def partida(self, height, width):
        '''
        :param height: La altura que va a tener la ventana
        :param width: La anchura que va a tener la ventana
        :param highscore: La mejor puntuacion
        :return: No devuelve nada de manera explicita pero se lleva a cabo toda la partida y modifica ciertos atributos de clase
        '''
        # Guardamos en una veriable autilizar la longitud inicial
        inicial=self.elemento.slider.longitud
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
        # Pintamos los objetivos
        for i in range(len(self.elemento.lista_Objetivos)):
            self.gameState[self.elemento.lista_Objetivos[i].posicionEjeX, self.elemento.lista_Objetivos[i].posicionEjeY] = 1
        # Pintamos la slider
        for i in range(self.elemento.slider.longitud):
            self.gameState[self.elemento.slider.posicionEjeX[i], self.elemento.slider.posicionEjeY[i]] = 2
        # Pintamos los obstaculos
        for i in range(len(self.elemento.lista_Obstaculos)):
            self.gameState[self.elemento.lista_Obstaculos[i].posicionEjeX, self.elemento.lista_Obstaculos[i].posicionEjeY] = 3
        #
        #
        # Configuramos las variable clave como el estado de la partida
        partida = True
        pause = True
        # Iniciamos la partida, en un principio pausada hasta que el jugador toque por primera vez una tecla cualquiera
        v=True
        movimiento=False
        while partida:
            # Para evitar cambios de forma secuencial, consiguiendo que todos los cambios
            newGameState = np.copy(self.gameState)
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
                        if self.elemento.slider.direccion != "arriba" and self.elemento.slider.direccion != "abajo":
                            self.elemento.slider.direccion = "arriba"
                            pause=False
                    # Teclas S y Down
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        movimiento = True
                        if self.elemento.slider.direccion != "abajo" and self.elemento.slider.direccion != "arriba":
                            self.elemento.slider.direccion = "abajo"
                            pause = False
                    # Teclas A y Left
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        movimiento = True
                        if self.elemento.slider.direccion != "izquierda" and self.elemento.slider.direccion != "derecha":
                            self.elemento.slider.direccion = "izquierda"
                            pause = False
                    # Teclas D y Right
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        movimiento = True
                        if self.elemento.slider.direccion != "derecha" and self.elemento.slider.direccion != "izquierda":
                            self.elemento.slider.direccion = "derecha"
                            pause = False
            #
            #
            # Autmatizamos los movimientos
            # Automatizamos la direccion de los objetivos
            objetivo_Impactado=None
            for i in range(len(self.elemento.lista_Objetivos)):
                newGameState[self.elemento.lista_Objetivos[i].posicionEjeX, self.elemento.lista_Objetivos[i].posicionEjeY] = 0
                self.elemento.lista_Objetivos[i].cambiaDireccion()
                newGameState[self.elemento.lista_Objetivos[i].posicionEjeX, self.elemento.lista_Objetivos[i].posicionEjeY] = 1
                if self.elemento.lista_Objetivos[i].posicionEjeX == self.elemento.slider.posicionEjeX[0] \
                    and self.elemento.lista_Objetivos[i].posicionEjeY == self.elemento.slider.posicionEjeY[0] \
                    and movimiento == True:
                    objetivo_Impactado = i
            if objetivo_Impactado != None:
                self.elemento.slider.objetivo_alcanzado(objetivo_Impactado)
                self.elemento.lista_Objetivos = self.elemento.slider.objetivos
            # Automatizamos la direccion de los obstaculos
            for i in range(len(self.elemento.lista_Obstaculos)):
                newGameState[self.elemento.lista_Obstaculos[i].posicionEjeX, self.elemento.lista_Obstaculos[i].posicionEjeY] = 0
                self.elemento.lista_Obstaculos[i].cambiaDireccion()
                newGameState[self.elemento.lista_Obstaculos[i].posicionEjeX, self.elemento.lista_Obstaculos[i].posicionEjeY] = 3
                if self.elemento.lista_Obstaculos[i].posicionEjeX == self.elemento.slider.posicionEjeX[0] \
                    and self.elemento.lista_Obstaculos[i].posicionEjeY == self.elemento.slider.posicionEjeY[0] \
                    and movimiento == True:
                    partida=False
                self.elemento.lista_Objetivos=self.elemento.slider.objetivos
            # Automatizamos la direccion del slider, para que siga con la direccion establecida
            if self.elemento.slider.direccion != "ninguna" and self.elemento.slider.estado!=0:
                newGameState[self.elemento.slider.posicionEjeX[0], self.elemento.slider.posicionEjeY[0]] = 0
                self.elemento.slider.cambiaDireccion(0, self.elemento.slider.direccion)
                newGameState[self.elemento.slider.posicionEjeX[0], self.elemento.slider.posicionEjeY[0]] = 2
                self.elemento.lista_Objetivos = self.elemento.slider.objetivos
                self.elemento.lista_Obstaculos = self.elemento.slider.obstaculos
                # Si la slider a chocado con un obstaculo, pasa de estar viva a muerta
                if self.elemento.slider.estado == 0:
                    partida = False
                else:
                    # Condicion si la slider tiene mas de una celda de longitud
                    if self.elemento.slider.longitud > 1 and self.elemento.slider.estado != 0:
                        varX = 0
                        varY = 0
                        # Hacemos que todo el cuerpo de la slider siga a la cabeza
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
            # Un verificador de impacto con objetivos
            objetivo_Impactado=None
            for i in range(len(self.elemento.lista_Objetivos)):
                if self.elemento.slider.posicionEjeX[0] == self.elemento.lista_Objetivos[i].posicionEjeX \
                        and self.elemento.slider.posicionEjeY[0] == self.elemento.lista_Objetivos[i].posicionEjeY \
                        and movimiento == True:
                    objetivo_Impactado = i
            if objetivo_Impactado!=None:
                self.elemento.slider.objetivo_alcanzado(objetivo_Impactado)
                self.elemento.lista_Objetivos = self.elemento.slider.objetivos
            # Un verificador de impacto con obstaculos
            obstaculo_Impactado = None
            for i in range(len(self.elemento.lista_Obstaculos)):
                if self.elemento.slider.posicionEjeX[0] == self.elemento.lista_Obstaculos[i].posicionEjeX \
                        and self.elemento.slider.posicionEjeY[0] == self.elemento.lista_Obstaculos[i].posicionEjeY \
                        and movimiento ==True:
                    partida = False
            #
            #
            # Dibujamos el tablero
            for x in range(0, self.nxC):
                for y in range(0, self.nyC):
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
            self.gameState = np.copy(newGameState)
            # Actualizamos la pantalla
            pygame.display.flip()
            # Condicion que determina si la slider se ha comido todos los objetivos
            if len(self.elemento.lista_Objetivos) == 0:
                # Coindiciones que en funcione del nivel actual, determina el proximo nivel
                if self.nivel == "facil":
                    self.nivel = "medio"
                elif self.nivel == "medio":
                    self.nivel = "dificil"
                elif self.nivel == "dificil":
                    self.nivel = "imposible"
                else:
                    self.nivel="imposible"
                # Creamos de nuevo todos los objetivos y obstaculos teniendo en cuenta la slider
                cantidadObjetivos = self.elemento.cantidadObjetivos(self.nivel,self.nxC,self.nyC)
                cantidadObstaculos = self.elemento.cantidadObstaculos(self.nivel, self.nxC, self.nyC)

                self.elemento.lista_Objetivos = []
                self.elemento.lista_Obstaculos = []
                # Creamos de nuevo todos los obstaculos
                self.elemento.creadorObjetivos(self.nivel,cantidadObjetivos,self.nxC,self.nyC)
                if self.nivel == "imposible":
                    self.elemento.creadorObstaculos(self.nivel, cantidadObstaculos, self.nxC, self.nyC)
                else:
                    self.gameState = np.zeros((self.nyC, self.nxC))
                    for i in range(self.elemento.slider.longitud):
                        newGameState[self.elemento.slider.posicionEjeX[i], self.elemento.slider.posicionEjeY[i]] = 2
                    self.elemento.creadorObstaculos(self.nivel, cantidadObstaculos, self.nxC, self.nyC)
            # Para pruebas
            # print(np.transpose(newGameState))
        # Modificamos la puntuacion
        self.score = self.elemento.slider.longitud - inicial


'''
def main():
    # Mapa (Matriz)
    mp = Mapa(50,50)
    mapa = mp.mapa

    # Mapa (Pygame)
    # Configuramos los ajustes de la pantalla
    pygame.init()
    height = 500
    width = 500
    # Configuramos las dimensiones de la pantalla
    screen = pygame.display.set_mode((height, width))
    # Dimensiones de las celdas en funcion del numero y cantidad de las mismas
    dimCW = width / 50
    dimCH = height / 50
    pygame.display.set_caption('A* with Snake')
    fps = pygame.time.Clock()
    # Con una intensidad los canales de color(Para formar colores en funcion de los primarios)
    bg = 25, 25, 25
    # Cambiamos el color de fondo por el elegido
    screen.fill(bg)

    # Comida
    foodSpawner = FoodSpawer(5,10)

    # IA
    snake = Snake(5, 5, 50, 50)
    score = 0
    inicio = (snake.posicionEjeX[0], snake.posicionEjeY[0])
    objetivo = (foodSpawner.posicionEjeX, foodSpawner.posicionEjeY)

    # Humano
    #snake2 = Snake(100, 100)
    #score2 = 0

    while True:
        newMapa = np.copy(mapa)
        camino = Astar(mapa, inicio, objetivo)
        print(camino)
        snake_x = snake.posicionEjeX[0]
        snake_y = snake.posicionEjeY[0]
        # IA
        for (x, y) in camino:
            if x > snake_x:
                snake.changueDirTo('Derecha')
            if x < snake_x:
                snake.changueDirTo('Izquierda')
            if y > snake_y:
                snake.changueDirTo('Abajo')
            if y < snake_y:
                snake.changueDirTo('Arriba')
            snake_x = x
            snake_y = y

        foodPos = []
        foodPos.append(foodSpawner.posicionEjeX)
        foodPos.append(foodSpawner.posicionEjeY)

        # IA
        if (snake.move(foodPos) == 1):  # Si hay colision
            score += 1
            foodSpawner.setFoodOnScreen(False)
        # Humano
        #if (snake2.move(foodPos) == 1):  # Si hay colision
        #    score2 += 1
        #    foodSpawner.setFoodOnScreen(False)

        newMapa[foodPos[0],foodPos[1]] = 1
        dimCW = 500 / 50
        dimCH = 500 / 50
        for x in range(50):
            for y in range(50):
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
        # IA
        print(snake.posicionEjeX)
        for pos in range(len(snake.posicionEjeX)):
            newMapa[snake.posicionEjeX[pos],snake.posicionEjeY[pos]] = 2

        # Humano
        # for pos in snake2.getBody():
        #    pygame.draw.rect(window, pygame.Color(0, 0, 225),
        #                     pygame.Rect(pos[0], pos[1], 10, 10))  # x,y,ancho,alto

        # Dibujar Comida
        newMapa[foodPos[0], foodPos[1]] = 1
        # Actualizamos el estado del juego
        mapa = np.copy(newMapa)
        # IA
        #if (snake.checkCollision() == 1):
        #    MAPA.gameOver(score, score2)
        # Humano
        #if (snake2.checkCollision() == 1):
        #    MAPA.gameOver(score, score2)
        print("--------")
        print(snake.getHeadPos())
        print("--------")
        # Puntaje
        pygame.display.set_caption("IA | Score :" + str(score))
        #pygame.display.set_caption("IA | Score :" + str(score) + " Humano | Score :" + str(score2))
        pygame.display.flip()
        fps.tick(24)

        # Actualizamos el estado del juego
        mapa = np.copy(newMapa)
        # Actualizamos la pantalla
        pygame.display.flip()
        # Nodo
        inicio = snake.getHeadPos()[0], snake.getHeadPos()[1]
        objetivo = foodPos[0], foodPos[1]

'''