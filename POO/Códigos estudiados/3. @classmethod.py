class Persona:
    cantidad = 0  # atributo de clase

    def __init__(self, nombre):
        self.nombre = nombre
        Persona.cantidad += 1

    @classmethod
    def crear_anónimo(cls):
        return cls("Anónimo")

    @classmethod
    def total_personas(cls):
        return f"Se han creado {cls.cantidad} personas."

p1 = Persona("Pedrito")
p2 = Persona.crear_anónimo()

print(p1.nombre)              # Alexei
print(p2.nombre)              # Anónimo
print(Persona.total_personas())  # Se han creado 2 personas.
