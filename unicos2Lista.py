def lista_de_unicos(lista):
    resultado = []
    orden = sorted(resultado)
    for i in range(len(lista)):
        if lista[i+1:].count(lista[i])==0:
            resultado.append(lista[i])
    return sorted(resultado)

listado = [5, 4, 2, 1, 0]
print(lista_de_unicos(listado))
listado.sort()
print(listado)