class persona:
    def __init__(self, _nombre="Juanito",_edad=0):
        self._nombre =_nombre
        self._edad= _edad

    def __str__(self):
        return f"Nonbre: [{self._nombre}] y Edad: ({self._edad})"
    
person1=persona()
person2=persona("Ana",25)
print(person1)
print(person2)