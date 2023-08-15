from Apuesta import Apuesta


class ApuestaPorColor(Apuesta):

    def __init__(self, jugador, dineroAApostar, color):
        super().__init__(jugador, dineroAApostar)
        self.color = color

    def ejecutarResultado(self, numeroDeLaRonda):
        if (numeroDeLaRonda.color == self.color):
            self.jugador.sumarSaldo(self.dineroApostado*2)
