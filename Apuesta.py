class Apuesta:

    def __init__(self, jugador, dineroAApostar):
        self.jugador = jugador
        self.dineroApostado = dineroAApostar
        self.jugador.restarSaldo(self.dineroApostado)
