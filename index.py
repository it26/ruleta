from Jugador import Jugador
from ApuestaPorColor import ApuestaPorColor
from Partida import Partida
from Ronda import Ronda
from NumeroDeRuleta import NumeroDeRuleta

partida = Partida()
jugador = Jugador()
ronda = Ronda()

ronda.agregarApuesta(ApuestaPorColor(jugador, 10, NumeroDeRuleta.COLOR_ROJO))
ronda.agregarApuesta(ApuestaPorColor(jugador, 10, NumeroDeRuleta.COLOR_NEGRO))
ronda.ejecutar()

#partida.obtenerDatosDeLaRonda(ronda)

print("El saldo del jugador es: " + str(jugador.saldo))