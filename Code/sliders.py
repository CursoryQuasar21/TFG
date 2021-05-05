class Slider():
    posicionObjetivoEjeX=[]
    posicionObjetivoEjeY=[]
    posicionEjeX=[0]
    posicionEjeY=[0]
    direccion="ninguna"
    longitud=1
    movimiento=1
    estado=1

    def constructor(self,ejeX,ejeY,longitud,movimiento,estado):
        self.posicionEjeX=[ejeX]
        self.posicionEjeY=[ejeY]
        self.longitud=longitud
        self.movimiento=movimiento
        self.estado=estado

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
            self.posicionEjeY[0]-=self.movimiento
        elif direccion=="abajo":
            self.direccion = "abajo"
            self.posicionEjeY[0]+=self.movimiento
        elif direccion=="izquierda":
            self.direccion = "izquierda"
            self.posicionEjeX[0]-=self.movimiento
        elif direccion=="derecha":
            self.direccion = "derecha"
            self.posicionEjeX[0]+=self.movimiento

    def isObjetivosCumplido(self):
        for i in self.posicionObjetivoEjeX:
            if self.posicionEjeX(0)==self.posicionObjetivoEjeX(i) and self.posicionEjeY(0)==self.posicionObjetivoEjeY(i):
                self.longitud=+1
                #Falta Añadir el nombre y el metodo(este fuera de este metodo) que alfinal del guasano, al pasar por el punto del objetivo se haga mas largo
                return True