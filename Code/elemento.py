from objetivo import *
from obstaculo import *
from snake import *
from mapa import *
'''
Esta clase se encargara de crear la snake, los obstaculos y objetivos
'''
class Elemento():

    def __init__(self, nxC, nyC, nivel):
        '''
        :param nxC: El numero de celdas del eje X
        :param nyC: El numero de celdas del eje Y
        :param nivel: El nivel de la partida
        '''

        # Creamos la snake
        self.snake = Snake(nxC // 2, nyC // 2, nxC, nyC)

        # Creamos los elementos como objetivos y obstaculos
        self.lista_Objetivos = []
        self.lista_Obstaculos = []

        # Creo y guardo una matriz poniendo todos los valores a cero
        self.mapa = Mapa(nxC, nyC)

        self.creadorObjetivos(nivel, nxC, nyC)
        self.creadorObstaculos(nivel, nxC, nyC)


    def cantidadObjetivos(self, nivel, nxC, nyC):
        '''
        :param nivel: El nivel de la partida en el momento actual
        :param nxC: La cantidad de celdas en el eje X
        :param nyC: La cantidad de celdas en el eje Y
        :return: Va a devolver una cantidad de objetivos en funcion del nivel y las dimensiones
        '''

        # Obtenemos una cantidad de objetivos en funcion de las dimensiones
        cantidadObjetivos = (nxC * nyC) // (nxC + nyC)

        # El grupo de condiciones que determinaran la cantidad extra de objetivos
        if nivel == "facil":
            cantidadObjetivos += 5
        elif nivel == "medio":
            cantidadObjetivos += 3
        elif nivel == "dificil":
            cantidadObjetivos += 1
        else:
            cantidadObjetivos -= 3

        # Devuelve la cantidad de objetivos
        return cantidadObjetivos

    def cantidadObstaculos(self, nivel, nxC, nyC):
        '''
        :param nivel: El nivel de la partida en el momento actual
        :param nxC: La cantidad de celdas en el eje X
        :param nyC: La cantidad de celdas en el eje Y
        :return: Va a devolver una cantidad de obstaculos en funcion del nivel y las dimensiones
        '''

        # Obtenemos una cantidad de obstaculos en funcion de las dimensiones
        cantidadObstaculos = (nxC * nyC) // (nxC + nyC)

        # El grupo de condiciones que determinaran la cantidad extra de obstaculos
        if nivel == "facil":
            cantidadObstaculos -= 3
        elif nivel == "medio":
            cantidadObstaculos += 1
        elif nivel == "dificil":
            cantidadObstaculos += 3
        else:
            cantidadObstaculos += 5

        # Devuelve la cantidad de obstaculos
        return cantidadObstaculos

    def creadorObjetivos(self, nivel, nxC, nyC):
        '''
        :param nivel: El nivel de la partida en el momento actual
        :param cantidadObjetivos: La cantidad de objetivos
        :param nxC: La cantidad de celdas en el eje X
        :param nyC: La cantidad de celdas en el eje Y
        :return: No devuelve nada de manera explicita pero si que modifica atributos de clase
        '''

        cantidadObjetivos = self.cantidadObjetivos(nivel, nxC, nyC)
        # Grupo de condiciones que se encargan de en funcion del nivel crear diferentes tipos de objetivos
        if nivel == "facil":
            ob1 = int(cantidadObjetivos - (cantidadObjetivos * 0.3))
            ob2 = int(cantidadObjetivos - ob1)
            ob3 = 0

        elif nivel == "medio":
            ob1 = int(cantidadObjetivos - (cantidadObjetivos * 0.4))
            ob2 = int((cantidadObjetivos - ob1) * 0.5)
            ob3 = int((cantidadObjetivos - (ob1+ob2)))

        elif nivel == "dificil":
            ob1 = int(cantidadObjetivos - (cantidadObjetivos * 0.9))
            ob2 = int((cantidadObjetivos - ob1) * 0.7)
            ob3 = int(cantidadObjetivos - (ob1 + ob2))
        else:
            ob1 = 0
            ob2 = int((cantidadObjetivos - ob1) * 0.7)
            ob3 = int(cantidadObjetivos - (ob1 + ob2))

        # Creamos una lista de la cantidad de los diferntes objetivos,
        # ob1-Objetivos de nivel 1, ob2-Objetivos de nivel 2 y ob3-Objetivos de nivel 3
        lista_ContadorObjetivos = [ob1, ob2, ob3]

        lista_Posiciones_Vacias = []

        for i in self.snake.cuerpo:
            self.mapa.mapa[i[0], i[1]] = 2
        for i in self.lista_Obstaculos:
            self.mapa.mapa[i[0], i[1]] = 3

        for i in range(nxC):
            for z in range(nyC):
                if self.mapa.mapa[i][z] == 0:
                    lista_Posiciones_Vacias.append([i, z])

        # Bucle que se va a encargar de crear tantos objetivos como numero sea la variable
        for obj in range(cantidadObjetivos):
            var = random.randrange(len(lista_Posiciones_Vacias))
            pos = lista_Posiciones_Vacias[var]
            self.mapa.mapa[pos[0], pos[1]] = 1
            lista_Posiciones_Vacias.pop(var)
            # Ahora en funcion de la lista de "lista_ContadorObjetivos" crearemos unos u otros objetivos en funcion de la iteracion del bucle
            if lista_ContadorObjetivos[0] != 0:
                self.lista_Objetivos.append(ObjetivoSimple(pos[0], pos[1], nxC, nyC))
                lista_ContadorObjetivos[0] -= 1
            elif lista_ContadorObjetivos[1] != 0:
                self.lista_Objetivos.append(ObjetivoMedio(pos[0], pos[1], nxC, nyC))
                lista_ContadorObjetivos[1] -= 1
            elif lista_ContadorObjetivos[2] != 0:
                self.lista_Objetivos.append(ObjetivoDificil(pos[0], pos[1], nxC, nyC))
                lista_ContadorObjetivos[2] -= 1

    def creadorObstaculos(self, nivel, nxC, nyC):
        '''
        :param nivel: El nivel de la partida en el momento actual
        :param cantidadObstaculos: La cantidad de objetivos
        :param nxC: La cantidad de celdas en el eje X
        :param nyC: La cantidad de celdas en el eje Y
        :return: No devuelve nada de manera explicita pero si que modifica atributos de clase
        '''

        cantidadObstaculos = self.cantidadObstaculos(nivel, nxC, nyC)
        # Grupo de condiciones que se encargan de en funcion del nivel crear diferentes tipos de obstaculos
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

        # Creamos una lista de la cantidad de los diferntes obstaculos,
        # ob1-obstaculos de nivel 1, ob2-obstaculos de nivel 2 y ob3-obstaculos de nivel 3
        lista_ContadorObstaculos = [ob1, ob2, ob3]

        lista_Posiciones_Vacias = []

        for i in self.lista_Objetivos:
            self.mapa.mapa[i.posicion[0], i.posicion[1]] = 1
        for i in self.snake.cuerpo:
            self.mapa.mapa[i[0], i[1]] = 2
        for i in self.lista_Obstaculos:
            self.mapa.mapa[i.posicion[0], i.posicion[1]] = 3

        for i in range(nxC):
            for z in range(nyC):
                if self.mapa.mapa[i][z] == 0:
                    lista_Posiciones_Vacias.append([i, z])

        # Bucle que se va a encargar de crear tantos objetivos como numero sea la variable
        for obj in range(cantidadObstaculos):
            var = random.randrange(len(lista_Posiciones_Vacias))
            pos = lista_Posiciones_Vacias[var]
            self.mapa.mapa[pos[0], pos[1]] = 1
            lista_Posiciones_Vacias.pop(var)
            # Ahora en funcion de la lista de "lista_ContadorObjetivos" crearemos unos u otros objetivos en funcion de la iteracion del bucle
            if lista_ContadorObstaculos[0] != 0:
                self.lista_Obstaculos.append(ObstaculoSimple(pos[0], pos[1], nxC, nyC))
                lista_ContadorObstaculos[0] -= 1
            elif lista_ContadorObstaculos[1] != 0:
                self.lista_Obstaculos.append(ObstaculoMedio(pos[0], pos[1], nxC, nyC))
                lista_ContadorObstaculos[1] -= 1
            elif lista_ContadorObstaculos[2] != 0:
                self.lista_Obstaculos.append(ObstaculoDificil(pos[0], pos[1], nxC, nyC))
                lista_ContadorObstaculos[2] -= 1

    def movimiento(self,newMapa):
        for i in self.lista_Objetivos:
            newMapa[i.posicion[0], i.posicion[1]] = 0
            i.cambiaDireccion()
            newMapa[i.posicion[0], i.posicion[1]] = 1
        for i in self.lista_Obstaculos:
            newMapa[i.posicion[0], i.posicion[1]] = 0
            i.cambiaDireccion()
            newMapa[i.posicion[0], i.posicion[1]] = 3
        for i in self.snake.cuerpo:
            newMapa[i[0], i[1]] = 0
        self.snake.cambiaDireccion()
        if self.snake.direccion != "Ninguna":
            self.verificadorPosicion()
        for i in self.snake.cuerpo:
            newMapa[i[0], i[1]] = 2
        return newMapa

    def verificadorPosicion(self):
        if self.mapa.mapa[self.snake.cabeza[0], self.snake.cabeza[1]] == 0:
            self.snake.cuerpo.pop()
        elif self.mapa.mapa[self.snake.cabeza[0], self.snake.cabeza[1]] == 1:
            for i in self.lista_Objetivos:
                if i.posicion == self.snake.cabeza:
                    self.snake.cuerpo.insert(0, list(i.posicion))
        else:
            self.snake.estado = 0
