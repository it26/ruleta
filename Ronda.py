import random
from NumeroDeRuleta import NumeroDeRuleta

class Ronda:

    def __init__(self):
        self.apuestas = []
        self.numero = None

    def agregarApuesta(self, apuesta):
        self.apuestas.append(apuesta)

    def ejecutar(self):
        self.numero = NumeroDeRuleta(random.randint(0, 36))
        #print("El numero que salio es:" + str(self.numero.valor))
        for apuesta in self.apuestas:
            apuesta.ejecutarResultado(self.numero)
