class NumeroDeRuleta:

    COLOR_ROJO = 'rojo'
    COLOR_NEGRO = 'negro'
    COLORES = [COLOR_ROJO, COLOR_NEGRO]
    PRIMER_DECENA = 'primera'
    SEGUNDA_DECENA = 'segunda'
    TERCERA_DECENA = 'tercera'
    DECENAS = [PRIMER_DECENA, SEGUNDA_DECENA, TERCERA_DECENA]
    PRIMERA_COLUMNA = 'primera'
    SEGUNDA_COLUMNA = 'segunda'
    TERCERA_COLUMNA = 'tercera'
    COLUMNAS = [PRIMERA_COLUMNA, SEGUNDA_COLUMNA, TERCERA_COLUMNA]
    MAYOR = 'mayor'
    MENOR = 'menor'
    PAR = 'par'
    IMPAR = 'impar'

    def __init__(self, valor):
        self.valor = valor
        self.color = self.obtenerColor()
        self.decena = self.obtenerDecena()
        self.columna = self.obtenerColumna()
        self.esMayor = True if self.obtenerMayorMenor() == self.MAYOR else False
        self.esMenor = True if self.obtenerMayorMenor() == self.MENOR else False
        self.esPar= True if self.obtenerParImpar() == self.PAR else False
        self.esImpar = True if self.obtenerParImpar() == self.IMPAR else False

    def salioCero(self):
        if(self.valor == 0):
            return True
        return False

    def obtenerColor(self):
        if(self.salioCero()):
            return None
        valoresRojos = [1, 3, 5, 7, 9, 12, 14, 16,
                        18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        if self.valor in valoresRojos:
            return self.COLOR_ROJO
        return self.COLOR_NEGRO

    def obtenerDecena(self):
        if(self.salioCero()):
            return None
        primeraDecena = range(1, 13)
        segundaDecena = range(13, 25)
        if self.valor in primeraDecena:
            return self.PRIMER_DECENA
        if self.valor in segundaDecena:
            return self.SEGUNDA_DECENA
        return self.TERCERA_DECENA

    def obtenerColumna(self):
        if(self.salioCero()):
            return None
        primerColumna = range(1, 37, 3)
        segundaColumma = range(2, 37, 3)
        if self.valor in primerColumna:
            return self.PRIMERA_COLUMNA
        if self.valor in segundaColumma:
            return self.SEGUNDA_COLUMNA
        return self.TERCERA_COLUMNA

    def obtenerMayorMenor(self):
        if(self.salioCero()):
            return None
        if (self.valor <= 18):
            return self.MENOR
        return self.MAYOR

    def obtenerParImpar(self):
        if(self.salioCero()):
            return None
        if self.valor % 2 == 0:
            return self.PAR
        return self.IMPAR
