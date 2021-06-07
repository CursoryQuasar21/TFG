import random


class ObstaculoSimple():

    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        '''
        :param ejeX: La posicion en el ejeX
        :param ejeY: La posicion en el ejeY
        :param celdasX: La cantidad de celdas del ejeX
        :param celdasY: La cantidad de celdas del ejeY
        '''
        self.posicion = [ejeX, ejeY]
        self.celdas = [celdasX, celdasY]
        self.direccion = "Ninguna"
        self.movimiento = 0
        self.estado = 1
    # Método para añadir dificultad al juego
    # Según aumente la dificultad se moverá más rápido
    def cambiaDireccion(self):
        if self.direccion != "Ninguna":
            if self.direccion == "Arriba":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if 0 > (self.posicion[1] - self.movimiento):
                    if self.posicion[1] == 0:
                        self.posicion[1] = self.celdas[1] - self.movimiento
                    else:
                        self.posicion[1] = self.posicion[1] - ((0 - self.posicion[1]) + self.movimiento)
                else:
                    self.posicion[1] -= self.movimiento
            elif self.direccion == "Abajo":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if self.celdas[1] <= (self.posicion[1] + self.movimiento):
                    if self.posicion[1] == self.celdas[1]:
                        self.posicion[1] = self.movimiento
                    else:
                        self.posicion[1] = ((self.posicion[1] - self.celdas[1]) + self.movimiento)
                else:
                    self.posicion[1] += self.movimiento
            elif self.direccion == "Izquierda":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if 0 > (self.posicion[0] - self.movimiento):
                    if self.posicion[0] == 0:
                        self.posicion[0] = self.celdas[0] - self.movimiento
                    else:
                        self.posicion[0] = self.celdas[0] - ((0 - self.posicion[0]) + self.movimiento)
                else:
                    self.posicion[0] -= self.movimiento
            elif self.direccion == "Derecha":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if self.celdas[0] <= (self.posicion[0] + self.movimiento):
                    if self.posicion[0] == self.celdas[0]:
                        self.posicion[0] = self.movimiento
                    else:
                        self.posicion[0] = ((self.posicion[0] - self.celdas[0]) + self.movimiento)
                else:
                    self.posicion[0] += self.movimiento

class ObstaculoMedio():

    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        '''
        :param ejeX: La posicion en el ejeX
        :param ejeY: La posicion en el ejeY
        :param celdasX: La cantidad de celdas del ejeX
        :param celdasY: La cantidad de celdas del ejeY
        '''
        self.posicion = [ejeX, ejeY]
        self.celdas = [celdasX, celdasY]
        self.direccion = "Ninguna"
        self.movimiento = 1
        self.estado = 1
        # Creo una lista con las diferentes direcciones y aleatoriamente se escoge una
        lista_Direcciones = ["Arriba", "Abajo", "Izquierda", "Derecha"]
        direccion = random.randrange(4)
        self.direccion = lista_Direcciones[direccion]

    # Método para añadir dificultad al juego
    # Según aumente la dificultad se moverá más rápido
    def cambiaDireccion(self):
        if self.direccion != "Ninguna":
            if self.direccion == "Arriba":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if 0 > (self.posicion[1] - self.movimiento):
                    if self.posicion[1] == 0:
                        self.posicion[1] = self.celdas[1] - self.movimiento
                    else:
                        self.posicion[1] = self.posicion[1] - ((0 - self.posicion[1]) + self.movimiento)
                else:
                    self.posicion[1] -= self.movimiento
            elif self.direccion == "Abajo":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if self.celdas[1] <= (self.posicion[1] + self.movimiento):
                    if self.posicion[1] == self.celdas[1]:
                        self.posicion[1] = self.movimiento
                    else:
                        self.posicion[1] = ((self.posicion[1] - self.celdas[1]) + self.movimiento)
                else:
                    self.posicion[1] += self.movimiento
            elif self.direccion == "Izquierda":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if 0 > (self.posicion[0] - self.movimiento):
                    if self.posicion[0] == 0:
                        self.posicion[0] = self.celdas[0] - self.movimiento
                    else:
                        self.posicion[0] = self.celdas[0] - ((0 - self.posicion[0]) + self.movimiento)
                else:
                    self.posicion[0] -= self.movimiento
            elif self.direccion == "Derecha":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if self.celdas[0] <= (self.posicion[0] + self.movimiento):
                    if self.posicion[0] == self.celdas[0]:
                        self.posicion[0] = self.movimiento
                    else:
                        self.posicion[0] = ((self.posicion[0] - self.celdas[0]) + self.movimiento)
                else:
                    self.posicion[0] += self.movimiento

class ObstaculoDificil():

    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        '''
        :param ejeX: La posicion en el ejeX
        :param ejeY: La posicion en el ejeY
        :param celdasX: La cantidad de celdas del ejeX
        :param celdasY: La cantidad de celdas del ejeY
        '''
        self.posicion = [ejeX, ejeY]
        self.celdas = [celdasX, celdasY]
        self.direccion = "Ninguna"
        self.movimiento = 2
        self.estado = 1
    # Método para añadir dificultad al juego
    # Según aumente la dificultad se moverá más rápido
    def cambiaDireccion(self):
        # Creo una lista con las diferentes direcciones y aleatoriamente se escoge una
        lista_Direcciones = ["Arriba", "Abajo", "Izquierda", "Derecha"]
        direccion = random.randrange(4)
        self.direccion = lista_Direcciones[direccion]
        if self.direccion != "Ninguna":
            if self.direccion == "Arriba":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if 0 > (self.posicion[1] - self.movimiento):
                    if self.posicion[1] == 0:
                        self.posicion[1] = self.celdas[1] - self.movimiento
                    else:
                        self.posicion[1] = self.posicion[1] - ((0 - self.posicion[1]) + self.movimiento)
                else:
                    self.posicion[1] -= self.movimiento
            elif self.direccion == "Abajo":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if self.celdas[1] <= (self.posicion[1] + self.movimiento):
                    if self.posicion[1] == self.celdas[1]:
                        self.posicion[1] = self.movimiento
                    else:
                        self.posicion[1] = ((self.posicion[1] - self.celdas[1]) + self.movimiento)
                else:
                    self.posicion[1] += self.movimiento
            elif self.direccion == "Izquierda":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if 0 > (self.posicion[0] - self.movimiento):
                    if self.posicion[0] == 0:
                        self.posicion[0] = self.celdas[0] - self.movimiento
                    else:
                        self.posicion[0] = self.celdas[0] - ((0 - self.posicion[0]) + self.movimiento)
                else:
                    self.posicion[0] -= self.movimiento
            elif self.direccion == "Derecha":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if self.celdas[0] <= (self.posicion[0] + self.movimiento):
                    if self.posicion[0] == self.celdas[0]:
                        self.posicion[0] = self.movimiento
                    else:
                        self.posicion[0] = ((self.posicion[0] - self.celdas[0]) + self.movimiento)
                else:
                    self.posicion[0] += self.movimiento
