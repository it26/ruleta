from Apuesta import Apuesta
from NumeroDeRuleta import NumeroDeRuleta

class ApuestaPorColor(Apuesta):

    def __init__(self, jugador, dineroAApostar, color):
        super().__init__(jugador, dineroAApostar)
        if (color not in NumeroDeRuleta.COLORES):
            raise Exception("Color de apuesta no válido")
        self.color = color

    def ejecutarResultado(self, numeroDeLaRonda):
        if (numeroDeLaRonda.color == self.color):
            self.jugador.sumarSaldo(self.dineroApostado*2)
