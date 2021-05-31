import random


class ObstaculoSimple():
    posicionEjeX = 0
    posicionEjeY = 0
    celdasX = 0
    celdasY = 0
    direccion="ninguna"
    movimiento = 0
    estado = 1

    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        '''
        :param ejeX: La posicion en el ejeX
        :param ejeY: La posicion en el ejeY
        :param celdasX: La cantidad de celdas del ejeX
        :param celdasY: La cantidad de celdas del ejeY
        '''
        self.posicionEjeX = ejeX
        self.posicionEjeY = ejeY
        self.celdasX = celdasX
        self.celdasY = celdasY
    # Método para añadir dificultad al juego
    # Según aumente la dificultad se moverá más rápido
    def cambiaDireccion(self):
        if self.direccion != "ninguna":
            if self.direccion == "arriba":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if 0 > (self.posicionEjeY - self.movimiento):
                    if self.posicionEjeY == 0:
                        self.posicionEjeY = self.celdasY - self.movimiento
                    else:
                        self.posicionEjeY = self.celdasY - ((0 - self.posicionEjeY) + self.movimiento)
                else:
                    self.posicionEjeY -= self.movimiento
            elif self.direccion == "abajo":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if self.celdasY <= (self.posicionEjeY + self.movimiento):
                    if self.posicionEjeY == self.celdasY:
                        self.posicionEjeY = self.movimiento
                    else:
                        self.posicionEjeY = ((self.posicionEjeY - self.celdasY) + self.movimiento)
                else:
                    self.posicionEjeY += self.movimiento
            elif self.direccion == "izquierda":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if 0 > (self.posicionEjeX - self.movimiento):
                    if self.posicionEjeX == 0:
                        self.posicionEjeX = self.celdasX - self.movimiento
                    else:
                        self.posicionEjeX = self.celdasX - ((0 - self.posicionEjeX) + self.movimiento)
                else:
                    self.posicionEjeX -= self.movimiento
            elif self.direccion == "derecha":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if self.celdasX <= (self.posicionEjeX + self.movimiento):
                    if self.posicionEjeX == self.celdasX:
                        self.posicionEjeX = self.movimiento
                    else:
                        self.posicionEjeX = ((self.posicionEjeX - self.celdasX) + self.movimiento)
                else:
                    self.posicionEjeX += self.movimiento

class ObstaculoMedio():
    posicionEjeX = 0
    posicionEjeY = 0
    celdasX=0
    celdasY=0
    direccion = "ninguna"
    movimiento = 1
    estado = 1

    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        '''
        :param ejeX: La posicion en el ejeX
        :param ejeY: La posicion en el ejeY
        :param celdasX: La cantidad de celdas del ejeX
        :param celdasY: La cantidad de celdas del ejeY
        '''
        self.posicionEjeX = ejeX
        self.posicionEjeY = ejeY
        self.celdasX = celdasX
        self.celdasY = celdasY
        # Creo una lista con las diferentes direcciones y aleatoriamente se escoge una
        lista_Direcciones = ["arriba", "abajo", "izquierda", "derecha"]
        direccion = random.randrange(4)
        self.direccion = lista_Direcciones[direccion]

    # Método para añadir dificultad al juego
    # Según aumente la dificultad se moverá más rápido
    def cambiaDireccion(self):
        if self.direccion != "ninguna":
            if self.direccion == "arriba":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if 0 > (self.posicionEjeY - self.movimiento):
                    if self.posicionEjeY == 0:
                        self.posicionEjeY = self.celdasY - self.movimiento
                    else:
                        self.posicionEjeY = self.celdasY - ((0 - self.posicionEjeY) + self.movimiento)
                else:
                    self.posicionEjeY -= self.movimiento
            elif self.direccion == "abajo":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if self.celdasY <= (self.posicionEjeY + self.movimiento):
                    if self.posicionEjeY == self.celdasY:
                        self.posicionEjeY = self.movimiento
                    else:
                        self.posicionEjeY = ((self.posicionEjeY - self.celdasY) + self.movimiento)
                else:
                    self.posicionEjeY += self.movimiento
            elif self.direccion == "izquierda":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if 0 > (self.posicionEjeX - self.movimiento):
                    if self.posicionEjeX == 0:
                        self.posicionEjeX = self.celdasX - self.movimiento
                    else:
                        self.posicionEjeX = self.celdasX - ((0 - self.posicionEjeX) + self.movimiento)
                else:
                    self.posicionEjeX -= self.movimiento
            elif self.direccion == "derecha":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if self.celdasX <= (self.posicionEjeX + self.movimiento):
                    if self.posicionEjeX == self.celdasX:
                        self.posicionEjeX = self.movimiento
                    else:
                        self.posicionEjeX = ((self.posicionEjeX - self.celdasX) + self.movimiento)
                else:
                    self.posicionEjeX += self.movimiento

class ObstaculoDificil():
    posicionEjeX = 0
    posicionEjeY = 0
    celdasX=0
    celdasY=0
    direccion = "ninguna"
    movimiento = 2
    estado = 1

    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        '''
        :param ejeX: La posicion en el ejeX
        :param ejeY: La posicion en el ejeY
        :param celdasX: La cantidad de celdas del ejeX
        :param celdasY: La cantidad de celdas del ejeY
        '''
        self.posicionEjeX = ejeX
        self.posicionEjeY = ejeY
        self.celdasX = celdasX
        self.celdasY = celdasY

    # Método para añadir dificultad al juego
    # Según aumente la dificultad se moverá más rápido
    def cambiaDireccion(self):
        # Creo una lista con las diferentes direcciones y aleatoriamente se escoge una
        lista_Direcciones = ["arriba", "abajo", "izquierda", "derecha"]
        direccion = random.randrange(4)
        self.direccion = lista_Direcciones[direccion]
        if self.direccion != "ninguna":
            if self.direccion == "arriba":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if 0 > (self.posicionEjeY - self.movimiento):
                    if self.posicionEjeY == 0:
                        self.posicionEjeY = self.celdasY - self.movimiento
                    else:
                        self.posicionEjeY = self.celdasY - ((0 - self.posicionEjeY) + self.movimiento)
                else:
                    self.posicionEjeY -= self.movimiento
            elif self.direccion == "abajo":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if self.celdasY <= (self.posicionEjeY + self.movimiento):
                    if self.posicionEjeY == self.celdasY:
                        self.posicionEjeY = self.movimiento
                    else:
                        self.posicionEjeY = ((self.posicionEjeY - self.celdasY) + self.movimiento)
                else:
                    self.posicionEjeY += self.movimiento
            elif self.direccion == "izquierda":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if 0 > (self.posicionEjeX - self.movimiento):
                    if self.posicionEjeX == 0:
                        self.posicionEjeX = self.celdasX - self.movimiento
                    else:
                        self.posicionEjeX = self.celdasX - ((0 - self.posicionEjeX) + self.movimiento)
                else:
                    self.posicionEjeX -= self.movimiento
            elif self.direccion == "derecha":
                # La condicion tiene en cuenta la estrategia toroidal o del pacman
                if self.celdasX <= (self.posicionEjeX + self.movimiento):
                    if self.posicionEjeX == self.celdasX:
                        self.posicionEjeX = self.movimiento
                    else:
                        self.posicionEjeX = ((self.posicionEjeX - self.celdasX) + self.movimiento)
                else:
                    self.posicionEjeX += self.movimiento