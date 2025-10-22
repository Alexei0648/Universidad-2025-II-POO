class rectangulo:

    def __init__(self,_altura,_base,_color="sin color"):
        self._altura=_altura
        self._color=_color
        self._base=_base

    def calcular_area(self):
        if self._altura>0:
            if self._base>0:
                return (self._base) *(self._altura)
        else:
            return ("No se puede calcular el area con numero negativos")

    def calcular_perimetro(self):
        if self._altura>0:
            if self._base>0:
                return (2*(self._base + self._altura))
        else:
            return("No se puede calcular el perimetro con numeros negativos")

    def __str__(self):
        return (f"""el area del rectangulo es de : {self.calcular_area()} Metros, 
                su perimetro es de: {self.calcular_perimetro()} Metros y su color es: {self._color}""")

rect1=rectangulo(200,400,"verde")
rect1.calcular_area()
rect1.calcular_perimetro()
print(rect1)

