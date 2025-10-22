#INICIO
def factorial(n):
    if n==0:
        return 1
    else:
        return (n*factorial(n-1))

#Fin
    
nro=int(input("ingrese su número entero positivo: " ))

fact= factorial(nro)
print("El factorial es" , fact)

