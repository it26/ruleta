from NumeroDeRuleta import NumeroDeRuleta

class GeneradorDeEstadisticas:

    def __init__(self, rondas):
        self.rondas = rondas

    def generarEstadisticas(self, ultimasRondasAAnalizar = False):
        rondasQueSalioElColorRojo = 0
        rondasQueSalioElColorNegro = 0
        rondasQueSalioPar = 0
        rondasQueSalioImpar = 0
        rondasQueSalioMayor = 0
        rondasQueSalioMenor = 0
        rondasQueSalioPrimeraColumna = 0
        rondasQueSalioSegundaColumna = 0
        rondasQueSalioTerceraColumna = 0
        rondasQueSalioPrimeraDocena = 0
        rondasQueSalioSegundaDocena = 0
        rondasQueSalioTerceraDocena = 0
        rondasPorNumero = self.generarArrayDeNumeros()
        rondasSinSalirElColorRojo = 0
        rondasSinSalirElColorNegro = 0
        rondasSinSalirPar = 0
        rondasSinSalirImpar = 0
        rondasSinSalirMayor = 0
        rondasSinSalirMenor = 0
        rondasSinSalirPrimeraColumna = 0
        rondasSinSalirSegundaColumna = 0
        rondasSinSalirTerceraColumna = 0
        rondasSinSalirPrimeraDocena = 0
        rondasSinSalirSegundaDocena = 0
        rondasSinSalirTerceraDocena = 0
        rondasSinSalirPorNumero = self.generarArrayDeNumeros()
        porcentajeDeRondasConColorRojo = 0
        porcentajeDeRondasConColorNegro = 0
        porcentajeDeRondasConPar = 0
        porcentajeDeRondasConImpar = 0
        porcentajeDeRondasConMayor = 0
        porcentajeDeRondasConMenor = 0
        porcentajeDeRondasConPrimeraColumna = 0
        porcentajeDeRondasConSegundaColumna = 0
        porcentajeDeRondasConTerceraColumna = 0
        porcentajeDeRondasConPrimeraDocena = 0
        porcentajeDeRondasConSegundaDocena = 0
        porcentajeDeRondasConTerceraDocena = 0
        porcentajeDeRondasPorNumero = self.generarArrayDeNumeros()
        maximoDeRondasSinSalirElColorRojo = 0
        maximoDeRondasSinSalirElColorNegro = 0
        maximoDeRondasSinSalirPar = 0
        maximoDeRondasSinSalirImpar = 0
        maximoDeRondasSinSalirMayor = 0
        maximoDeRondasSinSalirMenor = 0
        maximoDeRondasSinSalirPrimeraColumna = 0
        maximoDeRondasSinSalirSegundaColumna = 0
        maximoDeRondasSinSalirTerceraColumna = 0
        maximoDeRondasSinSalirPrimeraDocena = 0
        maximoDeRondasSinSalirSegundaDocena = 0
        maximoDeRondasSinSalirTerceraDocena = 0
        maximoDeRondasSinSalirPorNumero = self.generarArrayDeNumeros()

        if ultimasRondasAAnalizar == False:
            ultimasRondasAAnalizar = len(self.rondas)

        for ronda in self.rondas[-ultimasRondasAAnalizar:]:
            numero = ronda.numero

            for numeroRuleta in range(0, 37):
                if numeroRuleta == numero.valor:
                    rondasPorNumero[numeroRuleta] += 1
                    rondasSinSalirPorNumero[numeroRuleta] = 0
                else:
                    rondasSinSalirPorNumero[numeroRuleta] += 1

                if maximoDeRondasSinSalirPorNumero[numeroRuleta] < rondasSinSalirPorNumero[numeroRuleta]:
                    maximoDeRondasSinSalirPorNumero[numeroRuleta] = rondasSinSalirPorNumero[numeroRuleta]

            if (numero.salioCero() == False):
                if numero.color == NumeroDeRuleta.COLOR_ROJO:
                    rondasSinSalirElColorRojo = 0
                    rondasSinSalirElColorNegro += 1
                    rondasQueSalioElColorRojo += 1

                if numero.color == NumeroDeRuleta.COLOR_NEGRO:
                    rondasSinSalirElColorNegro = 0
                    rondasSinSalirElColorRojo += 1
                    rondasQueSalioElColorNegro += 1

                if numero.esPar:
                    rondasSinSalirPar = 0
                    rondasSinSalirImpar += 1
                    rondasQueSalioPar += 1

                if numero.esImpar:
                    rondasSinSalirImpar = 0
                    rondasSinSalirPar += 1
                    rondasQueSalioImpar += 1

                if numero.esMayor:
                    rondasSinSalirMayor = 0
                    rondasSinSalirMenor += 1
                    rondasQueSalioMayor += 1
                
                if numero.esMenor:
                    rondasSinSalirMenor = 0
                    rondasSinSalirMayor += 1
                    rondasQueSalioMenor += 1

                if numero.columna == NumeroDeRuleta.PRIMERA_COLUMNA:
                    rondasSinSalirPrimeraColumna = 0
                    rondasSinSalirSegundaColumna += 1
                    rondasSinSalirTerceraColumna += 1
                    rondasQueSalioPrimeraColumna += 1

                if numero.columna == NumeroDeRuleta.SEGUNDA_COLUMNA:
                    rondasSinSalirSegundaColumna = 0
                    rondasSinSalirPrimeraColumna += 1
                    rondasSinSalirTerceraColumna += 1
                    rondasQueSalioSegundaColumna += 1

                if numero.columna == NumeroDeRuleta.TERCERA_COLUMNA:
                    rondasSinSalirTerceraColumna = 0
                    rondasSinSalirPrimeraColumna += 1
                    rondasSinSalirSegundaColumna += 1
                    rondasQueSalioTerceraColumna += 1
                
                if numero.docena == NumeroDeRuleta.PRIMER_DOCENA:
                    rondasSinSalirPrimeraDocena = 0
                    rondasSinSalirSegundaDocena += 1
                    rondasSinSalirTerceraDocena += 1
                    rondasQueSalioPrimeraDocena += 1
                
                if numero.docena == NumeroDeRuleta.SEGUNDA_DOCENA:
                    rondasSinSalirSegundaDocena = 0
                    rondasSinSalirPrimeraDocena += 1
                    rondasSinSalirTerceraDocena += 1
                    rondasQueSalioSegundaDocena += 1
                
                if numero.docena == NumeroDeRuleta.TERCERA_DOCENA:
                    rondasSinSalirTerceraDocena = 0
                    rondasSinSalirPrimeraDocena += 1
                    rondasSinSalirSegundaDocena += 1
                    rondasQueSalioTerceraDocena += 1
            else:
                rondasSinSalirElColorRojo += 1
                rondasSinSalirElColorNegro += 1
                rondasSinSalirImpar += 1
                rondasSinSalirPar += 1
                rondasSinSalirMenor += 1
                rondasSinSalirMayor += 1
                rondasSinSalirPrimeraColumna += 1
                rondasSinSalirSegundaColumna += 1
                rondasSinSalirTerceraColumna += 1
                rondasSinSalirPrimeraDocena += 1
                rondasSinSalirSegundaDocena += 1
                rondasSinSalirTerceraDocena += 1

            if (maximoDeRondasSinSalirElColorRojo < rondasSinSalirElColorRojo):
                maximoDeRondasSinSalirElColorRojo = rondasSinSalirElColorRojo

            if (maximoDeRondasSinSalirElColorNegro < rondasSinSalirElColorNegro):
                maximoDeRondasSinSalirElColorNegro = rondasSinSalirElColorNegro

            if (maximoDeRondasSinSalirPar < rondasSinSalirPar):
                maximoDeRondasSinSalirPar = rondasSinSalirPar

            if (maximoDeRondasSinSalirImpar < rondasSinSalirImpar):
                maximoDeRondasSinSalirImpar = rondasSinSalirImpar

            if (maximoDeRondasSinSalirMenor < rondasSinSalirMenor):
                maximoDeRondasSinSalirMenor = rondasSinSalirMenor

            if (maximoDeRondasSinSalirMayor < rondasSinSalirMayor):
                maximoDeRondasSinSalirMayor = rondasSinSalirMayor

            if (maximoDeRondasSinSalirPrimeraColumna < rondasSinSalirPrimeraColumna):
                maximoDeRondasSinSalirPrimeraColumna = rondasSinSalirPrimeraColumna

            if (maximoDeRondasSinSalirSegundaColumna < rondasSinSalirSegundaColumna):
                maximoDeRondasSinSalirSegundaColumna = rondasSinSalirSegundaColumna

            if (maximoDeRondasSinSalirTerceraColumna < rondasSinSalirTerceraColumna):
                maximoDeRondasSinSalirTerceraColumna = rondasSinSalirTerceraColumna

            if (maximoDeRondasSinSalirPrimeraDocena < rondasSinSalirPrimeraDocena):
                maximoDeRondasSinSalirPrimeraDocena = rondasSinSalirPrimeraDocena

            if (maximoDeRondasSinSalirSegundaDocena < rondasSinSalirSegundaDocena):
                maximoDeRondasSinSalirSegundaDocena = rondasSinSalirSegundaDocena

            if (maximoDeRondasSinSalirTerceraDocena < rondasSinSalirTerceraDocena):
                maximoDeRondasSinSalirTerceraDocena = rondasSinSalirTerceraDocena


        porcentajeDeRondasConColorNegro = (rondasQueSalioElColorNegro * 100) / len(self.rondas)
        porcentajeDeRondasConColorRojo = (rondasQueSalioElColorRojo * 100) / len(self.rondas)
        porcentajeDeRondasConPar = (rondasQueSalioPar * 100) / len(self.rondas)
        porcentajeDeRondasConImpar = (rondasQueSalioImpar * 100) / len(self.rondas)
        porcentajeDeRondasConMenor = (rondasQueSalioMenor * 100) / len(self.rondas)
        porcentajeDeRondasConMayor = (rondasQueSalioMayor * 100) / len(self.rondas)
        porcentajeDeRondasConPrimeraColumna = (rondasQueSalioPrimeraColumna * 100) / len(self.rondas)
        porcentajeDeRondasConSegundaColumna = (rondasQueSalioSegundaColumna * 100) / len(self.rondas)
        porcentajeDeRondasConTerceraColumna = (rondasQueSalioTerceraColumna * 100) / len(self.rondas)
        porcentajeDeRondasConPrimeraDocena = (rondasQueSalioPrimeraDocena * 100) / len(self.rondas)
        porcentajeDeRondasConSegundaDocena = (rondasQueSalioSegundaDocena * 100) / len(self.rondas)
        porcentajeDeRondasConTerceraDocena = (rondasQueSalioTerceraDocena * 100) / len(self.rondas)

        for numeroRuleta in range(0,37):
            porcentajeDeRondasPorNumero[numeroRuleta] = (rondasPorNumero[numeroRuleta] * 100) / len(self.rondas)


        return {
                'maximoDeRondasSinSalirElColorNegro': maximoDeRondasSinSalirElColorNegro, 
                'porcentajeDeRondasConColorNegro': porcentajeDeRondasConColorNegro,
                'maximoDeRondasSinSalirElColorRojo': maximoDeRondasSinSalirElColorRojo,
                'porcentajeDeRondasConColorRojo': porcentajeDeRondasConColorRojo,
                'maximoDeRondasSinSalirPar': maximoDeRondasSinSalirPar,
                'porcentajeDeRondasConPar': porcentajeDeRondasConPar,
                'maximoDeRondasSinSalirImpar': maximoDeRondasSinSalirImpar,
                'porcentajeDeRondasConImpar': porcentajeDeRondasConImpar,
                'maximoDeRondasSinSalirMenor': maximoDeRondasSinSalirMenor,
                'porcentajeDeRondasConMenor': porcentajeDeRondasConMenor,
                'maximoDeRondasSinSalirMayor': maximoDeRondasSinSalirMayor,
                'porcentajeDeRondasConMayor': porcentajeDeRondasConMayor,
                'maximoDeRondasSinSalirPrimeraColumna': maximoDeRondasSinSalirPrimeraColumna,
                'porcentajeDeRondasConPrimeraColumna': porcentajeDeRondasConPrimeraColumna,
                'maximoDeRondasSinSalirSegundaColumna': maximoDeRondasSinSalirSegundaColumna,
                'porcentajeDeRondasConSegundaColumna': porcentajeDeRondasConSegundaColumna,
                'maximoDeRondasSinSalirTerceraColumna': maximoDeRondasSinSalirTerceraColumna,
                'porcentajeDeRondasConTerceraColumna': porcentajeDeRondasConTerceraColumna,
                'maximoDeRondasSinSalirPrimeraDocena': maximoDeRondasSinSalirPrimeraDocena,
                'porcentajeDeRondasConPrimeraDocena': porcentajeDeRondasConPrimeraDocena,
                'maximoDeRondasSinSalirSegundaDocena': maximoDeRondasSinSalirSegundaDocena,
                'porcentajeDeRondasConSegundaDocena': porcentajeDeRondasConSegundaDocena,
                'maximoDeRondasSinSalirTerceraDocena': maximoDeRondasSinSalirTerceraDocena,
                'porcentajeDeRondasConTerceraDocena': porcentajeDeRondasConTerceraDocena,
                'maximoDeRondasSinSalirPorNumero': maximoDeRondasSinSalirPorNumero,
                'porcentajeDeRondasPorNumero': porcentajeDeRondasPorNumero
                }

    def generarArrayDeNumeros(self):
        arrayNumeros = {}
        
        for numero in NumeroDeRuleta.NUMEROS:
            arrayNumeros[numero] = 0
        
        return arrayNumeros