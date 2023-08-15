class Numero:

    def __init__(self, valor):
        self.valor = valor
        self.color = self.obtenerColor()
        self.decena = self.obtenerDecena()
        self.columna = self.obtenerColumna()
        self.esMayorOMenor = self.obtenerMayorMenor()
        self.esParOImpar = self.obtenerParImpar()

    def obtenerColor(self):
        valoresRojos = [1, 3, 5, 7, 9, 12, 14, 16,
                        18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        if self.valor in valoresRojos:
            return 'rojo'
        return 'negro'

    def obtenerDecena(self):
        primeraDecena = range(1, 13)
        segundaDecena = range(13, 25)
        if self.valor in primeraDecena:
            return 'primera'
        if self.valor in segundaDecena:
            return 'segunda'
        return 'tercera'

    def obtenerColumna(self):
        primerColumna = range(1, 37, 3)
        segundaColumma = range(2, 37, 3)
        if self.valor in primerColumna:
            return 'primera'
        if self.valor in segundaColumma:
            return 'segunda'
        return 'tercera'

    def obtenerMayorMenor(self):
        if (self.valor <= 18):
            return 'menor'
        return 'mayor'

    def obtenerParImpar(self):
        if self.valor % 2 == 0:
            return 'par'
        return 'impar'
