import numpy as np

class Mapa:

    def __init__(self, x, y):
        self.mapa = np.zeros((x, y))

    def actualizarMapa(self, objetivos, obstaculos, snake):
        for i in objetivos:
            self.mapa[i.posicion[0], i.posicion[1]] = 1
        self.mapa[snake.cabeza[0], snake.cabeza[1]] = 2
        for i in obstaculos:
            self.mapa[i.posicion[0], i.posicion[1]] = 3
