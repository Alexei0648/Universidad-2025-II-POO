class estudiante:
    def __init__(self,_nombre,_matricula,_nota1=0,_nota2=0,_nota3=0):
        self._nombre=_nombre
        self._matricula=_matricula
        self._nota1, self._nota2, self.nota3 =_nota1,_nota2,_nota3


    
    def agregar(self,_nota1,_nota2,_nota3):
        
        prom=_nota1,_nota2,_nota3

  
    
    def promedio(self,prom):

        return (prom)/3

    
    def __str__(self):
        return f"Nombre: {self._nombre}, {self._matricula}"



alumno1=estudiante("Lucas", "M023",20,20,20)

print(alumno1.agregar(20,20,20))
print(alumno1)