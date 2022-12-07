def cuadrados():
    lista = []
    for i in range(1, 31):
        cuadrado = i ** 2
        lista.append(cuadrado)
    return lista


print(cuadrados())