# Definimos una lista
enteros = [1, 2, 3, 4, 5]

# Definimos una lista por comprensión
enteros_mas_uno = [numero + 1 for numero in enteros]

print(enteros_mas_uno)

# Además, optativamente, también es posible establecer condiciones que nos permitan filtrar
# los elementos dentro del iterable. Para ello, naturalmente, debemos incluir un llamado al
# if luego de declarar al iterable:

# definimos una lista
enteros = [1, 2, 3, 4, 5]

# definimos una lista por comprensión
enteros_mas_uno = [numero + 1  for  numero  in  enteros if numero > 3]

print(enteros_mas_uno)
