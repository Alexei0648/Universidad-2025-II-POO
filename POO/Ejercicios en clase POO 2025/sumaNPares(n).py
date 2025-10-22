import time

def sumaNPares(n): 
    suma = 0
    for i in range(2, 2*n+1, 2): 
        suma += i  
    return suma

def medir_tiempo_ejecucion(n): # funcion para medir el tiempo de ejecucion
    start_time = time.time() # tiempo de inicio
    resultado = sumaNPares(n) # llamada a la funcion
    end_time = time.time()  # tiempo de fin
    tiempo_transcurrido = end_time - start_time      
    print(f"Resultado sumaNPares({n}) = {resultado}")    
    print(f"Tiempo de ejecución: {tiempo_transcurrido:.6f} segundos")  
    return tiempo_transcurrido 

# ==========================
# PROBAR
# ==========================
n = 10
medir_tiempo_ejecucion(n)
