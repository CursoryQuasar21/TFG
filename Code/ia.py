import pygame
from snake import *
from mapa import *
from objetivo import *

def partida():

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

    # Configuramos los elementos a nivel visual de la partida
    mapa = Mapa(nxC, nyC)

    # Humano
    snakeH = SnakeIA(nxC // 2, nyC // 2, nxC, nyC)
    # IA
    snakeIA = SnakeIA(nxC // 2, nyC // 2, nxC, nyC)
    inicio = snakeIA.cabeza()
    # Comida
    comida = ObjetivoIA(nxC, nyC)
    objetivo = (comida.posicion[0], comida.posicion[1])


    screen.fill(bg)
    while True:
        camino = Astar(mapa.mapa, inicio, objetivo)
        snakeIA_x = snakeIA.cabeza()[0]
        snakeIA_y = snakeIA.cabeza()[1]
        for (x, y) in camino:
            if y > snakeIA_y:
                snakeIA.cambiarDireccion("Abajo")
            if y < snakeIA_y:
                snakeIA.cambiarDireccion("Arriba")
            if x > snakeIA_x:
                snakeIA.cambiarDireccion("Derecha")
            if x < snakeIA_x:
                snakeIA.cambiarDireccion("Izquierda")
            snakeIA_x = x
            snakeIA_y = y

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    snakeH.cambiarDireccion("Arriba")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    snakeH.cambiarDireccion("Abajo")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    snakeH.cambiarDireccion("Derecha")
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    snakeH.cambiarDireccion("Izquierda")

        cp = comida.aparecer(nxC, nyC)
        snakeH.mover(comida.posicion)
        snakeIA.mover(comida.posicion)
        newMapa = mapa.actualizarMapaIA(snakeH.posicion, snakeIA.posicion, comida.posicion)

        if snakeH.posicion[0] == cp:
            snakeH.score += 1
            comida.esta(False)
        if snakeIA.posicion[0] == cp:
            snakeIA.score += 1
            comida.esta(False)


        screen.fill(bg)

        # Dibujamos el tablero
        for x in range(nxC):
            for y in range(nyC):
                # Implementamos la condicion del control del flujo
                # if not pause:
                # Creamos los cuadrados de cada celda a dibujar
                poly = [(x * dimCW, y * dimCH),
                        ((x + 1) * dimCW, y * dimCH),
                        ((x + 1) * dimCW, (y + 1) * dimCH),
                        (x * dimCW, (y + 1) * dimCH)]
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
                # Snake
                elif newMapa[x, y] == 2:
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
                # Obstaculo
                elif newMapa[x, y] == 3:
                    pygame.draw.polygon(screen, (255, 0, 0), poly, 0)
                # IA
                else:
                    pygame.draw.polygon(screen, (0, 0, 255), poly, 0)

        newMapa[comida.posicion[0], comida.posicion[1]] = 1
        # Puntaje
        pygame.display.set_caption("IA | Score :" + str(snakeIA.score) + " Humano | Score :" + str(snakeH.score))
        pygame.display.flip()
        fps.tick(10)

        inicio = snakeIA.cabeza()
        objetivo = (comida.posicion[0], comida.posicion[1])

class Nodo:
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

if __name__ == '__main__':
    partida()