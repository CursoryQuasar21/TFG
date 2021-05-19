class Slider():
    #Array que guarda instancias de objetivos
    objetivos = []
    # Array que guarda instancias de obstaculos
    obstaculos = []
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
    estado=2
    colaX=0
    colaY=0

    def __init__(self,ejeX,ejeY,longitud,movimiento):
        self.posicionEjeX=[ejeX]
        self.posicionEjeY=[ejeY]
        self.longitud=longitud
        self.movimiento=movimiento
        self.colaX=ejeX
        self.colaY=ejeY
        if longitud>1:
            for i in range(self.longitud):
                self.posicionEjeX.append(self.posicionEjeX[i])
                self.posicionEjeY.append(self.posicionEjeY[i-1]-1)


    #En desarrollo, hay que mirar el funcionamiento cuando la velocidad es superior a 1
    def cambiaDireccion(self,eje,direccion):
        if direccion=="arriba":
            self.direccion="arriba"
            self.colaY=self.posicionEjeY[0]
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

        if self.direccion!="ninguna":
            verificarObjetivo=False
            marcadorObjetivo=0
            for i in range(len(self.objetivos)):
                if (self.posicionEjeX[0]==self.objetivos[i].posicionEjeX and self.posicionEjeY[0]==self.objetivos[i].posicionEjeY):
                    verificarObjetivo=True
                    marcadorObjetivo=i
            if verificarObjetivo:
                self.objetivo_alcanzado(marcadorObjetivo)
            for i in range(len(self.obstaculos)):
                if self.posicionEjeX[0] == self.obstaculos[i].posicionEjeX and self.posicionEjeY[0] == self.obstaculos[i].posicionEjeY:
                    self.estado = 0
            for i in range(1,self.longitud):
                if self.posicionEjeX[0] == self.posicionEjeX[i] and self.posicionEjeY[0] == self.posicionEjeY[i]:
                    self.estado = 0
    def objetivo_alcanzado(self,objetivoAlcanzado):
        #Evaluamos la condición de cuando se choquen
        self.longitud=self.longitud+1
        self.posicionEjeX.append(self.colaX)
        self.posicionEjeY.append(self.colaY)
        self.objetivos.pop(objetivoAlcanzado)