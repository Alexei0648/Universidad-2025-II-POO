class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre     # atributo "protegido"
        self._edad = edad

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor < 0:
            raise ValueError("La edad no puede ser negativa.")
        self._edad = valor

    @edad.deleter
    def edad(self):
        print("Edad eliminada")
        del self._edad
p = Persona("Alexei", 20)

print(p.edad)       # ✅ llama automáticamente a def edad(self)
p.edad = 25         # ✅ llama al setter
del p.edad          # ✅ llama al deleter
