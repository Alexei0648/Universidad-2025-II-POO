def imprimir_descendente(n): #---------------------------------definición
    if n == 0: # if es  sí, además que n tiene el valor de 0                                       #caso base
        return # retorna el dato de n igual a 0                                                    #caso base
    print("el número ganador es",n) #imprime cada cifra                                            #caso recursivo
    imprimir_descendente(n - 1) # comprende el quitarle menos uno al valor de la definición        #caso recursivo

# Llamamos a la función con 100
imprimir_descendente(10)#--------------- los parentesis, le da el valor a la definición, cada vez que lo lea, será de menor valor
