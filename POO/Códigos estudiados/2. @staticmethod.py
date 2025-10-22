class Matematica:
    @staticmethod
    def sumar(a, b):
        return a + b
    @staticmethod
    def restar(a, b):
        return a - b
    @staticmethod
    def multiplicar(a, b):
        return a * b
print(Matematica.sumar(10,4))   # ✅ se llama directamente
print(Matematica.restar(10,4))   # ❌ Error: restar() missing 1 required positional argument: 'b'
print(Matematica.multiplicar(10,4))   # ❌ Error: multiplicar() missing 1 required positional argument: 'b'