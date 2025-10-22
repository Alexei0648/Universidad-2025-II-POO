def fibonacci(n): # funcion def fibonacci
    
    
    if n == 0:         # si n es igula a 0, entonces se ejecuta retornar 0
        return 0       # se retorna 0, como dato, solo regresa 0
    
    elif n == 1:       # sino, n debe ser igual a 1
        return 1       # retornar 1, 
    
    else:              # caso contrario
        return fibonacci(n - 1) + fibonacci(n - 2) # retorna fibonacci(n - 1) + fibonacci(n - 2)
    
#-------------------------------------------------------------
a=int(input("ingrese el el número: "))  # ingreso del dato o numero
print(f" el número es", fibonacci(a))  # se ejecuta toda la función