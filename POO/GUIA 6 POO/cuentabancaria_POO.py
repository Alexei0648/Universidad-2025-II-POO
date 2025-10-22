#Clase: cuenta
class cuenta:
#------------------ATRIBUTO----------------------------
    def __init__(self, titular,saldo=0):
        self.titular = titular
        self.saldo = saldo
#-------------------MÉTODO-------------------------------
    def depositar(self, cantidad):
        if cantidad>0 :
            if cantidad <=10000:
                self.saldo =self.saldo + cantidad
            else:
                print("No puede depositar mas de 10,000 Intis")
        else:
             print("Monto minimo es de Un inti")
    def retirar(self, cantidad):
        if cantidad <self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad}. Saldo actual: {self.saldo}")
        else:
             print("Su Saldo es insuficiente, solo tiene",(self.saldo),"Intis")

    def mostrar(self):
        print(f"Titular: {self.titular}, Su cuenta es de: {self.saldo} INTIS")
        print("----------------------------------------------------------")
    
#-----------------------INSTANCIA-----------------------------
# Crear una cuenta
print("----------------------CUENTAS BANCARIAS-------------------")
cuenta1 = cuenta("Pablo Emilio")
cuenta1.depositar(10000)
cuenta1.retirar(233000)
cuenta1.mostrar()

