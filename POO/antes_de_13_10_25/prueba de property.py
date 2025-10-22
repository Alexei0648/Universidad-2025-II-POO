class rectangulo:
    def __init__ (self,_ancho, _alto):
        self._ancho=_ancho
        self._alto=_alto
    @property
    def area(self):
        return self._ancho*self._alto
    


recta1= rectangulo (3,4)
print(recta1.area)

rect2=rectangulo(5,4)
print(rect2.area)