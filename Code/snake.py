import numpy as np

class Slider():

    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        '''
        :param ejeX: La posicion en el que se encuentra la cabeza en el ejeX
        :param ejeY: La posicion en el que se encuentra la cabeza en el ejeX
        :param celdasX: La cantidad de celdas en el ejeX
        :param celdasY: La cantidad de celdas en el ejeY
        '''
        self.posicion = [[ejeX, ejeY]]
        self.cola = [ejeX, ejeY]
        self.celdas = [celdasX, celdasY]
        self.direccion = "ninguna"
        self.longitud = 1
        self.movimiento = 1
        self.estado = 2
        # Array que guarda instancias de objetivos
        self.objetivos = []
        # Array que guarda instancias de obstaculos
        self.obstaculos = []

    # En desarrollo, hay que mirar el funcionamiento cuando la velocidad es superior a 1
    def cambiaDireccion(self):
        self.cola = self.posicion[0].copy()
        if self.direccion == "Arriba" and not self.direccion == "Abajo":
            #self.cola[1] = self.posicion[0][1]
            if self.posicion[0][1] == 0 or self.posicion[0][1] < (self.posicion[0][1] - self.movimiento):
                self.posicion[0][1] = self.celdas[1]-1
            else:
                self.posicion[0][1] -= self.movimiento
        elif self.direccion == "Abajo" and not self.direccion == "Arriba":
            #self.cola[1] = self.posicion[0][1]
            if self.posicion[0][1] == self.celdas[1]-1 or self.posicion[0][1] > (self.posicion[0][1] + self.movimiento):
                self.posicion[0][1] = 0
            else:
                self.posicion[0][1] += self.movimiento
        elif self.direccion == "Izquierda" and not self.direccion == "Derecha":
            #self.cola[0] = self.posicion[0][0]
            if self.posicion[0][0] == 0 or self.posicion[0][0] < (self.posicion[0][0] - self.movimiento):
                self.posicion[0][0] = self.celdas[0]-1
            else:
                self.posicion[0][0] -= self.movimiento
        elif self.direccion == "Derecha" and not self.direccion == "Izquierda":
            #self.cola[0] = self.posicion[0][0]
            if self.posicion[0][0] == self.celdas[0] - 1 or self.posicion[0][0] > (self.posicion[0][0] + self.movimiento):
                self.posicion[0][0] = 0
            else:
                self.posicion[0][0] += self.movimiento

        self.verificadorImpacto()

    def verificadorImpacto(self):
        if self.direccion != "ninguna":
            marcadorObjetivo = 0
            for i in self.objetivos:
                if i.posicion == self.posicion[0]:
                    self.objetivo_alcanzado(marcadorObjetivo)
                marcadorObjetivo += 1
            # Bucle que gestiona si se come un obstaculo
            for i in self.obstaculos:
                if i.posicion == self.posicion[0]:
                    print("obstaculo")
                    self.estado = 0
            # Bucle que gestiona cuando se come a sí mismo
            contador = 0
            #for i in self.posicion:
            #    if contador > 0:
            #        if i == self.posicion[0] and self.cola != self.posicion[0]:
            #            self.estado = 0
            #    contador += 1


    def objetivo_alcanzado(self, marcador):
        # Evaluamos la condición de cuando se choquen
        self.longitud = self.longitud + 1
        self.posicion.append(self.cola)
        self.objetivos.pop(marcador)