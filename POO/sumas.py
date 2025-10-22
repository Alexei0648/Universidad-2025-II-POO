def sumar_n(n):
    # Caso base
    if n == 1:
        return 1
    # Caso recursivo
    else:
        return n + sumar_n(n - 1)

# Solicitar número al usuario
numero = int(input("Ingrese un número: "))

# Llamada a la función
resultado = sumar_n(numero)
print(f"La suma del 1 al {numero} es: {resultado}")
