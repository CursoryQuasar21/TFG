class ObjetivoSimple():
    posicionEjeX=0
    posicionEjeY=0
    movimiento=0
    estado=1

    def __init__(self,ejeX,ejeY):
        self.posicionEjeX=ejeX
        self.posicionEjeY=ejeY
    
    #Método para añadir dificultad al juego
    #Según aumente la dificultad se moverá más rápido
    def cambiaPosicion(self,direccion):
        if direccion=="arriba":
            for i in self.posicionEjeX:
                self.posicionEjeX[i] -= self.movimiento
        elif direccion=="abajo":
            for i in self.posicionEjeX:
                self.posicionEjeX[i] += self.movimiento
        elif direccion=="iquierda":
            for i in self.posicionEjeY:
                self.posicionEjeY[i] -= self.movimiento
        else:
            for i in self.posicionEjeY:
                self.posicionEjeY[i] += self.movimiento