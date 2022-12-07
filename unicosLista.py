def unicos(lista):
    lista1 = []
    for i in lista:
        if i in lista1:
            lista1.remove(i)
        else:
            lista1.append(i)
    return lista1


listado = [1, 2, 3, 4, 3]
print(unicos(listado))


""" def unicos(lista):
    lista1 = []
    for num in lista:
        if lista.count(num) >= 2:
            lista1.remove(num)
        else:
            lista1.append(num)
    return lista1
    
        

listado = [1, 2, 5, 4, 4]
print(unicos(listado)) """