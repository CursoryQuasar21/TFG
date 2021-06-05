import numpy as np

class Slider():

    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        '''
        :param ejeX: La posicion en el que se encuentra la cabeza en el ejeX
        :param ejeY: La posicion en el que se encuentra la cabeza en el ejeX
        :param celdasX: La cantidad de celdas en el ejeX
        :param celdasY: La cantidad de celdas en el ejeY
        '''
        self.posicionEjeX = [ejeX]
        self.posicionEjeY = [ejeY]
        self.colaX = ejeX
        self.colaY = ejeY
        self.celdasX = celdasX
        self.celdasY = celdasY
        self.direccion = "ninguna"
        self.longitud = 1
        self.movimiento = 1
        self.estado = 2
        # Array que guarda instancias de objetivos
        self.objetivos = []
        # Array que guarda instancias de obstaculos
        self.obstaculos = []
        if self.longitud > 1:
            for i in range(self.longitud):
                self.posicionEjeX.append(self.posicionEjeX[i])
                self.posicionEjeY.append(self.posicionEjeY[i-1]-1)

    # En desarrollo, hay que mirar el funcionamiento cuando la velocidad es superior a 1
    def cambiaDireccion(self,eje,direccion):
        if direccion == "arriba" and not self.direccion == "abajo":
            self.direccion = "arriba"
            self.colaY = self.posicionEjeY[0]
            if self.posicionEjeY[eje] == 0 or self.posicionEjeY[eje] < (self.posicionEjeY[eje] - self.movimiento):
                self.posicionEjeY[eje] = self.celdasY-1
            else:
                self.posicionEjeY[eje] -= self.movimiento
        elif direccion == "abajo" and not self.direccion == "arriba":
            self.direccion = "abajo"
            self.colaY = self.posicionEjeY[eje]
            if self.posicionEjeY[eje] == self.celdasY-1 or self.posicionEjeY[eje] > (self.posicionEjeY[eje] + self.movimiento):
                self.posicionEjeY[eje] = 0
            else:
                self.posicionEjeY[eje] += self.movimiento
        elif direccion == "izquierda" and not self.direccion == "derecha":
            self.direccion = "izquierda"
            self.colaX = self.posicionEjeX[eje]
            if self.posicionEjeX[eje] == 0 or self.posicionEjeX[eje] < (self.posicionEjeX[eje] - self.movimiento):
                self.posicionEjeX[eje] = self.celdasX-1
            else:
                self.posicionEjeX[eje] -= self.movimiento
        elif direccion == "derecha" and not self.direccion == "izquierda":
            self.direccion = "derecha"
            self.colaX = self.posicionEjeX[eje]
            if self.posicionEjeX[eje] == self.celdasX-1 or self.posicionEjeX[eje] > (self.posicionEjeX[eje] + self.movimiento):
                self.posicionEjeX[eje] = 0
            else:
                self.posicionEjeX[eje] += self.movimiento

        if self.direccion != "ninguna":
            verificarObjetivo = False
            marcadorObjetivo = 0
            for i in range(len(self.objetivos)):
                if (self.posicionEjeX[0] == self.objetivos[i].posicionEjeX
                        and self.posicionEjeY[0] == self.objetivos[i].posicionEjeY):
                    verificarObjetivo = True
                    marcadorObjetivo = i
            if verificarObjetivo:
                self.objetivo_alcanzado(marcadorObjetivo)
            # Bucle que gestiona si se come un obstaculo
            for i in range(len(self.obstaculos)):
                if self.posicionEjeX[0] == self.obstaculos[i].posicionEjeX and self.posicionEjeY[0] == self.obstaculos[i].posicionEjeY:
                    self.estado = 0
            # Bucle que gestiona cuando se come a sí mismo
            for i in range(1,self.longitud):
                if self.posicionEjeX[0] == self.posicionEjeX[i] and self.posicionEjeY[0] == self.posicionEjeY[i]:
                    self.estado = 0
    def objetivo_alcanzado(self,objetivoAlcanzado):
        # Evaluamos la condición de cuando se choquen
        self.longitud=self.longitud+1
        self.posicionEjeX.append(self.colaX)
        self.posicionEjeY.append(self.colaY)
        self.objetivos.pop(objetivoAlcanzado)

class SliderIA():

    def __init__(self, mapa, ejeX, ejeY):
        self.posicionEjeX = [ejeX]
        self.posicionEjeY = [ejeY]
        self.mapa = mapa
        self.direction = "izquierda"

    def Astar(mapa, inicio, objetivo):
        print("Astar")
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

class Nodo():
    def __init__(self, pariente=None, posicion=None):
        self.pariente = pariente
        self.posicion = posicion

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, otro):
        return self.posicion == otro.posicion