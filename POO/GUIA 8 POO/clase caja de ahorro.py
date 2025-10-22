class Cuenta:
    def __init__(self, saldo_inicial=0):
        self._saldo = saldo_inicial  
    @property
    def saldo(self):
        return self._saldo
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
        else:
            print("La cantidad debe ser positiva.")
    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
        else:
            print("Fondos insuficientes")
cu1 = Cuenta(100)
cu1.depositar(50)
cu1.retirar(30)
print("Saldo actual:", cu1.saldo)