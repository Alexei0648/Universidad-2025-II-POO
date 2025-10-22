import random
class persona:
    def __init__(self,_nombre="",_edad=0,_sexo="H",_peso=0,_altura=0,_dni=0):
        self._Dni=_dni
        self._nombre=_nombre
        self._edad=_edad
        self._sexo=_sexo
        self._peso=_peso
        self._altura=_altura
    def calcular_IMC(self):
            return (self._peso//(self._altura*self._altura))
    def calcular_IMCB(self):
        if self.calcular_IMC() < 20:
            return("-1 bajo peso")        
        elif 20 < self.calcular_IMC() < 25:
            return("0, peso ideal")       
        elif self.calcular_IMC() > 25:
            return("1, obesidad")    
    def es_mayor_de_edad(self):
        if self._edad > 18:
            return True
        else:
            return False
    def generar_DNI(self,_dni=0):
            _dni = random.randint(10000000, 99999999)
            return _dni    
    def __str__(self):
        return (f"""Buen dia Señor: {self._nombre}, su edad es de: {self._edad} Años, su DNI es el: {self.generar_DNI()}, 
                su sexo es: {self._sexo}, su peso es: {self._peso} kg, su altura es: {self._altura} mts y su Indice de Masa Corporal es de: {self.calcular_IMC()} 
                que significa: {self.calcular_IMCB()} y es mayor de edad: {self.es_mayor_de_edad()}""")
        
per1=persona("Juan carlos segundo maximiliano escobar delgado mamani",400,"Prefiereo no decirlo",80,1.80,0)
print(per1)
