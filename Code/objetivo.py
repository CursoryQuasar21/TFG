import random


class ObjetivoSimple:

    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        """
        :param ejeX: La posicion en el ejeX
        :param ejeY: La posicion en el ejeY
        :param celdasX: La cantidad de celdas del ejeX
        :param celdasY: La cantidad de celdas del ejeY
        """
        self.posicion = [ejeX, ejeY]
        self.celdas = [celdasX, celdasY]
        self.direccion = "Ninguna"
        self.movimiento = 0
        self.estado = 1

    def cambiaDireccion(self):
        """
        :return: No devulve nada de manera explicita, pero modifica la posicion del objetivo
        """
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

class ObjetivoMedio:

    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        """
        :param ejeX: La posicion en el ejeX
        :param ejeY: La posicion en el ejeY
        :param celdasX: La cantidad de celdas del ejeX
        :param celdasY: La cantidad de celdas del ejeY
        """
        self.posicion = [ejeX, ejeY]
        self.celdas = [celdasX, celdasY]
        self.direccion = "Ninguna"
        self.movimiento = 1
        self.estado = 1
        # Creo una lista con las diferentes direcciones y aleatoriamente se escoge una
        lista_Direcciones = ["Arriba", "Abajo", "Izquierda", "Derecha"]
        direccion = random.randrange(4)
        self.direccion = lista_Direcciones[direccion]

    def cambiaDireccion(self):
        """
        :return: No devulve nada de manera explicita, pero modifica la posicion del objetivo
        """
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

class ObjetivoDificil:

    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        """
        :param ejeX: La posicion en el ejeX
        :param ejeY: La posicion en el ejeY
        :param celdasX: La cantidad de celdas del ejeX
        :param celdasY: La cantidad de celdas del ejeY
        """
        self.posicion = [ejeX, ejeY]
        self.celdas = [celdasX, celdasY]
        self.direccion = "Ninguna"
        self.movimiento = 2
        self.estado = 1

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

class ObjetivoIA:
    def __init__(self, nxC, nyC):
        """
        :param nxC: Numero de celdas en el eje X
        :param nyC: Numero de celdas en el eje Y
        """

        # Creamos de manera aleatoria la posicion del objetivo
        self.posicion = [random.randrange(nxC), random.randrange(nyC)]
        # Confirmamos que el objetivo se encuentra en la pantalla
        self.isFoodOnScreen = True

    def aparecer(self, nxC, nyC):
        """
        :param nxC: Numero de celdas en el eje X
        :param nyC: Numero de celdas en el eje Y
        :return: Devuleve la posicion en el mapa del objetivo
        """

        # Condicional que determina si esta el objetivo en pantalla
        if not self.isFoodOnScreen:
            self.posicion = [random.randrange(nxC), random.randrange(nyC)]
            self.isFoodOnScreen = True

        return self.posicion

    def esta(self, b):
        """
        :param b: Estado del objetivo en pantalla
        :return: No devuleve nada de manera explicita pero modifica un atributo
        """

        # Cambia el valor del atributo al pasado por parametro
        self.isFoodOnScreen = b