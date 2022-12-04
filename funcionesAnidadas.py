lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Funcion para contar la cantidad de objetos de la lista
def contador(listado):
    total = len(listado)
    return total


print(contador(lista))
    

# Funcion para sumar los valores de la lista   
def sumatoria(listado):
    suma_de_lista = 0
    for i in listado:
        suma_de_lista += i
    return suma_de_lista


print(sumatoria(lista))


# Funcion para calcular la media de los elementos de una lista
def media (listado):
    promedio = sumatoria(listado) / contador(listado)
    return promedio

print(media(lista))