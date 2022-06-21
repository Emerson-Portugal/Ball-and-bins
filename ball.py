import itertools
import operator
import time

def combinations_with_replacement_counts(n, r):
    size = n + r - 1
    for indices in itertools.combinations(range(size), n-1):
        starts = [0] + [index+1 for index in indices]
        stops = indices + (size,)
        yield tuple(map(operator.sub, stops, starts))
inicio = time.time()
print(list(combinations_with_replacement_counts(2, 3)))
fin = time.time()

print(fin-inicio)
# Para mostrar que el algoritmo funciona, doy un ejemplo con valores reales, 2 cajas  y 3 bolas