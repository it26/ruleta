class NumeroDeRuleta:

    def __init__(self, valor):
        self.valor = valor
        self.color = self.obtenerColor()
        self.decena = self.obtenerDecena()
        self.columna = self.obtenerColumna()
        self.esMayor = True if self.obtenerMayorMenor() == 'mayor' else False
        self.esMenor = True if self.obtenerMayorMenor() == 'menor' else False
        self.esPar= True if self.obtenerParImpar() == 'par' else False
        self.esImpar = True if self.obtenerParImpar() == 'impar' else False

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
            return 'rojo'
        return 'negro'

    def obtenerDecena(self):
        if(self.salioCero()):
            return None
        primeraDecena = range(1, 13)
        segundaDecena = range(13, 25)
        if self.valor in primeraDecena:
            return 'primera'
        if self.valor in segundaDecena:
            return 'segunda'
        return 'tercera'

    def obtenerColumna(self):
        if(self.salioCero()):
            return None
        primerColumna = range(1, 37, 3)
        segundaColumma = range(2, 37, 3)
        if self.valor in primerColumna:
            return 'primera'
        if self.valor in segundaColumma:
            return 'segunda'
        return 'tercera'

    def obtenerMayorMenor(self):
        if(self.salioCero()):
            return None
        if (self.valor <= 18):
            return 'menor'
        return 'mayor'

    def obtenerParImpar(self):
        if(self.salioCero()):
            return None
        if self.valor % 2 == 0:
            return 'par'
        return 'impar'
