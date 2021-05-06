class Slider():
    posicionObjetivoEjeX=[1]
    posicionObjetivoEjeY=[1]
    #Slider basado en dos listas
    posicionEjeX=[1]
    posicionEjeY=[1]

    celdasX=0
    celdasY=0
    direccion="ninguna"
    longitud=1
    movimiento=1
    estado=1

    def __init__(self,ejeX,ejeY,longitud,movimiento):
        self.posicionEjeX=[ejeX]
        self.posicionEjeY=[ejeY]
        self.longitud=longitud
        self.movimiento=movimiento

    def dimensionesMapa(self, celdasX, celdasY):
        self.celdasX=celdasX
        self.celdasY=celdasY

    def registraObjetivos(self, ejesX, ejesY):
        for i in ejesX:
            self.posicionObjetivoEjeX[i]=ejesX[i]
        for i in ejesY:
            self.posicionObjetivoEjeX[i]=ejesY[i]

    def aumentarLongitud(self):
        self.longitud+=1

    def disminuirLongitud(self):
        self.longitud-=1

    def cambiaDireccion(self,direccion):
        if direccion=="arriba":
            self.direccion="arriba"
            for i in range(0, len(self.posicionEjeY)):
                if self.posicionEjeY[i]==0 or self.posicionEjeY[i]<(self.posicionEjeY[i]-self.movimiento):
                    self.posicionEjeY[i]=self.celdasY-1
                else:
                    self.posicionEjeY[0]-=self.movimiento
        elif direccion=="abajo":
            self.direccion = "abajo"
            for i in range(0, len(self.posicionEjeY)):
                if self.posicionEjeY[i]==self.celdasY-1 or self.posicionEjeY[i]>(self.posicionEjeY[i]+self.movimiento):
                    self.posicionEjeY[i]=0
                else:
                    self.posicionEjeY[0]+=self.movimiento
        elif direccion=="izquierda":
            self.direccion = "izquierda"
            for i in range(0, len(self.posicionEjeX)):
                if self.posicionEjeX[i]==0 or self.posicionEjeX[i]<(self.posicionEjeX[i] - self.movimiento):
                    self.posicionEjeX[i]=self.celdasX-1
                else:
                    self.posicionEjeX[0]-=self.movimiento
        elif direccion=="derecha":
            self.direccion = "derecha"
            for i in range(0, len(self.posicionEjeX)):
                if self.posicionEjeX[i]==self.celdasX-1 or self.posicionEjeX[i]>(self.posicionEjeX[i]+self.movimiento):
                    self.posicionEjeX[i]=0
                else:
                    self.posicionEjeX[0]+=self.movimiento

    def isObjetivosCumplido(self):
        for i in self.posicionObjetivoEjeX:
            if self.posicionEjeX(0)==self.posicionObjetivoEjeX(i) and self.posicionEjeY(0)==self.posicionObjetivoEjeY(i):
                self.longitud=+1
                #Falta Añadir el nombre y el metodo(este fuera de este metodo) que alfinal del guasano, al pasar por el punto del objetivo se haga mas largo
                return True