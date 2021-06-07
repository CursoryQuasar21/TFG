import pygame

from objetivo import *
from obstaculo import *
from sliders import *

'''
Esta clase se encargara de crear la slider, los obstaculos y objetivos
'''
class Elemento():

    def __init__(self, nxC, nyC, nivel):
        '''
        :param nxC: El numero de celdas del eje X
        :param nyC: El numero de celdas del eje Y
        :param nivel: El nivel de la partida
        '''

        # Creamos la slider
        self.slider = Slider(nxC // 2, nyC // 2, nxC, nyC)

        # Creamos los elementos como objetivos y obstaculos
        self.lista_Objetivos = []
        self.lista_Obstaculos = []
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

        # pruebas
        # Creamos una lista de la cantidad de los diferntes objetivos,
        # ob1-Objetivos de nivel 1, ob2-Objetivos de nivel 2 y ob3-Objetivos de nivel 3
        lista_ContadorObjetivos = [ob1, ob2, ob3]

        # Bucle que se va a encargar de crear tantos objetivos como numero sea la variable
        for obj in range(cantidadObjetivos):

            # La variable verificarCordenada se encarga de confirmar
            # las coordenadas del objetivo que no coincidan con ninguna otra cordenada del juego
            verificarCordenada = True

            # La variable contador se va a encargar de contar que todas las verificaciones en ese momento se cumplan
            contador = 0
            while verificarCordenada:
                lista = [random.randrange(nxC), random.randrange(nyC)]

                # El bucle for se encarga de recorer n veces la cantidad de la longitud del slider
                for s in self.slider.posicion:
                    if len(self.lista_Objetivos) == 0:
                        if len(self.lista_Obstaculos) == 0:
                            # Si las cordenadas aleatorias no coinciden con ninguna coirdenada el contador aumenta
                            if lista != s:
                                contador += 1
                        else:
                            for obs in self.lista_Obstaculos:
                                # Si las cordenadas aleatorias no coinciden con ninguna coirdenada el contador aumenta
                                if lista != s and lista != obs.posicion:
                                    contador += 1
                    else:
                        for obj in self.lista_Objetivos:
                            if len(self.lista_Obstaculos) == 0:
                                # Si las cordenadas aleatorias no coinciden con ninguna coirdenada el contador aumenta
                                if lista != s and lista != obj:
                                    contador += 1
                            else:
                                for obs in self.lista_Obstaculos:
                                    # Si las cordenadas aleatorias no coinciden con ninguna coirdenada el contador aumenta
                                    if lista != s and lista != obj.posicion and lista != obs.posicion:
                                        contador += 1

                    # Ahora comprobaremos si tras todas las comprobaciones las cordenadas dadas no han coincidido con ninguna otra
                    if (contador == self.slider.longitud) \
                        or (contador == (self.slider.longitud*len(self.lista_Obstaculos))) \
                        or (contador == (self.slider.longitud*len(self.lista_Objetivos)))  \
                        or (contador == (self.slider.longitud*len(self.lista_Objetivos)*len(self.lista_Obstaculos))):
                        # Ahora en funcion de la lista de "lista_ContadorObjetivos" crearemos unos u otros objetivos en funcion de la iteracion del bucle
                        if lista_ContadorObjetivos[0] != 0:
                            self.lista_Objetivos.append(ObjetivoSimple(lista[0], lista[1], nxC, nyC))
                            lista_ContadorObjetivos[0] -= 1
                        elif lista_ContadorObjetivos[1] != 0:
                            self.lista_Objetivos.append(ObjetivoMedio(lista[0], lista[1], nxC, nyC))
                            lista_ContadorObjetivos[1] -= 1
                        elif lista_ContadorObjetivos[2] != 0:
                            self.lista_Objetivos.append(ObjetivoDificil(lista[0], lista[1], nxC, nyC))
                            lista_ContadorObjetivos[2] -= 1
                        verificarCordenada = False
        # Una vez hallamos creado todos los objetivos, los pasaremos al slider
        self.slider.objetivos = self.lista_Objetivos

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

        # pruebas
        #lista_ContadorObstaculos = [1,0,0]
        #for obj in range(1):
        cont=0
        # Bucle que se va a encargar de crear tantos obstaculos como numero sea la variable
        for obj in range(cantidadObstaculos):

            # La variable verificarCordenada se encarga de confirmar
            # las coordenadas del objetivo que no coincidan con ninguna otra cordenada del juego
            verificarCordenada = True

            # La variable contador se va a encargar de contar que todas las verificaciones en ese momento se cumplan
            contador = 0

            while verificarCordenada:
                cont += 1
                lista = [random.randrange(nxC), random.randrange(nyC)]

                # El bucle for se encarga de recorer n veces la cantidad de la longitud del slider
                for s in self.slider.posicion:
                    if len(self.lista_Objetivos) == 0:
                        if len(self.lista_Obstaculos) == 0:
                            # Si las cordenadas aleatorias no coinciden con ninguna coirdenada el contador aumenta
                            if lista == s:
                                contador += 1
                        else:
                            for obs in self.lista_Obstaculos:
                                # Si las cordenadas aleatorias no coinciden con ninguna coirdenada el contador aumenta
                                if lista != s and lista != obs.posicion:
                                    contador += 1
                    else:
                        for obj in self.lista_Objetivos:
                            if len(self.lista_Obstaculos) == 0:
                                # Si las cordenadas aleatorias no coinciden con ninguna coirdenada el contador aumenta
                                if lista != s and lista != obj.posicion:
                                    contador += 1
                            else:
                                for obs in self.lista_Obstaculos:
                                    # Si las cordenadas aleatorias no coinciden con ninguna coirdenada el contador aumenta
                                    if lista != s and lista != obj.posicion and lista != obs.posicion:
                                        contador += 1

                    # Ahora comprobaremos si tras todas las comprobaciones las cordenadas dadas no han coincidido con ninguna otra
                    if (contador == self.slider.longitud) \
                            or (contador == (self.slider.longitud * len(self.lista_Obstaculos))) \
                            or (contador == (self.slider.longitud * len(self.lista_Objetivos))) \
                            or (contador == (self.slider.longitud * len(self.lista_Objetivos) * len(self.lista_Obstaculos))):
                        # Ahora en funcion de la lista de "lista_ContadorObjetivos" crearemos unos u otros objetivos en funcion de la iteracion del bucle
                        if lista_ContadorObstaculos[0] != 0:
                            self.lista_Obstaculos.append(ObstaculoSimple(lista[0], lista[1], nxC, nyC))
                            lista_ContadorObstaculos[0] -= 1
                        elif lista_ContadorObstaculos[1] != 0:
                            self.lista_Obstaculos.append(ObstaculoMedio(lista[0], lista[1], nxC, nyC))
                            lista_ContadorObstaculos[1] -= 1
                        elif lista_ContadorObstaculos[2] != 0:
                            self.lista_Obstaculos.append(ObstaculoDificil(lista[0], lista[1], nxC, nyC))
                            lista_ContadorObstaculos[2] -= 1
                        verificarCordenada = False
        # Una vez hallamos creado todos los obstaculos, los pasaremos al slider
        self.slider.obstaculos = self.lista_Obstaculos