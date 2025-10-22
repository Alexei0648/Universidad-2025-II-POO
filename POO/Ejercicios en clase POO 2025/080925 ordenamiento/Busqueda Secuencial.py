print("\n---------------------------------------------------")

def seleccion(lista,b): # función con 2 variables
    n = len(lista) #n toma el valor de la longitud
    for i in range(0, n): #rango denominado i, su rango es de la posición 0 hasta el tamaño de la longitud
        if lista[i] ==b: # si en caso la posicion i cumple con la condición que sea igual a b entonces se retornara en la posición encontrada
            return i # torna el numero de la posicón
    return -1 # caso contrario a no encontrarar el valor, votara un -1


lista=[5,9,4,1,8,3,2,0,11,20]
b=11 # el valor a encontrar
print("El número: ",b,"esta en la posición: ",seleccion(lista,b))
print("\n---------------------------------------------------")

#busqueda binaria'?\\
