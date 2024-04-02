from Jugador import Jugador
from ApuestaPorColor import ApuestaPorColor
from Partida import Partida
from Ronda import Ronda
from NumeroDeRuleta import NumeroDeRuleta
from Interfaz import Interfaz

partida = Partida()
jugador = Jugador()
interfaz = Interfaz(partida)



#for i in range(10000000):
    #ronda = partida.iniciarNuevaRonda()

    #ronda.agregarApuesta(ApuestaPorColor(jugador, 10, NumeroDeRuleta.COLOR_ROJO))
    #ronda.agregarApuesta(ApuestaPorColor(jugador, 10, NumeroDeRuleta.COLOR_NEGRO))
    #ronda.ejecutar()

#print(partida.obtenerEstadisticas())


#print("El saldo del jugador es: " + str(jugador.saldo))