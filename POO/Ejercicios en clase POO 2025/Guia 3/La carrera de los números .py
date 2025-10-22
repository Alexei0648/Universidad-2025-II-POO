def burbuja_numeros(lista): #funcion a llmar
    arr = lista[:] # lista que se va a ordenar
    n = len(arr) # aqui se ve la longitud de la lista
    
    # Vamos a recorrer varias veces la lista
    for i in range(n): # interador 
        # En cada pasada, comparamos pares vecinos
        for j in range(0, n-i-1):
            # Si el de la izquierda es más grande que el de la derecha hay que moverlos
            if arr[j] > arr[j+1]:
                # Intercambiamos los dos
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # Mostramos el cambio como si fueran corredores cambiando de puesto 
                print(f"Intercambio: {arr}")# esto imprime los intercambios
    
    return arr # retorna la variable arr


# solamente imprimimos el resultado
print("Lista ordenada:", burbuja_numeros([5, 3, 8, 4, 2]))# hacemos la impresion del texto y luego de la funcion
