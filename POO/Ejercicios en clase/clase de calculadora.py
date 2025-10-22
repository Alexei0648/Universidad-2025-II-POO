class Calculadora:
    
    @staticmethod
    def sumar(a, b):
        return a + b
    @staticmethod
    def restar(a, b):
        return a - b
    @staticmethod
    def multiplicar(a, b):
        return a * b
    @staticmethod
    def dividir(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: división entre cero."
        
print("Suma:", Calculadora.sumar(5, 3))
print("Resta:", Calculadora.restar(10, 4))
print("Multiplicación:", Calculadora.multiplicar(6, 7))
print("División:", Calculadora.dividir(8, 2))
