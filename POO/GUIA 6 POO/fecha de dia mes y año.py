class Fecha:
    # Constructor
    
#-----------------------ATRIBUTOS---------------------------------
    def __init__(self, dia=1, mes=1, anio=2000):
        self.dia = dia
        self.mes = mes
        self.anio = anio
#-----------------------MÉTODOS-----------------------------------    
    def mostrar(self):
        print(f"{self.dia:02d}/{self.mes:02d}/{self.anio}")
        
    def es_bisiesto(self, anio):
        return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
    
    def dias_del_mes(self, mes, anio):
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif mes in [4, 6, 9, 11]:
            return 30
        elif mes == 2:
            if self.es_bisiesto(anio):
                return 29
            else:
                return 28

    def incrementar(self, numeroDias):
        for i in range(numeroDias):
            self.dia += 1
            if self.dia > self.dias_del_mes(self.mes, self.anio):
                self.dia = 1
                self.mes += 1
                if self.mes > 12:
                    self.mes = 1
                    self.anio += 1

    def convertir_a_dias(self, dia, mes, anio):
        total = 0
        for a in range(1, anio):
            if self.es_bisiesto(a):
                total += 366
            else:
                total += 365
        for m in range(1, mes):
            total += self.dias_del_mes(m, anio)
        total += dia
        return total
    
    def distancia(self, dia, mes, anio):
        dias1 = self.convertir_a_dias(self.dia, self.mes, self.anio)
        dias2 = self.convertir_a_dias(dia, mes, anio)
        return abs(dias1 - dias2)
#-----------------------INSTANCIA--------------------------------
fecha1 = Fecha()
print("Fecha inicial:")
fecha1.mostrar()  
fecha1.incrementar(40)
print("Después de incrementar 40 días:")
fecha1.mostrar()  
dist = fecha1.distancia(1, 1, 2000)
print("Distancia en días con 01/01/2000:", dist)
print("----------------------------------------------------------")
