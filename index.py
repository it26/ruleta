from Jugador import Jugador
from ApuestaPorColor import ApuestaPorColor
from Partida import Partida
from Ronda import Ronda

partida = Partida()
jugador = Jugador()
ronda = Ronda()

ronda.agregarApuesta(ApuestaPorColor(jugador, 10, 'rojo'))
ronda.agregarApuesta(ApuestaPorColor(jugador, 10, 'negro'))
ronda.ejecutar()

#partida.obtenerDatosDeLaRonda(ronda)

print("El saldo del jugador es: " + str(jugador.saldo))