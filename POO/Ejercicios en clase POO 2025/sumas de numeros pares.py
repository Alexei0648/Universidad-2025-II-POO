def suma_pares(n):
    if n == 0: 
        return 0
    else:
        if n % 2 == 0:  # si  n debe ser  divisible entre 2, asi mismo ese resultado es es igual a cero , entonces retorna  lo identado
            return n + suma_pares(n - 1) # el numero ingresa + el numero -1 
        else:
            return suma_pares(n - 1) # caso contrario 

# Ingreso del número límite

limite = int(input("Ingresa un número: "))# limite es la variable de ingreso de datos

resultado = suma_pares(limite) # la funcion se guarda en la variable resultado

print("La suma de pares es:", resultado)# imprime texto y imprime la variable