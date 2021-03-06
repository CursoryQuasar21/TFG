import tkinter as tk
import pickle
from tkinter import Canvas, ttk
from partida import Partida
from jugador import Jugador
from ia import partida
class SnakeGUI:
    """
    Esta clase gestiona la interfaz de usuario del juego
    """

    def __init__(self):

        ventana = tk.Tk()
        ventana.title("Snake GUI")

        # Dimensiones de la Ventana
        ventana.geometry('700x400')

        # Establecemos el fondo en negro
        ventana.configure(background='black')

        # Recuperamos los nombres y las puntuaciones de las partidas en esta variable.
        self.lista_partidas = self.recuperar_puntuacion("puntuaciones")

        # Etiquetas de la ventana
        self.highscore_label = tk.Label(ventana, text='[HIGHSCORE]:', fg='green', bg='black')
        self.highscore_label.config(font=("Arial", 15))
        self.highscore_label.place(x=450, y=20)

        ranking_label = tk.Label(ventana, text='RANKING HISTÓRICO', bg='black', fg='orange red')
        ranking_label.config(font=("Arial", 12))
        ranking_label.place(x=450, y=75)

        self.firstP_label = tk.Label(ventana, text='1 -->', bg='black', fg='green')
        self.firstP_label.config(font=("Arial", 12))
        self.firstP_label.place(x=450, y=115)

        self.secondP_label = tk.Label(ventana, text='2 -->', bg='black', fg='green')
        self.secondP_label.config(font=("Arial", 12))
        self.secondP_label.place(x=450, y=165)

        self.thirdP_label = tk.Label(ventana, text='3 -->', bg='black', fg='green')
        self.thirdP_label.config(font=("Arial", 12))
        self.thirdP_label.place(x=450, y=215)

        self.forthP_label = tk.Label(ventana, text='4 -->', bg='black', fg='green')
        self.forthP_label.config(font=("Arial", 12))
        self.forthP_label.place(x=450, y=265)

        self.fithP_label = tk.Label(ventana, text='5 -->', bg='black', fg='green')
        self.fithP_label.config(font=("Arial", 12))
        self.fithP_label.place(x=450, y=315)

        name_label = tk.Label(ventana, text='Introduce tu nombre por favor:', bg='black', fg='green')
        name_label.config(font=("Arial", 12))
        name_label.place(x=20, y=22)

        difficulty_level = tk.Label(ventana, text='Elige dificultad para jugar:', bg='black', fg='green')
        difficulty_level.config(font=("Arial", 12))
        difficulty_level.place(x=20, y=85)

        game_mode = tk.Label(ventana, text='[MODO DE JUEGO]', bg='black', fg='green')
        game_mode.config(font=("Arial", 12))
        game_mode.place(x=20, y=210)

        # Cuadro de texto para el nombre
        self.name_txtbox = ttk.Entry(ventana)
        self.name_txtbox.place(x=245, y=24)

        # Botones de radio para gestionar la dificultad
        self.radio_value = tk.IntVar()

        # Definimos los botones
        easy = tk.Radiobutton(ventana, text='Fácil', variable=self.radio_value, value=1, bg='black', fg='green')
        medium = tk.Radiobutton(ventana, text='Medio', variable=self.radio_value, value=2, bg='black', fg='green')
        hard = tk.Radiobutton(ventana, text='Difícil', variable=self.radio_value, value=3, bg='black', fg='green')
        impossible = tk.Radiobutton(ventana, text='Nivel Dios', variable=self.radio_value, value=4, bg='black', fg='orange red')

        # Definimos los botones en la pantalla
        easy.place(x=20, y=130)
        medium.place(x=80, y=130)
        hard.place(x=140, y=130)
        impossible.place(x=200, y=130)

        # Botones encargados de gestionar la eleccion del tipo de juego
        basic_snake = tk.Button(ventana, text="Basic Snake", bg='black', fg='green', command=self.basicSnake)
        basic_snake.config(font=("Arial", 12))
        basic_snake.place(x=20, y=250)

        basic_snake = tk.Button(ventana, text="Snake vs IA ", bg='black', fg='orange red', command=self.snakeVsIA)
        basic_snake.config(font=("Arial", 12))
        basic_snake.place(x=20, y=310)

        separator = Canvas(width=15, height=400, bg="green")
        separator.create_line(0, 200, 200, 0, fill="green")

        # Asignamos las puntuaciones a su sitio correspondiente del ranking
        if len(self.lista_partidas) >= 1:
            self.highscore_label.config(text='HIGHSCORE:'+str(self.lista_partidas[0].score))
            self.firstP_label.config(text=self.lista_partidas[0].nombreJugador+' -> ' + str(self.lista_partidas[0].score))
        if len(self.lista_partidas) >= 2:
            self.secondP_label.config(text=self.lista_partidas[1].nombreJugador+' -> ' + str(self.lista_partidas[1].score))
        if len(self.lista_partidas) >= 3:
            self.thirdP_label.config(text=self.lista_partidas[2].nombreJugador+' -> ' + str(self.lista_partidas[2].score))
        if len(self.lista_partidas) >= 4:
            self.forthP_label.config(text=self.lista_partidas[3].nombreJugador+' -> ' + str(self.lista_partidas[3].score))
        if len(self.lista_partidas) >= 5:
            self.fithP_label.config(text=self.lista_partidas[4].nombreJugador+' -> ' + str(self.lista_partidas[4].score))

        ventana.mainloop()

    #
    # Metodos que gestionan la funcionalidadd de la interfaz
    #
    def basicSnake(self):
        """
        :return: Este método una vez que es llamado inicia la partida del basic snake
        """
        # Evaluamos el valor de el radiobutton para establecer el nivel
        if self.radio_value.get() == 1:
            nivel = 1
        elif self.radio_value.get() == 2:
            nivel = 2
        elif self.radio_value.get() == 3:
            nivel = 3
        else:
            nivel = 4

        # Iniciamos la partida con los parámetros establecidos.
        game = Partida(600, 600, 50, 50, self.name_txtbox.get(), nivel)
        self.puntuacion(game)
        self.highscore_label.config(text='HIGHSCORE:'+str(self.lista_partidas[0].score))
        if len(self.lista_partidas) >= 1:
            self.firstP_label.config(text=self.lista_partidas[0].nombreJugador+' -> ' + str(self.lista_partidas[0].score))
        if len(self.lista_partidas) >= 2:
            self.secondP_label.config(text=self.lista_partidas[1].nombreJugador+' -> ' + str(self.lista_partidas[1].score))
        if len(self.lista_partidas) >= 3:
            self.thirdP_label.config(text=self.lista_partidas[2].nombreJugador+' -> ' + str(self.lista_partidas[2].score))
        if len(self.lista_partidas) >= 4:
            self.forthP_label.config(text=self.lista_partidas[3].nombreJugador+' -> ' + str(self.lista_partidas[3].score))
        if len(self.lista_partidas) >= 5:
            self.fithP_label.config(text=self.lista_partidas[4].nombreJugador+' -> ' + str(self.lista_partidas[4].score))

    @staticmethod
    def snakeVsIA():
        """
        :return: Este método una vez que es llamado inicia la partida de Snake VS IA
        """
        partida()

    def puntuacion(self, game):
        """
        :param game: El parametro partida contiene la puntuacion de la partida y el nivel al que ha llegado
        :return: El metodo no devuelve nada de manera explicita pero si que modifica las variables de clase "lista_Puntuaciones" y "highscore"
        """
        contador = len(self.lista_partidas)
        # En funcion del nivel se le aplicara un bonus de pntuacion en base al nivel
        if game.nivel == "facil":
            game.score = game.score*1.25
        if game.nivel == "Medio":
            game.score = game.score*1.5
        if game.nivel == "Dificil":
            game.score = game.score*3
        else:
            game.score = game.score*5

        if len(self.lista_partidas) == 0:
            self.lista_partidas.append(game)
        else:
            for i in self.lista_partidas:
                if i.score < game.score:
                    contador -= 1
            if contador < 5:
                self.lista_partidas.insert(contador, game)
                if len(self.lista_partidas) > 5:
                    self.lista_partidas.pop()

        # Guardamos la tupla en el archivo de puntuaciones
        self.guardar_puntuacion("puntuaciones")

    def guardar_puntuacion(self, nombre_archivo):
        """ Guarda la lista de puntajes en el archivo.
        Pre: nombre_archivo corresponde a un archivo válido, puntajes corresponde a los valores a guardar
        Post: se guardaron los valores en el archivo en formato pickle.
        """

        archivo = open(nombre_archivo, "wb")
        lista_Jugadores = []
        for i in range(len(self.lista_partidas)):
            # Añadimos objetos de jugador a la lista según la info de la lista de partidas
            lista_Jugadores.append(Jugador(self.lista_partidas[i].nombreJugador, self.lista_partidas[i].score))

        # Serializamos
        pickle.dump(lista_Jugadores, archivo)
        archivo.close()

    @staticmethod
    def recuperar_puntuacion(nombre_archivo):
        """
        :param nombre_archivo:
        :return:
        """
        """ 
        Recupera los puntajes a partir del archivo provisto.
            Devuelve una lista con los valores de los puntajes.
        Pre: el archivo contiene los puntajes en formato pickle
        Post: la lista devuelta contiene los puntajes en el
            mismo formato que se los almacenó.
        """

        archivo = open(nombre_archivo, "rb")
        lista_jugadores = pickle.load(archivo)
        archivo.close()
        return lista_jugadores
