def busqueda_binaria(lista, b):
    n=len(lista)
    i=0
    j=n-1
    while i<= j:
        m=(i+j)//2
        if (b > lista[m]):
            i = m+1
        elif(b< lista[m]):
            j=m+1
        else:
            return m
    return -1

lista=[1,2,3,4,5,6,60,70,80,100]
b= 80
print("",busqueda_binaria(lista,b))