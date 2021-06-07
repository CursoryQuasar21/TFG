import pygame
import random
import numpy as np

class Nodo():
    def __init__(self, pariente=None, posicion=None):
        self.pariente = pariente
        self.posicion = posicion

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, otro):
        return self.posicion == otro.posicion

def Astar(mapa, inicio, objetivo):
    Nodo_incio = Nodo(None, inicio)
    Nodo_incio.g = Nodo_incio.h = Nodo_incio.f = 0
    Nodo_fin = Nodo(None, objetivo)
    Nodo_fin.g = Nodo_fin.h = Nodo_fin.f = 0
    lista_abierta = []
    lista_cerrada = []
    lista_abierta.append(Nodo_incio)
    while len(lista_abierta) > 0:
        Nodo_actual = lista_abierta[0]
        index_actual = 0
        for index, item in enumerate(lista_abierta):
            if item.f < Nodo_actual.f:
                Nodo_actual = item
                index_actual = index

        lista_abierta.pop(index_actual)
        lista_cerrada.append(Nodo_actual)
        if Nodo_actual == Nodo_fin:
            path = []
            current = Nodo_actual
            while current is not None:
                path.append(current.posicion)
                current = current.pariente
            return path[::-1]

        sucesores = []
        for pos in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:  # adyacentes

            Nodo_posicion = (Nodo_actual.posicion[0] + pos[0], Nodo_actual.posicion[1] + pos[1])
            if Nodo_posicion[0] > (len(mapa) - 1) or Nodo_posicion[0] < 0 or Nodo_posicion[1] > (
                    len(mapa[len(mapa) - 1]) - 1) or Nodo_posicion[1] < 0:
                continue

            if mapa[Nodo_posicion[0]][Nodo_posicion[1]] != 0:
                continue

            nuevo_Nodo = Nodo(Nodo_actual, Nodo_posicion)

            sucesores.append(nuevo_Nodo)

        for sucesor in sucesores:
            for closed_child in lista_cerrada:
                if sucesor == closed_child:
                    continue

            sucesor.g = Nodo_actual.g + 1
            sucesor.h = ((sucesor.posicion[0] - Nodo_fin.posicion[0]) ** 2) + (
                        (sucesor.posicion[1] - Nodo_fin.posicion[1]) ** 2)
            sucesor.f = sucesor.g + sucesor.h

            for open_Nodo in lista_abierta:
                if sucesor == open_Nodo and sucesor.g > open_Nodo.g:
                    continue

            lista_abierta.append(sucesor)

class Snake():
    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        self.posicion = [[ejeX, ejeY]]
        self.celdas = [celdasX, celdasY]
        self.cola = [ejeX, ejeY]
        self.movimiento = 1
        self.direccion = "Derecha"

    def changueDirTo(self, direccion):
        if direccion == "Derecha" and not self.direccion == "Izquierda":
            self.direccion = "Derecha"
        if direccion == "Izquierda" and not self.direccion == "Derecha":
            self.direccion = "Izquierda"
        if direccion == "Arriba" and not self.direccion == "Abajo":
            self.direccion = "Arriba"
        if direccion == "Abajo" and not self.direccion == "Arriba":
            self.direccion = "Abajo"

    def cambiarDireccion(self, foodPos):
        self.cola = self.posicion[0].copy()
        if self.direccion == "Arriba" and not self.direccion == "Abajo":
            if self.posicion[0][1] == 0 or self.posicion[0][1] < (self.posicion[0][1] - self.movimiento):
                self.posicion[0][1] = self.celdas[1] - 1
            else:
                self.posicion[0][1] -= self.movimiento
        elif self.direccion == "Abajo" and not self.direccion == "Arriba":
            if self.posicion[0][1] == self.celdas[1] - 1 or self.posicion[0][1] > (
                    self.posicion[0][1] + self.movimiento):
                self.posicion[0][1] = 0
            else:
                self.posicion[0][1] += self.movimiento
        elif self.direccion == "Izquierda" and not self.direccion == "Derecha":
            if self.posicion[0][0] == 0 or self.posicion[0][0] < (self.posicion[0][0] - self.movimiento):
                self.posicion[0][0] = self.celdas[0] - 1
            else:
                self.posicion[0][0] -= self.movimiento
        elif self.direccion == "Derecha" and not self.direccion == "Izquierda":
            if self.posicion[0][0] == self.celdas[0] - 1 or self.posicion[0][0] > (
                    self.posicion[0][0] + self.movimiento):
                self.posicion[0][0] = 0
            else:
                self.posicion[0][0] += self.movimiento

        if self.posicion[0] == foodPos:
            self.posicion.append(self.cola)

        if len(self.posicion) > 1:
            contador = 0
            for i in self.posicion:
                if contador > 0:
                    colaX = self.cola[0]
                    colaY = self.cola[1]
                    varX = i[0]
                    varY = i[1]
                    self.posicion[contador] = [colaX, colaY]
                    self.cola[0] = varX
                    self.cola[1] = varY
                contador += 1

    def cabeza(self):
        return self.posicion[0]

    def cuerpo(self):
        contador = 0
        cuerpo = []
        for i in self.posicion:
            if contador > 0:
                cuerpo.append(i)
        return cuerpo

