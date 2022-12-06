def repetidos(lista):
  prueba = len(lista) == len(set(lista))
  return prueba

listado = [55, 2, 9, 45, 4, 3, 99, 89, 6, 1, 8]
print(repetidos(listado))
