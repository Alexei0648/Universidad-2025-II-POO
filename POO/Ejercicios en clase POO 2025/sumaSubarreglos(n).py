import time

def sumaSubarreglos(n):
    arr = list(range(1, n+1))
    total = 0
    for i in range(n):
        for j in range(i, n): # i a j 
            total += sum(arr[i:j+1])  
    return total # suma de todos los subarreglos

def medir_tiempo_ejecucion(n): # funcion para medir el tiempo de ejecucion
    start_time = time.time()
    resultado = sumaSubarreglos(n) # llamada a la funcion
    end_time = time.time()
    tiempo_transcurrido = end_time - start_time
    print(f"Resultado sumaSubarreglos({n}) = {resultado}")
    print(f"Tiempo de ejecución: {tiempo_transcurrido:.6f} segundos")
    return tiempo_transcurrido

# ==========================
# PROBAR
# ==========================
n = 5
medir_tiempo_ejecucion(n)
