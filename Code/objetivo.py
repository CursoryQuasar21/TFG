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
        if direccion != "ninguna":
            if direccion == "arriba":
                if self.posicionEjeY == 0 or self.posicionEjeY < (self.posicionEjeY - self.movimiento):
                    self.posicionEjeY = self.celdasY - 1
                else:
                    self.posicionEjeY -= self.movimiento
            elif direccion == "abajo":
                self.colaY = self.posicionEjeY
                if self.posicionEjeY == self.celdasY - 1 or self.posicionEjeY > (self.posicionEjeY + self.movimiento):
                    self.posicionEjeY = 0
                else:
                    self.posicionEjeY += self.movimiento
            elif direccion == "izquierda":
                self.colaX = self.posicionEjeX
                if self.posicionEjeX == 0 or self.posicionEjeX < (self.posicionEjeX - self.movimiento):
                    self.posicionEjeX = self.celdasX - 1
                else:
                    self.posicionEjeX -= self.movimiento
            elif direccion == "derecha":
                self.colaX = self.posicionEjeX
                if self.posicionEjeX == self.celdasX - 1 or self.posicionEjeX > (
                        self.posicionEjeX + self.movimiento):
                    self.posicionEjeX = 0
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
        direccion = random.randrange(3)
        self.direccion=lista_Direcciones[direccion]

    # Método para añadir dificultad al juego
    # Según aumente la dificultad se moverá más rápido
    def cambiaDireccion(self, direccion):
        if direccion!="ninguna":
            if direccion == "arriba":
                if self.posicionEjeY == 0 or self.posicionEjeY < (self.posicionEjeY - self.movimiento):
                    self.posicionEjeY = self.celdasY - 1
                else:
                    self.posicionEjeY -= self.movimiento
            elif direccion == "abajo":
                self.colaY = self.posicionEjeY
                if self.posicionEjeY == self.celdasY - 1 or self.posicionEjeY > (self.posicionEjeY + self.movimiento):
                    self.posicionEjeY = 0
                else:
                    self.posicionEjeY += self.movimiento
            elif direccion == "izquierda":
                self.colaX = self.posicionEjeX
                if self.posicionEjeX == 0 or self.posicionEjeX < (self.posicionEjeX - self.movimiento):
                    self.posicionEjeX = self.celdasX - 1
                else:
                    self.posicionEjeX -= self.movimiento
            elif direccion == "derecha":
                self.colaX = self.posicionEjeX
                if self.posicionEjeX == self.celdasX - 1 or self.posicionEjeX > (
                        self.posicionEjeX + self.movimiento):
                    self.posicionEjeX = 0
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
        lista_Direcciones = ["arriba", "abajo", "izquierda", "derecha"]

    # Método para añadir dificultad al juego
    # Según aumente la dificultad se moverá más rápido
    def cambiaDireccion(self, direccion):
        lista_Direcciones = ["arriba", "abajo", "izquierda", "derecha"]
        direccion = random.randrange(3)
        self.direccion = lista_Direcciones[direccion]
        if direccion != "ninguna":
            if direccion == "arriba":
                if self.posicionEjeY == 0 or self.posicionEjeY < (self.posicionEjeY - self.movimiento):
                    self.posicionEjeY = self.celdasY - 1
                else:
                    self.posicionEjeY -= self.movimiento
            elif direccion == "abajo":
                self.colaY = self.posicionEjeY
                if self.posicionEjeY == self.celdasY - 1 or self.posicionEjeY > (self.posicionEjeY + self.movimiento):
                    self.posicionEjeY = 0
                else:
                    self.posicionEjeY += self.movimiento
            elif direccion == "izquierda":
                self.colaX = self.posicionEjeX
                if self.posicionEjeX == 0 or self.posicionEjeX < (self.posicionEjeX - self.movimiento):
                    self.posicionEjeX = self.celdasX - 1
                else:
                    self.posicionEjeX -= self.movimiento
            elif direccion == "derecha":
                self.colaX = self.posicionEjeX
                if self.posicionEjeX == self.celdasX - 1 or self.posicionEjeX > (
                        self.posicionEjeX + self.movimiento):
                    self.posicionEjeX = 0
                else:
                    self.posicionEjeX += self.movimiento
