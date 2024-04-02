import tkinter as tk

class Interfaz:

    def __init__(self, partida):
        self.partida = partida
        self.ventana = tk.Tk()
        self.textoPorcentajeCero = tk.Label(self.ventana, text="Cero: ")
        self.textoPorcentajeCero.place(x=10, y=50)
        self.textoApuestasColor = tk.Label(self.ventana, text="Color: ")
        self.textoApuestasColor.place(x=10, y=70)
        self.textoApuestasDocenas = tk.Label(self.ventana, text="Docenas: ")
        self.textoApuestasDocenas.place(x=10, y=90)
        self.botonEjecutarCienRondas = tk.Button(self.ventana, text="Ejecutar 100 rondas", command=lambda: self.ejecutarRondas(100))
        self.botonEjecutarCienRondas.place(x=10, y=10)
        self.botonEjecutarCienRondas = tk.Button(self.ventana, text="Ejecutar 1.000.000 rondas", command=lambda: self.ejecutarRondas(1000000))
        self.botonEjecutarCienRondas.place(x=200, y=10)
        self.ventana.geometry("400x300+400+200")
        self.ventana.mainloop()

    def ejecutarRondas(self, numeroDeRondasAEjecutar):
        for i in range(numeroDeRondasAEjecutar):
            ronda = self.partida.iniciarNuevaRonda()
            ronda.ejecutar()

        self.actualizarEstadisticas()

    def actualizarEstadisticas(self):
        estadisticas = self.partida.obtenerEstadisticas()
        self.textoPorcentajeCero.config(text="Cero: " + str(round(estadisticas["porcentajeDeRondasPorNumero"][0], 2)) + "%")
        self.textoApuestasColor.config(text="Color: Rojo " + str(round(estadisticas["porcentajeDeRondasConColorRojo"], 2)) + "%, Negro " + str(round(estadisticas["porcentajeDeRondasConColorNegro"], 2)) + "%")
        self.textoApuestasDocenas.config(text="Docenas: Primera " + str(round(estadisticas["porcentajeDeRondasConPrimeraDocena"], 2)) + "%, Segunda " + str(round(estadisticas["porcentajeDeRondasConSegundaDocena"], 2)) + "%, Tercera " + str(round(estadisticas["porcentajeDeRondasConTerceraDocena"], 2)) + "%")
