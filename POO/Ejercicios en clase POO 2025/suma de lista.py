#---------------------------------------------------------------------------------------------
def sumar_lista(lista): # funcion con la variable lista
    if not lista:                  # si no es la lista, entonces retorna 0
        return 0  # Caso base: lista vacía, da 0
#---------------------------------------------------------------------------------------------
    else: # sino
        return lista[0] + sumar_lista(lista[1:])  # Llamada recursiva, el lista[0], comprende que 
    #                                       empieza desde la posición 0, luego lo suma con la posicón 1 hasta la ultima posicón
    #   retorna la posicón cero más la función con la varible con [1:]
#---------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------
numeros = [10,9,8,7,6,5,4,3,2,1]# lista con los datos
# posición  0 1 2 3 4 5 6 7 8 9
resultado = sumar_lista(numeros)# a la funcón se el implanta la lista a recorrer

print("La suma de la lista es:", resultado) # imprime la variable que contiene a la funcion
#---------------------------------------------------------------------------------------------

#                                                             RESUMEN
#---------------------------------------------------------------------------------------------
# la funcion def, denominada sumar_lista(lista), tiene que si si no es la lista, entonces retorna 0, sino retornara la formula
# que es sumar la posicón 0, con la posicón 1, luego con la posición siguiente hasta terminar la lista completa