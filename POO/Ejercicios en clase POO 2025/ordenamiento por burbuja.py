# Métodos de ordenamiento
# método de ordenamiento de la burbuja, sencillo pero no eficiente.
# Nota: existe un auxiliar, además que se debe comparar cada elemento con mayor y/o menor que

def metodo_de_burbuja(lista):
    n=len(lista)
    movimiento=0
    for i in range(n-1):
        for j in range(n-1-i):
            if lista[j]>lista[j+1]:
                lista[j] , lista[j+1]= lista[j+1] , lista[j]
                movimiento+=1
    return lista

lista=[123,65,3,5,7,9,765,3,46,98,34,6,98,]
print(metodo_de_burbuja(lista))


# crear panel de opcions para ingreso de lista y de ordenar

lista=[]
abierto=False
while abierto== False:
    print("Seleccion una opcion")
    print("opcion 1, ingreso de números: ")
    print("Opción 2, ordenar los números ingresados")
    print("Opción 0, salir del programa")
    opcion= int(input("Escriba el número de opción: "))
    if(opcion==1):
        elementos=int(input("Ingrese número: "))
        lista.append(elementos)
        print(lista)
    elif(opcion==2):
        if(len(lista)>0):
            print("La lista desordenada es: ", lista )
            print("L lista ordenada es:",metodo_de_burbuja(lista))
    
        else:
            print("lista vacia, no se puede proseguir")
    elif(opcion==0):
        abierto=True
        print("se cerro el programa")
    