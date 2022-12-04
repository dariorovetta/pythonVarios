""" Escribí una función que reciba una lista de números enteros y 
devuelva una tupla con dos listas, una con los números pares y 
otra con los números impares. """

def lista_par_impar(num):
    # Definimos una tupla, con dos listas vacias
    tupla = ([],[])
    
    # Iteramos en un rango de 10 asignando un valor creciente a i (crece de 1 en 1)
    for i in num:
        if i % 2 == 0:
            # Si el número es par, se guarda en la primer lista
            tupla[0].append(i)
        else:
            # Si el número es impar, se guarda en la segunda lista
            tupla[1].append(i)

    return tupla


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista_par_impar(lista))