
class Snake:
    """
    Clase encargada de gestionar la snake y su comportamiento basico
    """
    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        """
        :param ejeX: Posicion en el eje X
        :param ejeY: Posicion en el eje Y
        :param celdasX: Cantidad de celdas en el eje X
        :param celdasY: Cantidad de celdas en el eje Y
        """

        self.cabeza = [ejeX, ejeY]
        self.cuerpo = [[ejeX, ejeY]]
        self.cola = [ejeX, ejeY]
        self.celdas = [celdasX, celdasY]
        self.direccion = "Ninguna"
        self.movimiento = 1
        self.estado = 2

    def cambiaDireccion(self):
        """
        :return: No devulve nada de manera explicita, pero modifica la posicion de la cabeza
        """

        if self.direccion == "Arriba":
            if self.cabeza[1] == 0 or self.cabeza[1] < (self.cabeza[1] - self.movimiento):
                self.cabeza[1] = self.celdas[1]-1
            else:
                self.cabeza[1] -= self.movimiento
        elif self.direccion == "Abajo":
            if self.cabeza[1] == self.celdas[1]-1 or self.cabeza[1] > (self.cabeza[1] + self.movimiento):
                self.cabeza[1] = 0
            else:
                self.cabeza[1] += self.movimiento
        elif self.direccion == "Izquierda":
            if self.cabeza[0] == 0 or self.cabeza[0] < (self.cabeza[0] - self.movimiento):
                self.cabeza[0] = self.celdas[0]-1
            else:
                self.cabeza[0] -= self.movimiento
        elif self.direccion == "Derecha":
            if self.cabeza[0] == self.celdas[0] - 1 or self.cabeza[0] > (self.cabeza[0] + self.movimiento):
                self.cabeza[0] = 0
            else:
                self.cabeza[0] += self.movimiento

    def moverCuerpo(self):
        """
        :return: El metodo no devuelve nada de manera explicita pero modifica atributos,
        de esta manera se consigue el efecto del movimiento
        """

        # Metodo utilizado para insertar al principio de una lista un elemento
        self.cuerpo.insert(0, list(self.cabeza))
        self.cola = self.cuerpo[len(self.cuerpo)-1]
        # Metodo que eleimina el ultimo elemento de la lista
        self.cuerpo.pop()

class SnakeIA:
    """
    Clase encargada de gestionar la snake en el modo de juego de la IA
    """

    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        """
        :param ejeX: Posicion en el eje X
        :param ejeY: Posicion en el eje Y
        :param celdasX: Cantidad de celdas en el eje X
        :param celdasY: Cantidad de celdas en el eje Y
        """

        self.posicion = [[ejeX, ejeY]]
        self.celdas = [celdasX, celdasY]
        self.cola = [ejeX, ejeY]
        self.movimiento = 1
        self.direccion = "Derecha"
        self.score = 0

    def cambiarDireccion(self, direccion):
        """
        :param direccion: Nueva direccion pasada por parametro
        :return: El metodo no devuelve nada de manera explicita pero modifica un atributo
        """
        if direccion == "Derecha" and not self.direccion == "Izquierda":
            self.direccion = "Derecha"
        if direccion == "Izquierda" and not self.direccion == "Derecha":
            self.direccion = "Izquierda"
        if direccion == "Arriba" and not self.direccion == "Abajo":
            self.direccion = "Arriba"
        if direccion == "Abajo" and not self.direccion == "Arriba":
            self.direccion = "Abajo"

    def mover(self, cp):
        """
        :param cp: Posicion de el objetivo en el mapa
        :return: El metodo no devuelve nada pero modifica ciertos atributos
        """

        # Guardamos la antigua primera posicion para su posterior utilizacion
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

        # Condicion que determina si la cabeza esta situada en la misma posicion que la comida
        if self.posicion[0] == cp:
            # Metodo por el cual se añade una nueva posicion a la lista
            self.posicion.append(self.cola)

        # Condicion que determina si la snake es superior a 1 de longitud
        if len(self.posicion) > 1:
            # Variable contador que alberga el numero de iteracion
            contador = 0
            for i in self.posicion:
                # Condicion que controla un error para evitar que la iteracion sea igual a la propia cabeza y se superponga
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
        """
        :return: Metodo que devuelve la cabeza de la snake
        """

        return self.posicion[0]

    def cuerpo(self):
        """
        :return: Metodo que devuelve el cuerpo sin la cabeza de la snake
        """

        contador = 0
        cuerpo = []
        for i in self.posicion:
            if contador > 0:
                cuerpo.append(i)

        return cuerpo