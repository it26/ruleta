class Jugador:

    def __init__(self):
        self.saldoInicial = 100
        self.saldo = self.saldoInicial

    def restarSaldo(self, dineroARestar):
        self.saldo -= dineroARestar 

    def sumarSaldo(self, dineroASumar):
        self.saldo += dineroASumar 