class persona:
    def __init__(self, _nombre,_ciudad, _ocupacion):
        self.nombre= _nombre
        self.ciudad= _ciudad
        self.ocupacion= _ocupacion

    def mostrar (self,_nombre,_ciudad, _ocupacion):
        print(_nombre,_ciudad, _ocupacion,)
        
persona1 = persona("Carlos","a","a")
persona1.mostrar