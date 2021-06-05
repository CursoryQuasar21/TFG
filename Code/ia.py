import pygame
import sys
import random
import time
import numpy as np

# Developers: - Rodrigo Lara
#            - Cesar Gutierrez
#      -------------------------------
#
#                Snake Game
#                   with
#           A Asterisk Algortihm
#
#      -------------------------------

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
    print(inicio)
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


##########################
class Snake():
    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        self.posicionEjeX = [ejeX,ejeX-1]
        self.posicionEjeY = [ejeY]
        self.celdasX = celdasX
        self.celdasY = celdasY
        self.direction = "Derecha"

    def changueDirTo(self, direccion):
        if direccion == "Derecha" and not self.direction == "Izquierda":
            self.direction = "Derecha"
        if direccion == "Izquierda" and not self.direction == "Derecha":
            self.direction = "Izquierda"
        if direccion == "Arriba" and not self.direction == "Abajo":
            self.direction = "Arriba"
        if direccion == "Abajo" and not self.direction == "Arriba":
            self.direction = "Abajo"

    def move(self,foodPos):
        if self.direction == "Derecha":
            self.posicionEjeX[0] += 1
        if self.direction == "Izquierda":
            self.posicionEjeX[0] -= 1
        if self.direction == "Arriba":
            self.posicionEjeX[0] -= 1
        if self.direction == "Abajo":
            self.posicionEjeX[0] += 1

        if self.posicionEjeX[0] == foodPos[0] and self.posicionEjeY[0] == foodPos[1]:
            self.posicionEjeX.insert(0, foodPos[0])
            self.posicionEjeY.insert(0, foodPos[1])
            return 1
        else:
            return 0


    def checkCollision(self):
        x = self.posicionEjeX[0]
        y = self.posicionEjeY[0]
        if x > self.celdasX or x < 0:
            return 1
        elif y > self.celdasY or y < 0:
            return 1
        # for bodyPart in self.body[1:]:
        # if self.position == bodyPart:
        #   return 1
        return 0

    def getHeadPos(self):
        posicion = [self.posicionEjeX[0],self.posicionEjeY[0]]
        return posicion

    def getBody(self):
        posicion = []
        for i in range(len(self.posicionEjeX)):
            if i >0:
                posicion.append([self.posicionEjeX[i], self.posicionEjeY[i]])
        return posicion

class FoodSpawer():
    def __init__(self, ejeX, ejeY):
        self.posicionEjeX = ejeX
        self.posicionEjeY = ejeY
        self.isFoodOnScreen = True

    def spawnFood(self):
        if self.isFoodOnScreen == False:
            self.posicionEjeX = random.randrange(1, 50) * 10
            self.posicionEjeX = random.randrange(1, 50) * 10
            self.isFoodOnScreen = True
        return self.position

    def setFoodOnScreen(self, b):
        self.isFoodOnScreen = b


class Mapa:

    def __init__(self, x, y):
        self.mapa = np.zeros((x, y))

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

if __name__ == '__main__':
    main()