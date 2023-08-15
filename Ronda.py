import random
from Numero import Numero

class Ronda:

    def __init__(self):
        self.apuestas = []
        self.numero = None

    def agregarApuesta(self, apuesta):
        self.apuestas.append(apuesta)

    def ejecutar(self):
        self.numero = Numero(random.randint(0, 36))
        print("El numero que salio es:" + str(self.numero.valor))
        for apuesta in self.apuestas:
            apuesta.ejecutarResultado(self.numero)