class Objetivo():
    def __init__(self, nxC, nyC):
        self.posicion = [random.randrange(nxC), random.randrange(nyC)]
        self.isFoodOnScreen = True

    def aparecer(self, nxC, nyC):
        if self.isFoodOnScreen == False:
            self.posicion = [random.randrange(nxC), random.randrange(nyC)]
            self.isFoodOnScreen = True
        return self.posicion

    def esta(self, b):
        self.isFoodOnScreen = b

class Mapa:

    def __init__(self, x, y):
        self.mapa = np.zeros((x, y))

    def getMapa(self):
        return self.mapa

def main():
    #
    #
    # Configuramos los ajustes de la pantalla
    pygame.init()
    # Configuramos las dimensiones de la pantalla
    height = 500
    width = 500
    nxC = 30
    nyC = 30
    screen = pygame.display.set_mode((height, width))
    # Dimensiones de las celdas en funcion del numero y cantidad de las mismas
    dimCW = width / nxC
    dimCH = height / nyC
    # Congiguramos el color de fondo
    # Con una intensidad los canales de color(Para formar colores en funcion de los primarios)
    bg = 25, 25, 25
    # Cambiamos el color de fondo por el elegido
    screen.fill(bg)
    fps = pygame.time.Clock()
    #
    #
    # Configuramos los elementos a nivel visual de la partida
    mapa = Mapa(nxC, nyC)

    # IA
    snake = Snake(nxC // 2, nyC // 2, nxC, nyC)
    score = 0
    inicio = snake.cabeza()

    comida = Objetivo(nxC, nyC)
    objetivo = (comida.posicion[0], comida.posicion[1])
    newMapa = np.copy(mapa.mapa)

    # Humano
    snake2 = Snake(nxC // 2, nyC // 2, nxC, nyC)
    score2 = 0

    screen.fill(bg)
    while True:
        camino = Astar(mapa.mapa, inicio, objetivo)
        snake_x = snake.cabeza()[0]
        snake_y = snake.cabeza()[1]
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
        # Humano
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake2.changueDirTo('Derecha')
                if event.key == pygame.K_LEFT:
                    snake2.changueDirTo('Izquierda')
                if event.key == pygame.K_UP:
                    snake2.changueDirTo('Arriba')
                if event.key == pygame.K_DOWN:
                    snake2.changueDirTo('Abajo')

        foodPos = comida.aparecer(nxC, nyC)  # Retorna posicion de comida

        # IA
        for i in snake.posicion:
            newMapa[i[0], i[1]] = 0
        snake.cambiarDireccion(foodPos)
        for i in snake.posicion:
            newMapa[i[0], i[1]] = 4
        # Humano
        for i in snake2.posicion:
            newMapa[i[0], i[1]] = 0
        snake2.cambiarDireccion(foodPos)
        for i in snake2.posicion:
            newMapa[i[0], i[1]] = 2


        if snake.posicion[0] == foodPos:
            score += 1
            comida.esta(False)
        if snake2.posicion[0] == foodPos:
            score2 += 1
            comida.esta(False)

        screen.fill(bg)

        # Dibujamos el tablero
        for x in range(nxC):
            for y in range(nyC):
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
                # Obstaculo
                elif newMapa[x, y] == 3:
                    pygame.draw.polygon(screen, (255, 0, 0), poly, 0)
                # IA
                else:
                    pygame.draw.polygon(screen, (0, 0, 255), poly, 0)

        newMapa[comida.posicion[0], comida.posicion[1]] = 1

        # Actualizamos la pantalla
        # Puntaje
        pygame.display.set_caption("IA | Score :" + str(score) + " Humano | Score :" + str(score2))
        pygame.display.flip()
        fps.tick(10)

        inicio = snake.cabeza()
        objetivo = (comida.posicion[0], comida.posicion[1])

if __name__ == '__main__':
    main()