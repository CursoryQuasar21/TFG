import numpy as np

class Mapa:

    def __init__(self, x, y):
        self.mapa = np.zeros((x, y))
        self.celdas = [x, y]

    def actualizarMapa(self, objetivos, obstaculos, snake):
        for i in objetivos:
            self.mapa[i.posicion[0], i.posicion[1]] = 1
        self.mapa[snake.cabeza[0], snake.cabeza[1]] = 2
        for i in obstaculos:
            self.mapa[i.posicion[0], i.posicion[1]] = 3

    def actualizarMapaIA(self, snakeJ, snakeIA, comidaP):
        newMapa = np.zeros((self.celdas[0], self.celdas[1]))
        newMapa[comidaP[0], comidaP[1]] = 1
        for i in snakeJ:
            newMapa[i[0], i[1]] = 2
        for i in snakeIA:
            newMapa[i[0], i[1]] = 4

        return newMapa