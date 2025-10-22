def ordenar_monedas(monedas):
    numerodelementos = len(monedas) # toma el valor de la longitud de la lista
    # Recorrer la lista desde el segundo elemento hasta el final
    for Nombre_del_primer_iterador in range(1, numerodelementos): 
        
        key = monedas[Nombre_del_primer_iterador] # elemento actual a insertar
        
        Nombre_del_segundo_iterador = Nombre_del_primer_iterador - 1 # índice del elemento anterior
        # Mover los elementos mayores que la key una posición a la derecha 
        
        while Nombre_del_segundo_iterador >= 0 and monedas[Nombre_del_segundo_iterador] > key: # mientras Ndsi >=0  y tambien  debe cumplir la condifción de que 
            monedas[Nombre_del_segundo_iterador + 1] = monedas[Nombre_del_segundo_iterador]
            
            Nombre_del_segundo_iterador -= 1 
            
        # Insertar la key en la posición correcta
        
        monedas[Nombre_del_segundo_iterador + 1] = key 
        
    return monedas # retornar la lista ordenada


# Ejemplo de uso
monedas = [10,5,25,1,8] # es la lista a ordenar
print("Lista ordenada:", ordenar_monedas(monedas)) # se imprime un texto y imprime la lista ordenada
