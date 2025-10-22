#Clase: cuenta
class cuenta:
#------------------ATRIBUTO----------------------------
    def __init__(self, titular, saldo="Lo siento, estas sin plata"):
        self.titular = titular
        self.saldo = saldo

#-------------------MÉTODO-------------------------------
    def depositar(self, cantidad):
        self.saldo =self.saldo + cantidad
        print(f"Depósito de {cantidad}. Saldo actual: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad}. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes")

            
    def mostrar(self):
            print(f"Titular: {self.titular}, Su cuenta es de: {self.saldo} ")

#-----------------------INSTANCIA-----------------------------
# Crear una cuenta
cuenta1 = cuenta("Carlos",100)
cuenta1.mostrar()
cuenta1.depositar(230)
cuenta2= cuenta("mateo")
cuenta2.mostrar()

