def burbuja_contador(lista):   # función a llamar   
    arr = lista[:] # lista que se va a ordenar
    n = len(arr) # aquí se ve la longitud de la lista
    
    comparaciones = 0  # cuántas veces miramos un par
    intercambios = 0   # cuántas veces realmente movimos algo
    
    for i in range(n):
        for j in range(0, n-i-1):
            comparaciones += 1  # cada vez que comparo, sumo
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                intercambios += 1
                print(f"Intercambio: {arr}")  # para ver cómo avanza
    
    # Mostramos los datos finales de conteo, easi se imprime cada iteración
    print(f"Total comparaciones: {comparaciones}") # se imprime texto y la variable
    print(f"Total intercambios: {intercambios}") # se imprime texto y la variable
    return arr


# Probamos
print("Lista ordenada:", burbuja_contador([5, 3, 8, 4, 2]))
