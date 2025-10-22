def ordenaniento_seleccion(lista):
    n=len(lista)
    for i in range (n-1):
        min=i
        for j in range(i+1, n):
            if lista[j] < lista[min]:
                min=j
        lista[j], lista[min] = lista[min], lista[i]
        print(f"la iteración es: {i+1} -- {lista}")
    return lista

lista=[4,5,6,7]
print("La lista ordenada es: ",ordenaniento_seleccion(lista))