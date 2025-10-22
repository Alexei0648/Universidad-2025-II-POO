class Temperatura:
    def __init__(self,grados_c):
        self._grados_c=grados_c
    @property
    def grados_c (self):
        return self._grados_c
    
    @grados_c.setter  # el setter sirve para actualizar
    def grados_c(self, valor):
        if valor >= -273.15:
            self._grados_c=valor
        else:
            raise ValueError ("por debajo del cero absoluto")
    
   
temp1=Temperatura(0)
#temp1.grados_c = -273.14
print(temp1.grados_c)