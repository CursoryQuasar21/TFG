class ObjetivoSimple():
    posicionEjeX=0
    posicionEjeY=0
    movimiento=0
    estado=2

    def constructor(self,ejeX,ejeY,movimiento):
        self.posicionEjeX=ejeX
        self.posicionEjeY=ejeY
        self.movimiento=movimiento

    def cambiaPosicion(self,direccion):
        if direccion=="arriba":
            for i in self.posicionEjeX:
                self.posicionEjeX[i] = -self.movimiento
        elif direccion=="abajo":
            for i in self.posicionEjeX:
                self.posicionEjeX[i]=+self.movimiento
        elif direccion=="iquierda":
            for i in self.posicionEjeY:
                self.posicionEjeY[i]=-self.movimiento
        else:
            for i in self.posicionEjeY:
                self.posicionEjeY[i]=+self.movimiento