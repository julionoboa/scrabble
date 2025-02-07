import random
class Fichas :
    #region FichasList
    Fichas = [
    {'letra': 'A', 'valor': 1, 'cantidad': 12},
    {'letra': 'B', 'valor': 3, 'cantidad': 2},
    {'letra': 'C', 'valor': 3, 'cantidad': 4},
    {'letra': 'D', 'valor': 2, 'cantidad': 5},
    {'letra': 'E', 'valor': 1, 'cantidad': 12},
    {'letra': 'F', 'valor': 4, 'cantidad': 1},
    {'letra': 'G', 'valor': 2, 'cantidad': 2},
    {'letra': 'H', 'valor': 4, 'cantidad': 2},
    {'letra': 'I', 'valor': 1, 'cantidad': 6},
    {'letra': 'J', 'valor': 8, 'cantidad': 1},
    {'letra': 'K', 'valor': 5, 'cantidad': 1},
    {'letra': 'L', 'valor': 1, 'cantidad': 4},
    {'letra': 'M', 'valor': 3, 'cantidad': 2},
    {'letra': 'N', 'valor': 1, 'cantidad': 5},
    {'letra': 'O', 'valor': 1, 'cantidad': 9},
    {'letra': 'P', 'valor': 3, 'cantidad': 2},
    {'letra': 'Q', 'valor': 10, 'cantidad': 1},
    {'letra': 'R', 'valor': 1, 'cantidad': 5},
    {'letra': 'S', 'valor': 1, 'cantidad': 6},
    {'letra': 'T', 'valor': 1, 'cantidad': 6},
    {'letra': 'U', 'valor': 1, 'cantidad': 6},
    {'letra': 'V', 'valor': 4, 'cantidad': 1},
    {'letra': 'W', 'valor': 4, 'cantidad': 1},
    {'letra': 'X', 'valor': 8, 'cantidad': 1},
    {'letra': 'Y', 'valor': 4, 'cantidad': 1},
    {'letra': 'Z', 'valor': 10, 'cantidad': 1},
    {'letra': '-', 'valor': 0, 'cantidad': 2}
    ]
    #endregion

    #Metodo para sacar fichas de la bolsa:
    def sacar(self,Cantidad_Fichas):
        ListaSacada = []
        if (Cantidad_Fichas > 0 and Cantidad_Fichas <= 7):
            for i in range(Cantidad_Fichas):
                while(True):
                    rando = random.randint(0,len(self.Fichas)-1)

                    if self.Fichas[rando]["cantidad"] > 0:
                        self.Fichas[rando]["cantidad"] -= 1
                        ListaSacada.append(self.Fichas[rando]["letra"])
                        break
        return ListaSacada

    #Metodo para recibir que el jugador quiere cambiar
    def retornar(self,ListaDevuelta):
        for letra in ListaDevuelta:
            for ficha in self.Fichas:
                if ficha["letra"] == letra:
                    ficha["cantidad"]+=1
                    break
