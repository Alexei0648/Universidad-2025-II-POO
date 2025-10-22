def lista_de_compracion(lista):
    mayor =lista[0]
    for num in (lista):
        if num>mayor:
            mayor= num
    return mayor
lista=[5,8,3,12,7]
#      0 1 2 3  4
print("El de mayor valor es", lista_de_compracion(lista))

