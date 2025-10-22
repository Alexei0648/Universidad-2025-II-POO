




def ordenamiento_insercion(lista):
    n=len(lista)
    for i in range(1, n):
        while i>0 and lista[i] < lista[i-1]: #mientras la posición i de la lista sea mayor a cero Y sea la lista i sean menores a la posición anterior, 
                                             #osea la izquierda de la posición 1, que es cero en si 
            lista[i], lista[i-1] = lista[i-1] , lista[i] # la posición de la lista, la posición 1, se cambiara por la posición que estaba en izquierda
            i=i-1 # la posición i, se le resta una posicón, menos 1
        return lista # retorna la lista
    
lista=[2,3,9,2,4,1,0,5,7] # es el contenido de la lista
print("La lista ordenada es: ", ordenamiento_insercion(lista)) # imprime la lista ya ordenda, tecnicamente la función