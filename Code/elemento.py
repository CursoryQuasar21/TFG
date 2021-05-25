from objetivo import*
from obstaculo import*
from sliders import Slider


class Elementos():
    slider = 0
    lista_Objetivos = []
    lista_Obstaculos = []


    def __init__(self, nxC, nyC, nivel):
        cantidadObjetivos = (nxC * nyC) // (nxC+nyC)
        cantidadObstaculos = (nxC * nyC) // (nxC+nyC)

        if nivel == "facil":
            movimiento=0
            cantidadObjetivos += 5
            cantidadObstaculos -= 3
        elif nivel == "medio":
            movimiento = 1
            cantidadObjetivos += 3
            cantidadObstaculos += 1
        elif nivel == "dificil":
            movimiento = 2
            cantidadObjetivos += 1
            cantidadObstaculos += 3
        else:
            movimiento = 3
            cantidadObjetivos -= 1
            cantidadObstaculos += 5
        # Creamos la slider
        self.slider = Slider(nxC // 2, nyC // 2,1)
        self.slider.celdasX = nxC
        self.slider.celdasY = nyC
        # Creamos los elementos como objetivos y obstaculos
        self.lista_Objetivos=[]
        self.lista_Obstaculos=[]
        self.creadorObjetivos(nivel, cantidadObjetivos, nxC, nyC)
        self.creadorObstaculos(nivel, cantidadObstaculos, nxC, nyC)

    def cantidadObjetivos(self,nivel,nxC,nyC):
        cantidadObjetivos = (nxC * nyC) // (nxC + nyC)
        if nivel == "facil":
            cantidadObjetivos += 5
        elif nivel == "medio":
            cantidadObjetivos += 3
        elif nivel == "dificil":
            cantidadObjetivos += 1
        else:
            cantidadObjetivos -= 1
        return cantidadObjetivos

    def cantidadObstaculos(self,nivel,nxC,nyC):
        cantidadObstaculos = (nxC * nyC) // (nxC + nyC)
        if nivel == "facil":
            cantidadObstaculos -= 3
        elif nivel == "medio":
            cantidadObstaculos += 1
        elif nivel == "dificil":
            cantidadObstaculos += 3
        else:
            cantidadObstaculos += 5
        return cantidadObstaculos

    def creadorObjetivos(self, nivel, cantidadObjetivos, nxC, nyC):
        if nivel == "facil":
            ob1 = int(cantidadObjetivos - (cantidadObjetivos * 0.3))
            ob2 = int(cantidadObjetivos - ob1)
            ob3 = 0

        elif nivel == "medio":
            ob1 = int(cantidadObjetivos - (cantidadObjetivos * 0.4))
            ob2 = int((cantidadObjetivos - ob1) * 0.5)
            ob3 = int((cantidadObjetivos - (ob1+ob2)))

        elif nivel == "dificil":
            ob1 = int(cantidadObjetivos - (cantidadObjetivos * 0.1))
            ob2 = int((cantidadObjetivos - ob1) * 0.5)
            ob3 = int(cantidadObjetivos - (ob1 + ob2))
        else:
            ob1 = 0
            ob2 = int((cantidadObjetivos - ob1) * 0.7)
            ob3 = int(cantidadObjetivos - (ob1 + ob2))


        #lista_ContadorObjetivos = [1,0,0]
        #for obj in range(1):
        lista_ContadorObjetivos = [ob1, ob2, ob3]
        for obj in range(cantidadObjetivos):
            verificarCordenada = True
            contador = 0
            while verificarCordenada:
                ejeX = random.randrange(nxC)
                ejeY = random.randrange(nyC)
                for s in range(self.slider.longitud):
                    if len(self.lista_Objetivos) == 0:
                        if len(self.lista_Obstaculos) == 0:
                            if ejeX != self.slider.posicionEjeX[s] or ejeY != self.slider.posicionEjeY[s]:
                                contador += 1
                        else:
                            for obs in range(len(self.lista_Obstaculos)):
                                if (ejeX!=self.slider.posicionEjeX[s] or ejeY != self.slider.posicionEjeY[s]) \
                                        and (ejeX != self.lista_Obstaculos[obs].posicionEjeX or ejeY != self.lista_Obstaculos[obs].posicionEjeY):
                                    contador+=1
                    else:
                        for obj in range(len(self.lista_Objetivos)):
                            if len(self.lista_Obstaculos) == 0:
                                if (ejeX != self.slider.posicionEjeX[s] or ejeY != self.slider.posicionEjeY[s]) \
                                        and (ejeX != self.lista_Objetivos[obj].posicionEjeX or ejeY != self.lista_Objetivos[obj].posicionEjeY):
                                    contador += 1
                            else:
                                for obz in range(len(self.lista_Obstaculos)):
                                    if (ejeX != self.slider.posicionEjeX[s] or ejeY != self.slider.posicionEjeY[s]) \
                                        and (ejeX != self.lista_Objetivos[obj].posicionEjeX or ejeY != self.lista_Objetivos[obj].posicionEjeY) \
                                            and (ejeX != self.lista_Obstaculos[obz].posicionEjeX or ejeY != self.lista_Obstaculos[obz].posicionEjeY):
                                        contador += 1
                    if (contador == self.slider.longitud) \
                        or (contador == (self.slider.longitud*len(self.lista_Obstaculos))) \
                        or (contador == (self.slider.longitud*len(self.lista_Objetivos)))  \
                        or (contador == (self.slider.longitud*len(self.lista_Objetivos)*len(self.lista_Obstaculos))):
                        if lista_ContadorObjetivos[0] != 0:
                            self.lista_Objetivos.append(ObjetivoSimple(ejeX, ejeY, nxC, nyC))
                            lista_ContadorObjetivos[0] -= 1
                        elif lista_ContadorObjetivos[1] != 0:
                            self.lista_Objetivos.append(ObjetivoMedio(ejeX, ejeY, nxC, nyC))
                            lista_ContadorObjetivos[1] -= 1
                        elif lista_ContadorObjetivos[2] != 0:
                            self.lista_Objetivos.append(ObjetivoDificil(ejeX, ejeY, nxC, nyC))
                            lista_ContadorObjetivos[2] -= 1
                        verificarCordenada = False
        self.slider.objetivos=self.lista_Objetivos
    def creadorObstaculos(self, nivel, cantidadObstaculos, nxC, nyC):
        if nivel == "facil":
            ob1 = int(cantidadObstaculos - (cantidadObstaculos * 0.3))
            ob2 = int(cantidadObstaculos - ob1)
            ob3 = 0

        elif nivel == "medio":
            ob1 = int(cantidadObstaculos - (cantidadObstaculos * 0.4))
            ob2 = int((cantidadObstaculos - ob1) * 0.5)
            ob3 = int((cantidadObstaculos - (ob1 + ob2)))

        elif nivel == "dificil":
            ob1 = int(cantidadObstaculos - (cantidadObstaculos * 0.1))
            ob2 = int((cantidadObstaculos - ob1) * 0.5)
            ob3 = int(cantidadObstaculos - (ob1 + ob2))
        else:
            ob1 = 0
            ob2 = int((cantidadObstaculos - ob1) * 0.7)
            ob3 = int(cantidadObstaculos - (ob1 + ob2))

        lista_ContadorObstaculos = [ob1, ob2, ob3]
        for obj in range(cantidadObstaculos):
            verificarCordenada = True
            contador = 0
            while verificarCordenada:
                ejeX = random.randrange(nxC)
                ejeY = random.randrange(nyC)
                for s in range(self.slider.longitud):
                    if len(self.lista_Obstaculos) == 0:
                        if len(self.lista_Objetivos) == 0:
                            if ejeX != self.slider.posicionEjeX[s] or ejeY != self.slider.posicionEjeY[s]:
                                contador += 1
                        else:
                            for obj in range(len(self.lista_Objetivos)):
                                if (ejeX != self.slider.posicionEjeX[s] or ejeY != self.slider.posicionEjeY[s]) \
                                        and (ejeX != self.lista_Objetivos[obj].posicionEjeX or ejeY != self.lista_Objetivos[obj].posicionEjeY):
                                    contador += 1
                    else:
                        for obs in range(len(self.lista_Obstaculos)):
                            if len(self.lista_Objetivos) == 0:
                                if (ejeX != self.slider.posicionEjeX[s] or ejeY != self.slider.posicionEjeY[s]) \
                                        and (ejeX != self.lista_Obstaculos[obs].posicionEjeX or ejeY != self.lista_Obstaculos[obs].posicionEjeY):
                                    contador += 1
                            else:
                                for obj in range(len(self.lista_Objetivos)):
                                    if (ejeX != self.slider.posicionEjeX[s] or ejeY != self.slider.posicionEjeY[s]) \
                                            and (ejeX != self.lista_Obstaculos[obs].posicionEjeX or ejeY != self.lista_Obstaculos[obs].posicionEjeY) \
                                            and (ejeX != self.lista_Objetivos[obj].posicionEjeX or ejeY != self.lista_Objetivos[obj].posicionEjeY):
                                        contador += 1
                    if (contador == self.slider.longitud) \
                            or (contador == (self.slider.longitud * len(self.lista_Objetivos))) \
                            or (contador == (self.slider.longitud * len(self.lista_Obstaculos))) \
                            or (contador == (self.slider.longitud * len(self.lista_Objetivos) * len(self.lista_Obstaculos))):
                        if lista_ContadorObstaculos[0] != 0:
                            self.lista_Obstaculos.append(ObstaculoSimple(ejeX, ejeY, nxC, nyC))
                            lista_ContadorObstaculos[0] -= 1
                        elif lista_ContadorObstaculos[1] != 0:
                            self.lista_Obstaculos.append(ObstaculoMedio(ejeX, ejeY, nxC, nyC))
                            lista_ContadorObstaculos[1] -= 1
                        elif lista_ContadorObstaculos[2] != 0:
                            self.lista_Obstaculos.append(ObstaculoDificil(ejeX, ejeY, nxC, nyC))
                            lista_ContadorObstaculos[2] -= 1
                        verificarCordenada = False

        self.slider.obstaculos=self.lista_Obstaculos