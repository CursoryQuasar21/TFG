
class Jugador:
    """
    Esta clase se encarga de guardar tanto el nombre como la puntuación de los jugadores del snake
    """

    def __init__(self, nombre, puntuacion):
        """
        :param nombre: Nombre del jugador
        :param puntuacion: Puntuacion de la partida
        """

        self.nombreJugador = nombre
        self.score = puntuacion
