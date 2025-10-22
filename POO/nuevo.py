import random
# generar lista aleatoria
lista = [random.randint(1, 100) for iterador_de_lista in range(10)]
print("obj original:", lista)

# ---------------------------
# ORDENAMIENTO BURBUJA
# ---------------------------
def burbuja(lista):
    la_lista = lista.copy()
    cantidad_de_lista = len(la_lista)
    for primerbucle in range(cantidad_de_lista):
        swapped = False
        for segundobucle in range(0, cantidad_de_lista - primerbucle - 1):
            if la_lista[segundobucle] > la_lista[segundobucle + 1]:
                la_lista[segundobucle], la_lista[segundobucle + 1] = la_lista[segundobucle + 1], la_lista[segundobucle]
                swapped = True
        if not swapped:
            break
    return la_lista
print("burbuja  ->", burbuja(lista))