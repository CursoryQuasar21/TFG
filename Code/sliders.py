from objetivo import ObjetivoSimple

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

    #En desarrollo
    def registraObjetivos(self, ejesX, ejesY):
        for i in ejesX:
            self.posicionObjetivoEjeX[i]=ejesX[i]
        for i in ejesY:
            self.posicionObjetivoEjeX[i]=ejesY[i]

    #En desarrollo, hay que mirar el funcionamiento cuando la velocidad es superior a 1
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
        if self.direccion!="ninguna":
            for i in range(0, len(self.objetivos)-1):
                if self.posicionEjeX[0]==self.objetivos[i].posicionEjeX and self.posicionEjeY[0]==self.objetivos[i].posicionEjeY:
                    self.objetivo_alcanzado()
            for i in range(0, len(self.obstaculos)-1):
                if self.posicionEjeX[0]==self.obstaculos[i].posicionEjeX and self.posicionEjeY[0]==self.obstaculos[i].posicionEjeY:
                    self.obstaculo_alcanzado()
    def objetivo_alcanzado(self):
        #Evaluamos la condición de cuando se choquen
        verificadoImpacto=False
        objetivoAlcanzado = 0
        for i in range(0, len(self.objetivos)):
            if self.posicionEjeX[0] == self.objetivos[i].posicionEjeX and self.posicionEjeY[0] == self.objetivos[i].posicionEjeY:
                #Elimina el objetivo alcanzado por la cabeza del slider
                objetivoAlcanzado=i
                verificadoImpacto=True
        if verificadoImpacto:
            self.longitud=self.longitud+1
            self.posicionEjeX.append(self.colaX)
            self.posicionEjeY.append(self.colaY)
            self.objetivos.pop(objetivoAlcanzado)

    def obstaculo_alcanzado(self):
        # Evaluamos la condición de cuando se choquen
        verificadoImpacto = False
        obstaculoAlcanzado = 0
        for i in range(0,len(self.obstaculos)):
            if self.posicionEjeX[0] == self.obstaculos[i].posicionEjeX and self.posicionEjeY[0] == self.obstaculos[i].posicionEjeY:
                # Elimina el objetivo alcanzado por la cabeza del slider
                obstaculoAlcanzado = i
                verificadoImpacto = True
        if verificadoImpacto:
            self.longitud = self.longitud - 1
            self.posicionEjeX.pop()
            self.posicionEjeY.pop()
            self.obstaculos.pop(obstaculoAlcanzado)