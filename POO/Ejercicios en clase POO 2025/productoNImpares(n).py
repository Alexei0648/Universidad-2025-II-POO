import time

def productoNImpares(n): # funcion de la ecución para calcular el producto de los n primeros numeros impares 
    producto = 1
    for i in range(1, 2*n, 2):  # 1,3,5,...,(2n-1)
        producto *= i
    return producto

def medir_tiempo_ejecucion(n):# funcion para medir el tiempo de ejecucion
    start_time = time.time()# tiempo de inicio
    resultado = productoNImpares(n) # llamada a la funcion
    end_time = time.time() # tiempo de fin
    tiempo_transcurrido = end_time - start_time
    print(f"Resultado productoNImpares({n}) = {resultado}")
    print(f"Tiempo de ejecución: {tiempo_transcurrido:.6f} segundos") 
    return tiempo_transcurrido 

# ==========================
# PROBAR
# ==========================
n = 10
medir_tiempo_ejecucion(n)
