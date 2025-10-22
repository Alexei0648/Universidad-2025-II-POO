class semaforo:
    def __init__(self,_luz=0):
        self._luz=_luz

    @property
    def cambiar(self):
        if self._luz==1:
            return ("luz verde")
        elif self._luz ==2 :
            return ("luz amarilla")
        elif self._luz == 3 :
            return ("luz roja")
        else:
            return ("no valido")
    
se1=semaforo(1)
print(se1.cambiar)