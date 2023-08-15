class Apuesta:

    def __init__(self, jugador, dineroAApostar):
        self.jugador = jugador
        self.dineroApostado = dineroAApostar
        self.jugador.restarSaldo(self.dineroApostado)


    def salioCero(self, numeroDeLaRonda):
        if (numeroDeLaRonda.valor == 0):
            return True
        
        return False
