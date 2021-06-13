from objetivo import *
from obstaculo import *
from snake import *
from mapa import *

class Elemento:
    """
    Esta clase se encargara de crear la snake, el mapa, los obstaculos y objetivos
    """

    def __init__(self, nxC, nyC, nivel):
        """
        :param nxC: El numero de celdas del eje X
        :param nyC: El numero de celdas del eje Y
        :param nivel: El nivel de la partida
        """

        # Creamos la snake
        self.snake = Snake(nxC // 2, nyC // 2, nxC, nyC)

        # Creamos los elementos como objetivos y obstaculos
        self.lista_Objetivos = []
        self.lista_Obstaculos = []

        # Creo y guardo una matriz poniendo todos los valores a cero
        self.mapa = Mapa(nxC, nyC)

        # LLamamos a los metodos encargados de crear las listas de objetivos y obstaculos
        self.creadorObjetivos(nivel, nxC, nyC)
        self.creadorObstaculos(nivel, nxC, nyC)

    @staticmethod
    def cantidadObjetivos(nivel, nxC, nyC):
        """
        :param nivel: El nivel de la partida en el momento actual
        :param nxC: La cantidad de celdas en el eje X
        :param nyC: La cantidad de celdas en el eje Y
        :return: Va a devolver una cantidad de objetivos en funcion del nivel y las dimensiones
        """

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

    @staticmethod
    def cantidadObstaculos(nivel, nxC, nyC):
        """
        :param nivel: El nivel de la partida en el momento actual
        :param nxC: La cantidad de celdas en el eje X
        :param nyC: La cantidad de celdas en el eje Y
        :return: Va a devolver una cantidad de obstaculos en funcion del nivel y las dimensiones
        """

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
        """
        :param nivel: El nivel de la partida en el momento actual
        :param nxC: La cantidad de celdas en el eje X
        :param nyC: La cantidad de celdas en el eje Y
        :return: No devuelve nada de manera explicita pero si que modifica atributos de clase
        """

        # Obtenemos la cantidad de objetivos segun diferentes factores
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

        # Esta lista se encarga de registrar que posiciones del mapa estan vacias
        lista_Posiciones_Vacias = []

        # Colocamos la snake en el mapa
        for i in self.snake.cuerpo:
            self.mapa.mapa[i[0], i[1]] = 2

        # Colocamos los obstaculos en el mapa
        for i in self.lista_Obstaculos:
            self.mapa.mapa[i[0], i[1]] = 3

        # Recorremos el mapa y todos aquellas posiciones que esten vacias las guardamos
        for i in range(nxC):
            for z in range(nyC):
                if self.mapa.mapa[i][z] == 0:
                    lista_Posiciones_Vacias.append([i, z])

        # Bucle que se va a encargar de crear tantos objetivos como numero sea la variable
        for obj in range(cantidadObjetivos):
            # Generamos un numero aleatorio de la lista de posiciones vacias
            var = random.randrange(len(lista_Posiciones_Vacias))
            # Guardamos esas coordenadas
            pos = lista_Posiciones_Vacias[var]
            # Colocamos el objetivo en el mapa
            self.mapa.mapa[pos[0], pos[1]] = 1
            # Eliminamos de la lista esas coordenadas utilizadas
            lista_Posiciones_Vacias.pop(var)

            # Segun la lista de "lista_ContadorObjetivos",
            # Crearemos unos u otros objetivos en funcion de la iteracion del bucle
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
        """
        :param nivel: El nivel de la partida en el momento actual
        :param nxC: La cantidad de celdas en el eje X
        :param nyC: La cantidad de celdas en el eje Y
        :return: No devuelve nada de manera explicita pero si que modifica atributos de clase
        """

        # Obtenemos la cantidad de obstaculos segun diferentes factores
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
            ob1 = int(cantidadObstaculos - (cantidadObstaculos * 0.9))
            ob2 = int((cantidadObstaculos - ob1) * 0.7)
            ob3 = int(cantidadObstaculos - (ob1 + ob2))
        else:
            ob1 = 0
            ob2 = int((cantidadObstaculos - ob1) * 0.7)
            ob3 = int(cantidadObstaculos - (ob1 + ob2))

        # Creamos una lista de la cantidad de los diferntes obstaculos,
        # ob1-Obstaculos de nivel 1, ob2-Obstaculos de nivel 2 y ob3-Obstaculos de nivel 3
        lista_ContadorObstaculos = [ob1, ob2, ob3]

        # Esta lista se encarga de registrar que posiciones del mapa estan vacias
        lista_Posiciones_Vacias = []

        # Colocamos la snake en el mapa
        for i in self.snake.cuerpo:
            self.mapa.mapa[i[0], i[1]] = 2

        # Colocamos los obstaculos en el mapa
        for i in self.lista_Obstaculos:
            self.mapa.mapa[i[0], i[1]] = 3

        # Recorremos el mapa y todos aquellas posiciones que esten vacias las guardamos
        for i in range(nxC):
            for z in range(nyC):
                if self.mapa.mapa[i][z] == 0:
                    lista_Posiciones_Vacias.append([i, z])

        # Bucle que se va a encargar de crear tantos obstaculos como numero sea la variable
        for obj in range(cantidadObstaculos):
            # Generamos un numero aleatorio de la lista de posiciones vacias
            var = random.randrange(len(lista_Posiciones_Vacias))
            # Guardamos esas coordenadas
            pos = lista_Posiciones_Vacias[var]
            # Colocamos el obstaculo en el mapa
            self.mapa.mapa[pos[0], pos[1]] = 1
            # Eliminamos de la lista esas coordenadas utilizadas
            lista_Posiciones_Vacias.pop(var)

            # Segun la lista de "lista_ContadorObstaculos",
            # Crearemos unos u otros obstaculos en funcion de la iteracion del bucle
            if lista_ContadorObstaculos[0] != 0:
                self.lista_Obstaculos.append(ObstaculoSimple(pos[0], pos[1], nxC, nyC))
                lista_ContadorObstaculos[0] -= 1
            elif lista_ContadorObstaculos[1] != 0:
                self.lista_Obstaculos.append(ObstaculoMedio(pos[0], pos[1], nxC, nyC))
                lista_ContadorObstaculos[1] -= 1
            elif lista_ContadorObstaculos[2] != 0:
                self.lista_Obstaculos.append(ObstaculoDificil(pos[0], pos[1], nxC, nyC))
                lista_ContadorObstaculos[2] -= 1

    def autmoatizarMovimietno(self, newMapa):
        """
        :param newMapa: El mapa que se utilizara para albergar las modificaciones del mapa
        :return: El metodo devuelve el mapa con las modificaciones ya realizadas
        """

        # Cambiamos de posicion los objetivos
        # Modificamos el mapa segun las nuevas posiciones de los objetivos
        for i in self.lista_Objetivos:
            newMapa[i.posicion[0], i.posicion[1]] = 0
            i.cambiaDireccion()
            newMapa[i.posicion[0], i.posicion[1]] = 1

        # Cambiamos de posicion los obstaculos
        # Modificamos el mapa segun las nuevas posiciones de los obstaculos
        for i in self.lista_Obstaculos:
            newMapa[i.posicion[0], i.posicion[1]] = 0
            i.cambiaDireccion()
            newMapa[i.posicion[0], i.posicion[1]] = 3

        # Condicion que mantiene seguro a la snake hasta que se mueve por primera vez
        if self.snake.direccion != "Ninguna":
            # Metodo encargado de saber si ha habido algun impacto antes de que la cabeza se mueva
            self.verificadorPosicionElementos()
            # Cambiamos de posicion el cuerpo de la snake
            # Modificamos el mapa segun las nuevas posiciones del cuerpo de la snake
            for i in self.snake.cuerpo:
                newMapa[i[0], i[1]] = 0
            # Movemos la cabeza de la serpiente
            self.snake.cambiaDireccion()
            # Metodo encargado de saber si ha habido algun impacto despues de que la cabeza se mueva
            self.verificadorPosicionElementos()
            # Metodo encargado de saber si ha habido algun impacto de la cabeza contra su cuerpo
            self.verificadorPosicionCuerpo()
            # Metodo que se encarga de mover el cuerpo de la snake
            self.snake.moverCuerpo()
            # Modificamos el mapa en funcion de la posicion del cuerpo
            for i in self.snake.cuerpo:
                newMapa[i[0], i[1]] = 2

        return newMapa

    def verificadorPosicionElementos(self):
        """
        :return: El metodo no devuelve nada de manera explicita pero si que modifica ciertos atributos
        """

        # Variable encargada de contar numero de iteraciones del bucle en funcion de la longitud de "lista_Objetivos"
        contador = 0
        # Variable encargada de registrar en que iteracion la posicion de la cabeza es igual a la de algun objetivo
        impacto = None
        # Bucle en cargado de comparar cada posicion de cada elemento de "lista_Objetivos" con la cabeza de la snake
        for i in self.lista_Objetivos:
            # Condicion queverifica la posicion del objetivo con la de la cabeza de la snake
            if i.posicion == self.snake.cabeza:
                # Metodo encargaddo de añadir al cuerpo la posicion de la cola
                self.snake.cuerpo.insert(0, list(self.snake.cola))
                # Registrar el numero de iteracion
                impacto = contador
            contador += 1
        # Condicion encargada de verificar si ha habido algun impacto
        if impacto is not None:
            # Eliminamos el objetivos impactado de su lista
            self.lista_Objetivos.pop(impacto)

        # Bucle en cargado de comparar cada posicion de cada elemento de "lista_Obstaculos" con la cabeza de la snake
        for i in self.lista_Obstaculos:
            # Condicion queverifica la posicion del obstaculo con la de la cabeza de la snake
            if i.posicion == self.snake.cabeza:
                # Cambiamos el estado de la snake a muerta
                self.snake.estado = 0

    def verificadorPosicionCuerpo(self):
        """
        :return: El metodo no devuelve nada de manera explicita pero si que modifica ciertos atributos
        """

        # Condicion que determina que si la longitud del cuerpo no es superior a 1 no realiza comprobaciones,
        # con respecto a impactos entre cabeza y cuerpo ya que es lo mismo
        if len(self.snake.cuerpo) > 1:
            # Condicion que verifica la posicion de la cabeza con cada posicion del cuerpo
            if self.snake.cabeza in self.snake.cuerpo:
                # Cambiamos el estado de la snake a muerta
                self.snake.estado = 0
