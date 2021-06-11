class Snake():

    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        self.cabeza = [ejeX, ejeY]
        self.cuerpo = [[ejeX, ejeY]]
        self.celdas = [celdasX, celdasY]
        self.direccion = "Ninguna"
        self.movimiento = 1
        self.estado = 2

    def cambiaDireccion(self):
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
        if self.direccion != "Ninguna":
            self.moverCuerpo()

    def moverCuerpo(self):
        self.cuerpo.insert(0, list(self.cabeza))


class SnakeIA():
    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        self.posicion = [[ejeX, ejeY]]
        self.celdas = [celdasX, celdasY]
        self.cola = [ejeX, ejeY]
        self.movimiento = 1
        self.direccion = "Derecha"

    def cambiarDireccion(self, direccion):
        if direccion == "Derecha" and not self.direccion == "Izquierda":
            self.direccion = "Derecha"
        if direccion == "Izquierda" and not self.direccion == "Derecha":
            self.direccion = "Izquierda"
        if direccion == "Arriba" and not self.direccion == "Abajo":
            self.direccion = "Arriba"
        if direccion == "Abajo" and not self.direccion == "Arriba":
            self.direccion = "Abajo"

    def mover(self, cp):
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

        if self.posicion[0] == cp:
            self.posicion.append(self.cola)

        if len(self.posicion) > 1:
            contador = 0
            for i in self.posicion:
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
        return self.posicion[0]

    def cuerpo(self):
        contador = 0
        cuerpo = []
        for i in self.posicion:
            if contador > 0:
                cuerpo.append(i)
        return cuerpo