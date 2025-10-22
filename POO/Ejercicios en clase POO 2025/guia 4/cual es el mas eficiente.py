import random
import time

# ---------- Algoritmo de Inserción ----------
def ordenar_monedas(lista):
    numerodelementos = len(lista) # toma el valor de la longitud de la lista
    # Recorrer la lista desde el segundo elemento hasta el final
    for Nombre_del_primer_iterador in range(1, numerodelementos): 
        
        key = lista[Nombre_del_primer_iterador] # elemento actual a insertar
        
        Nombre_del_segundo_iterador = Nombre_del_primer_iterador - 1 # índice del elemento anterior
        # Mover los elementos mayores que la key una posición a la derecha 
        
        while Nombre_del_segundo_iterador >= 0 and lista[Nombre_del_segundo_iterador] > key: # mientras Ndsi >=0  y tambien  debe cumplir la condifción de que 
            lista[Nombre_del_segundo_iterador + 1] = lista[Nombre_del_segundo_iterador]
            
            Nombre_del_segundo_iterador -= 1 
            
        # Insertar la key en la posición correcta
        
        lista[Nombre_del_segundo_iterador + 1] = key 
        
    return lista # retornar la lista ordenada
#-------------------------------------------------------------------------------------------------------

# ---------- Algoritmo de Selección ----------
def ordenar_equipo(lista):
    n = len(lista) # toma el valor de la longitud de la lista
    # Recorrer la lista
    for caballero in range(n): 
        # Encontrar el índice del valor mínimo en la parte no ordenada
        min_index = caballero 
        for arquero in range(caballero+1, n):    
            if lista[arquero] < lista[min_index]: 
                min_index = arquero 

        # Intercambiar el valor mínimo con el primer valor no ordenado
        lista[caballero], lista[min_index] = lista[min_index], lista[caballero]

    return lista 


# ---------- Menú ----------
def menu():
    lista = []
    while True:
        print("\n====== MENÚ  ======") # Título del menú usa el \n para hacer un salto de línea
        print("\nNúmero 1 para Generar lista aleatoria de 100 números") 
        print("\nNúmero 2 para Ordenar con Inserción")
        print("\nNúmero 3 para Ordenar con Selección")
        print("\nNúmero 4 para Comparar ambos métodos")
        print("\nNúmero 5 para Salir")
        
        opcion = input("Seleccione una opción: ") # se ingresa una de las opciones del menú
        if opcion == "1":
            lista = [random.randint(1, 1000) for _ in range(100)] # Genera una lista aleatoria de 100 números entre 1 y 1000
            print("Lista generada (100 elementos):")
            print(lista)
        elif opcion == "2":
            if not lista:
                print("Primero genere la lista (opción 1).")
            else:
                copia = lista[:]  # trabajar con una copia
                inicio = time.time()
                ordenada, comps = ordenar_monedas(copia)
                fin = time.time()
                print("\n Ordenamiento por Inserción completado.")
                print("Comparaciones realizadas:", comps)
                print("Tiempo de ejecución:", round(fin - inicio, 6), "segundos")
                print("Lista ordenada (primeros 20 elementos):", ordenada[:20])

        elif opcion == "3":
            if not lista:
                print("Primero genere la lista (opción 1).") 
            else:
                copia = lista[:]
                inicio = time.time() 
                ordenada, comps = ordenar_equipo(copia)
                fin = time.time()
                print("\nOrdenamiento por Selección completado.")
                print("Comparaciones realizadas:", comps)
                print("Tiempo de ejecución:", round(fin - inicio, 6), "segundos")
                print("Lista ordenada (primeros 20 elementos):", ordenada[:20])

        elif opcion == "4":
            if not lista:
                print("Primero genere la lista (opción 1).")
            else:
                # Inserción
                copia1 = lista[:]
                inicio1 = time.time()
                _, comps1 = ordenar_monedas(copia1)
                fin1 = time.time()
                tiempo1 = fin1 - inicio1

                # Selección
                copia2 = lista[:]
                inicio2 = time.time()
                _, comps2 = ordenar_equipo(copia2)
                fin2 = time.time()
                tiempo2 = fin2 - inicio2

                print("\n===== COMPARACIÓN =====")
                print("Inserción -> Comparaciones:", comps1, ", Tiempo:", round(tiempo1, 6), "s")
                print("Selección -> Comparaciones:", comps2, ", Tiempo:", round(tiempo2, 6), "s")

                if tiempo1 < tiempo2:
                    print("\n El método más eficiente fue: Inserción (menor tiempo).")
                elif tiempo2 < tiempo1:
                    print("\n El método más eficiente fue: Selección (menor tiempo).")
                else:
                    print("\n Ambos métodos tuvieron tiempos similares.")

        elif opcion == "5":
            print("Saliendo del programa... 👋")   
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# ---------- Ejecutar programa ----------
if __name__ == "__main__":
    menu()
