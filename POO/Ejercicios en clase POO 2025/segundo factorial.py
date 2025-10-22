#inicio
def fact(n):
    resultado=1
    for i in range (1,n+1): # es un bucle que establece un rango, de tal hasta tal cifra o dato
        resultado=resultado*i
    else:
        return resultado 

#fin funcion
red=int(input("ingrese el numero entero positivo: "))# ingreso de datos
factorial=(fact(red))
print("El factorial es:" ,factorial)
#de 5 es 120 < n*(n-1) >