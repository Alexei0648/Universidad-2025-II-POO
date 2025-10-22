import random

# generar lista aleatoria simple
obj = [random.randint(1, 50) for _ in range(10)]
print("obj original:", obj)

# --------- ordenamiento por selección (in-place) ----------
def seleccion(obj):
    n = len(obj)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if obj[j] < obj[min_idx]:
                min_idx = j
        # intercambio
        obj[i], obj[min_idx] = obj[min_idx], obj[i]
    return obj

# --------- búsqueda binaria (iterativa) ----------
def busqueda_binaria(obj, val):
    ini = 0
    fin = len(obj) - 1
    while ini <= fin:
        mid = (ini + fin) // 2
        if obj[mid] == val:
            return mid     # posición donde se encontró
        elif obj[mid] < val:
            ini = mid + 1
        else:
            fin = mid - 1
    return -1  # no encontrado

# --------- ejecutar y mostrar resultados ----------
seleccion(obj)  # ordena obj in-place
print("obj ordenado:", obj)

# buscar un valor que sí está
val = random.choice(obj)
pos = busqueda_binaria(obj, val)
print("Buscando", val, "-> posición:", pos)

# buscar un valor que probablemente no está (ejemplo)
val2 = 999
pos2 = busqueda_binaria(obj, val2)
print("Buscando", val2, "-> posición:", pos2)  # -1 indica no encontrado
