def a(lista):
    
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[1] == lista[j]:
                return True
    return False