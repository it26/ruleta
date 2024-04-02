from Ronda import Ronda
from GeneradorDeEstadisticas import GeneradorDeEstadisticas

class Partida:

    def __init__(self):
        self.rondas = []

    def iniciarNuevaRonda(self):
        ronda = Ronda()
        self.rondas.append(ronda)
        return ronda

    def obtenerEstadisticas(self, ultimasRondasAAnalizar = False):
        generadorDeEstadisticas = GeneradorDeEstadisticas(self.rondas)
        return generadorDeEstadisticas.generarEstadisticas(ultimasRondasAAnalizar)
            
            