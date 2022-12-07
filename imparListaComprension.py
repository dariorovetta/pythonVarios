# Escribí una función que, dado un número, devuelva una lista con
#  los números impares comprendidos entre 0 y ese número (sin incluirlo).
#  Como condición, la función se debe construir con una lista por comprensión.

def impares(numero):
    return [ x for x in range(numero) if x%2 != 0]


print(impares(5))