def burbuja(lista):
    n = len(lista)  # obtenemos el tamaño de la lista
    for i in range(n):  # bucle externo: controla cuántas pasadas damos
        # en cada pasada, el número más grande va "flotando" al final
        for j in range(0, n - i - 1):  
            # comparamos elementos adyacentes
            if lista[j] > lista[j + 1]:
                # si están en orden incorrecto, los intercambiamos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ejemplo de uso
print(burbuja([5, 3, 8, 4, 2]))
