import random



class ObjetivoSimple():
    posicionEjeX=0
    posicionEjeY=0
    celdasX = 0
    celdasY = 0
    direccion="ninguna"
    movimiento=0
    estado=1

    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        self.posicionEjeX=ejeX
        self.posicionEjeY=ejeY
        self.celdasX=celdasX
        self.celdasY=celdasY
    
    #Método para añadir dificultad al juego
    #Según aumente la dificultad se moverá más rápido
    def cambiaDireccion(self, direccion):
        if self.direccion != "ninguna":
            if self.direccion == "arriba":
                if 0 > (self.posicionEjeY - self.movimiento):
                    if self.posicionEjeY == 0:
                        self.posicionEjeY = self.celdasY - self.movimiento
                    else:
                        self.posicionEjeY = self.celdasY - ((0 - self.posicionEjeY) + self.movimiento)
                else:
                    self.posicionEjeY -= self.movimiento
            elif self.direccion == "abajo":
                if self.celdasY <= (self.posicionEjeY + self.movimiento):
                    if self.posicionEjeY == self.celdasY:
                        self.posicionEjeY = self.movimiento
                    else:
                        self.posicionEjeY = ((self.posicionEjeY - self.celdasY) + self.movimiento)
                else:
                    self.posicionEjeY += self.movimiento
            elif self.direccion == "izquierda":
                if 0 > (self.posicionEjeX - self.movimiento):
                    if self.posicionEjeX == 0:
                        self.posicionEjeX = self.celdasX - self.movimiento
                    else:
                        self.posicionEjeX = self.celdasX - ((0 - self.posicionEjeX) + self.movimiento)
                else:
                    self.posicionEjeX -= self.movimiento
            elif self.direccion == "derecha":
                if self.celdasX <= (self.posicionEjeX + self.movimiento):
                    if self.posicionEjeX == self.celdasX:
                        self.posicionEjeX = self.movimiento
                    else:
                        self.posicionEjeX = ((self.posicionEjeX - self.celdasX) + self.movimiento)
                else:
                    self.posicionEjeX += self.movimiento

class ObjetivoMedio():
    posicionEjeX = 0
    posicionEjeY = 0
    celdasX=0
    celdasY=0
    direccion = "ninguna"
    movimiento = 1
    estado = 1

    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        self.posicionEjeX = ejeX
        self.posicionEjeY = ejeY
        self.celdasX = celdasX
        self.celdasY = celdasY
        lista_Direcciones = ["arriba", "abajo", "izquierda", "derecha"]
        direccion = random.randrange(4)
        self.direccion=lista_Direcciones[direccion]

    # Método para añadir dificultad al juego
    # Según aumente la dificultad se moverá más rápido
    def cambiaDireccion(self, direccion):
        if self.direccion != "ninguna":
            if self.direccion == "arriba":
                if 0 > (self.posicionEjeY - self.movimiento):
                    if self.posicionEjeY == 0:
                        self.posicionEjeY = self.celdasY - self.movimiento
                    else:
                        self.posicionEjeY = self.celdasY - ((0 - self.posicionEjeY) + self.movimiento)
                else:
                    self.posicionEjeY -= self.movimiento
            elif self.direccion == "abajo":
                if self.celdasY <= (self.posicionEjeY + self.movimiento):
                    if self.posicionEjeY == self.celdasY:
                        self.posicionEjeY = self.movimiento
                    else:
                        self.posicionEjeY = ((self.posicionEjeY - self.celdasY) + self.movimiento)
                else:
                    self.posicionEjeY += self.movimiento
            elif self.direccion == "izquierda":
                if 0 > (self.posicionEjeX - self.movimiento):
                    if self.posicionEjeX == 0:
                        self.posicionEjeX = self.celdasX - self.movimiento
                    else:
                        self.posicionEjeX = self.celdasX - ((0 - self.posicionEjeX) + self.movimiento)
                else:
                    self.posicionEjeX -= self.movimiento
            elif self.direccion == "derecha":
                if self.celdasX <= (self.posicionEjeX + self.movimiento):
                    if self.posicionEjeX == self.celdasX:
                        self.posicionEjeX = self.movimiento
                    else:
                        self.posicionEjeX = ((self.posicionEjeX - self.celdasX) + self.movimiento)
                else:
                    self.posicionEjeX += self.movimiento

class ObjetivoDificil():
    posicionEjeX = 0
    posicionEjeY = 0
    celdasX = 0
    celdasY = 0
    direccion="ninguna"
    movimiento = 2
    estado = 1


    def __init__(self, ejeX, ejeY, celdasX, celdasY):
        self.posicionEjeX = ejeX
        self.posicionEjeY = ejeY
        self.celdasX = celdasX
        self.celdasY = celdasY

    # Método para añadir dificultad al juego
    # Según aumente la dificultad se moverá más rápido
    def cambiaDireccion(self, direccion):
        lista_Direcciones = ["arriba", "abajo", "izquierda", "derecha"]
        direccion = random.randrange(4)
        self.direccion = lista_Direcciones[direccion]
        if self.direccion != "ninguna":
            if self.direccion == "arriba":
                if 0 > (self.posicionEjeY - self.movimiento):
                    if self.posicionEjeY == 0:
                        self.posicionEjeY = self.celdasY - self.movimiento
                    else:
                        self.posicionEjeY = self.celdasY - ((0 - self.posicionEjeY) + self.movimiento)
                else:
                    self.posicionEjeY -= self.movimiento
            elif self.direccion == "abajo":
                if self.celdasY <= (self.posicionEjeY + self.movimiento):
                    if self.posicionEjeY == self.celdasY:
                        self.posicionEjeY = self.movimiento
                    else:
                        self.posicionEjeY = ((self.posicionEjeY - self.celdasY) + self.movimiento)
                else:
                    self.posicionEjeY += self.movimiento
            elif self.direccion == "izquierda":
                if 0 > (self.posicionEjeX - self.movimiento):
                    if self.posicionEjeX == 0:
                        self.posicionEjeX = self.celdasX - self.movimiento
                    else:
                        self.posicionEjeX = self.celdasX - ((0 - self.posicionEjeX) + self.movimiento)
                else:
                    self.posicionEjeX -= self.movimiento
            elif self.direccion == "derecha":
                if self.celdasX <= (self.posicionEjeX + self.movimiento):
                    if self.posicionEjeX == self.celdasX:
                        self.posicionEjeX = self.movimiento
                    else:
                        self.posicionEjeX = ((self.posicionEjeX - self.celdasX) + self.movimiento)
                else:
                    self.posicionEjeX += self.movimiento