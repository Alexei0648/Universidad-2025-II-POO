class circulo:
    pi=3.14159
    def __init__(self, radio):
        self.radio=radio
#-------------------------------------------------------
    @classmethod  # MÉTODO DE CLASE
    def unitario(cls):
        return cls(1)
#-------------------------------------------------------    
    @staticmethod #MÉTODO ESTÁTICO
    def area(r):
        return circulo.pi * r * r # se llama a la clase, junto a su atributo  de clase para multiplicar con r al cuadrado
#-------------------------------------------------------


c1=circulo.unitario()
print(c1.radio)
print(circulo.area(2))