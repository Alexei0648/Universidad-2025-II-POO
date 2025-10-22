def ordenar_equipo(fuerzas):
    n = len(fuerzas) # toma el valor de la longitud de la lista
    # Recorrer la lista
    for caballero in range(n): 
        # Encontrar el índice del valor mínimo en la parte no ordenada
        min_index = caballero 
        for arquero in range(caballero+1, n):    
            if fuerzas[arquero] < fuerzas[min_index]: 
                min_index = arquero 

        # Intercambiar el valor mínimo con el primer valor no ordenado
        fuerzas[caballero], fuerzas[min_index] = fuerzas[min_index], fuerzas[caballero]

    return fuerzas 

# Ejemplo de uso
fuerzas= [40,30,90,20,10] # es la lista a ordenar
print("Lista ordenada:", ordenar_equipo(fuerzas)) # se imprime un texto y imprime la lista ordenada