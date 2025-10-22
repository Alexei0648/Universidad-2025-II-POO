def suma_num(n):
    if n == 0: 
        return 0
    else:
        return n + suma_num(n - 1)
       
# Ingreso del número límite

limite = int(input("Ingresa un número: "))# limite es la variable de ingreso de datos

resultado = suma_num(limite) # la funcion se guarda en la variable resultado

print("La suma de es:", resultado)# imprime texto y imprime la variable