import random
def esta_ordenada(lista):
    return all(lista[i] <= lista[i+1] for i in range(len(lista)-1))
def busqueda_binaria(lista, numero):
    if not esta_ordenada(lista):
        lista.sort()
        print("⚠️ Lista no estaba ordenada. Se ordenó automáticamente.")
    izquierda, derecha = 0, len(lista) - 1
    iteraciones = 0
    while izquierda <= derecha:
        iteraciones += 1
        medio = (izquierda + derecha) // 2
        if lista[medio] == numero:
            return medio, iteraciones
        elif lista[medio] < numero:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1, iteraciones
def busqueda_secuencial(lista, numero):
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones += 1
        if lista[i] == numero:
            return i, comparaciones
    return -1, comparaciones
lista = [random.randint(1, 1000) for _ in range(100)]
print("Lista generada (puede no estar ordenada):", lista)
print("\n--- Resultados Búsqueda Binaria ---")
for i in range(5):
    numero = random.choice(lista)
    pos_bin, it = busqueda_binaria(lista, numero)
    pos_sec, comp_sec = busqueda_secuencial(lista, numero)
    print(f"Buscando {numero}:")
    print(f"   Binaria → Posición: {pos_bin}, Iteraciones: {it}")
    print(f"   Secuencial (estimado) → Comparaciones: {comp_sec}")
print("\n📌 Conclusión:")
print("La búsqueda binaria reduce las comparaciones porque divide la lista a la mitad en cada paso.")
print("Esto refleja su complejidad O(log n), frente a la O(n) de la búsqueda secuencial.")