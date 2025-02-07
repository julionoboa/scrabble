from Fichas2 import Fichas

class Jugador:
    ficha = Fichas()

    def __init__(self):
        self.ListFichaJ = self.ficha.sacar(7)
        self.ListFichaJ_temp =[]

    def CambiarListFichaJ(self):
        cantidad = len(self.ListFichaJ)
        self.ficha.retornar(self.ListFichaJ)
        self.ListFichaJ = self.ficha.sacar(cantidad)

    # def PasarTurno(self):
    #     #Limpiar la lista temporal
    #     pass

    def ColocarFicha(self, fichaParametro):
        for ficha in self.ListFichaJ:
            if ficha == fichaParametro:
                self.ListFichaJ_temp.append(ficha)
                self.ListFichaJ.remove(ficha)

    def DeshacerJugada(self):
        self.ListFichaJ += (self.ListFichaJ_temp)
        self.ListFichaJ_temp = []

    def MostrarListFichaJ(self):
        return(self.ListFichaJ)







