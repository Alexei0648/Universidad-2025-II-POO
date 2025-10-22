def burbuja_nombres(lista): # función a llamar
    arr = lista[:] # lista que se va a ordenar
    n = len(arr) # aquí se ve la longitud de la lista
    
    for i in range(n): # iterador
        for j in range(0, n-i-1): # en cada pasada, comparamos pares vecinos
            # Usamos comparación alfabética  algo asi como a, b, c..., y asi con cada 1ra letra de los nombres
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j] # intercambiamos los dos
                print(f"Intercambio: {arr}") # esto imprime los intercambios
    
    return arr 


nombres = ["Carlos", "Ana", "Pedro", "Lucía", "Diego"] # esta es la lista con los nombres
print("Lista ordenada:", burbuja_nombres(nombres)) # hacemos la impresión del texto y luego de la función
