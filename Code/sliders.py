class Slider():
    #Posiciones de los objetivos
    posicionObjetivoEjeX=[]
    posicionObjetivoEjeY=[]
    #Dimensiones del mapa
    celdasX=0
    celdasY=0
    #Slider basado en dos listas
    posicionEjeX = []
    posicionEjeY = []
    #Atributos del slider
    direccion="ninguna"
    longitud=1
    movimiento=1
    estado=1
    colaX=0
    colaY=0

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

    def cambiaDireccion(self,eje,direccion):
        if direccion=="arriba":
            self.direccion="arriba"
            self.colaY=self.posicionEjeY[eje]
            if self.posicionEjeY[eje]==0 or self.posicionEjeY[eje]<(self.posicionEjeY[eje]-self.movimiento):
                self.posicionEjeY[eje]=self.celdasY-1
            else:
                self.posicionEjeY[eje]-=self.movimiento
        elif direccion=="abajo":
            self.direccion = "abajo"
            self.colaY = self.posicionEjeY[eje]
            if self.posicionEjeY[eje]==self.celdasY-1 or self.posicionEjeY[eje]>(self.posicionEjeY[eje]+self.movimiento):
                self.posicionEjeY[eje]=0
            else:
                self.posicionEjeY[eje]+=self.movimiento
        elif direccion=="izquierda":
            self.direccion = "izquierda"
            self.colaX = self.posicionEjeX[eje]
            if self.posicionEjeX[eje]==0 or self.posicionEjeX[eje]<(self.posicionEjeX[eje] - self.movimiento):
                self.posicionEjeX[eje]=self.celdasX-1
            else:
                self.posicionEjeX[eje]-=self.movimiento
        elif direccion=="derecha":
            self.direccion = "derecha"
            self.colaX = self.posicionEjeX[eje]
            if self.posicionEjeX[eje]==self.celdasX-1 or self.posicionEjeX[eje]>(self.posicionEjeX[eje]+self.movimiento):
                self.posicionEjeX[eje]=0
            else:
                self.posicionEjeX[eje]+=self.movimiento

    def isObjetivosCumplido(self):
        for i in self.posicionObjetivoEjeX:
            if self.posicionEjeX(0)==self.posicionObjetivoEjeX(i) and self.posicionEjeY(0)==self.posicionObjetivoEjeY(i):
                self.longitud=+1
                #Falta Añadir el nombre y el metodo(este fuera de este metodo) que alfinal del guasano, al pasar por el punto del objetivo se haga mas largo
                return True