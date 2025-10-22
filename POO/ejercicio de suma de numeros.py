def suma_numeros(n):
    if n ==1:
        return 1
    else:
        return suma_numeros(n-1)+n

print(suma_numeros(7))