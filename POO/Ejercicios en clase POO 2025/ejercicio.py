import time

def contar_hasta_n(n):
    count = 0
    for i in range (n):
        count =+1
    return count

def medir_tiempo_ejecución(n):
    star_time = time.time()
    resultado = contar_hasta_n(n)
    end_time = time.time()
    tiempo_transcurrido = end_time - star_time
    return tiempo_transcurrido
n= 1000

tiempo= medir_tiempo_ejecución(n)
print(f"tiempo de ejecución: {tiempo:.6f} segundos")