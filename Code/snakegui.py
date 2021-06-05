import tkinter as tk

from tkinter import ttk
from partida import Partida

class SnakeGUI:
    '''Esta clase gestiona la interfaz de usuario del juego'''

    def __init__(self):
        
        ventana = tk.Tk()
        ventana.title("Snake GUI")

        #DIMENSIONES DE LA VENTANA
        ventana.geometry('800x400')

        #ESTABLECEMOS EL FONDO NEGRO
        ventana.configure(background= 'black')

        #ETIQUETAS DE LA VENTANA
        highscore_label = tk.Label(ventana, text='HIGHSCORE:', fg= 'green', bg = 'black')
        highscore_label.config(font= ("Arial", 20))
        highscore_label.place(x=500, y=20)

        ranking_label = tk.Label(ventana, text='RANKING HISTÓRICO', bg= 'black', fg= 'orange red')
        ranking_label.config(font= ("Arial", 12))
        ranking_label.place(x=500, y=75)

        firstP_label = tk.Label(ventana, text='1 -->', bg= 'black', fg= 'green')
        firstP_label.config(font= ("Arial", 12))
        firstP_label.place(x=500, y=115)

        secondP_label = tk.Label(ventana, text='2 -->', bg= 'black', fg= 'green')
        secondP_label.config(font= ("Arial", 12))
        secondP_label.place(x=500, y=165)

        thirdP_label = tk.Label(ventana, text='3 -->', bg= 'black', fg= 'green')
        thirdP_label.config(font= ("Arial", 12))
        thirdP_label.place(x=500, y=215)

        forthP_label = tk.Label(ventana, text='4 -->', bg= 'black', fg= 'green')
        forthP_label.config(font= ("Arial", 12))
        forthP_label.place(x=500, y=265)

        forthP_label = tk.Label(ventana, text='5 -->', bg= 'black', fg= 'green')
        forthP_label.config(font= ("Arial", 12))
        forthP_label.place(x=500, y=315)

        name_label = tk.Label(ventana, text= 'Introduce tu nombre por favor:', bg= 'black', fg= 'green')
        name_label.config(font= ("Arial", 12))
        name_label.place(x=20, y=22)

        difficulty_level = tk.Label(ventana, text= 'Elige dificultad para jugar:', bg= 'black', fg= 'green')
        difficulty_level.config(font= ("Arial", 12))
        difficulty_level.place(x=20, y=85)

        game_mode = tk.Label(ventana, text= '[MODO DE JUEGO]', bg= 'black', fg= 'green')
        game_mode.config(font= ("Arial", 12))
        game_mode.place(x=20, y=210)

        #CUADRO DE TEXTO PARA EL NOMBRE
        name_txtbox = ttk.Entry(ventana)
        name_txtbox.place(x=245, y=24)

        #BOTONES DE RADIO PARA DESIGNAR LA DIFICULTAD
        radio_value = tk.IntVar()

        #DEFINIMOS LOS BOTONES
        easy = tk.Radiobutton(ventana, text='Fácil',
                             variable=radio_value, value=1, bg= 'black', fg= 'green') 
        medium = tk.Radiobutton(ventana, text='Medio',
                                    variable=radio_value, value=2, bg= 'black', fg= 'green') 
        hard = tk.Radiobutton(ventana, text='Difícil',
                                    variable=radio_value, value=3, bg= 'black', fg= 'green')
        impossible = tk.Radiobutton(ventana, text='Nivel Dios',
                                    variable=radio_value, value=4, bg= 'black', fg= 'orange red')

        #LOS COLOCAMOS
        easy.place(x=20,y=130)
        medium.place(x=80,y=130)
        hard.place(x=140,y=130)
        impossible.place(x=200,y=130)

        #
        #MÉTODOS QUE GESTIONAN LA FUNCIONALIDAD DE LA INTERFAZ
        #
        def basicSnake():
            '''Este método una vez que es llamado inicia 
            la partida del basic snake'''

            partida = Partida(600,600,50,50)

            
        #BOTONES PARA DESIGNAR MODO DE JUEGO
        basic_snake = tk.Button(ventana, text="Basic Snake", bg= 'black', fg= 'green', command=basicSnake)
        basic_snake.config(font= ("Arial", 12))
        basic_snake.place(x=20, y=250)

        basic_snake = tk.Button(ventana, text="Snake vs IA ", bg= 'black', fg= 'orange red')
        basic_snake.config(font= ("Arial", 12))
        basic_snake.place(x=20, y=310)

        ventana.mainloop()




