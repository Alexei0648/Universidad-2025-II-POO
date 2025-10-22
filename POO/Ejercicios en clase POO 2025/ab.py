def suma_linea(a, b):
    pasos = 0 
    while b > 0: 
        a= a +1
        b= b-1 
        pasos += 1 
    print(f"total de pasos ejecutado: {pasos}")
    return a

a1=int(input("ingrese el dato 1: "))
b1=int(input("ingrese el dato 2: "))
resultados = suma_linea(a1, b1)
print("resultado 🍓", resultados)
