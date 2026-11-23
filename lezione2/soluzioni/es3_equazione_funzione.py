# Esercizio 3 - Equazione di secondo grado come funzione
import math


def risolvi(a, b, c):
    """Restituisce la lista delle soluzioni reali di a x^2 + b x + c = 0."""
    if a == 0:
        if b == 0:
            return []                 # nessuna x (o infinite, se anche c è 0)
        return [-c / b]               # equazione di primo grado
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return []
    if delta == 0:
        return [-b / (2 * a)]
    radice = math.sqrt(delta)
    return [(-b - radice) / (2 * a), (-b + radice) / (2 * a)]


print(risolvi(1, -5, 6))     # [2.0, 3.0]
print(risolvi(1, 2, 1))      # [-1.0]
print(risolvi(1, 0, 1))      # []
print(risolvi(0, 2, -4))     # [2.0]
print(risolvi(2, 3, -2))     # [-2.0, 0.5]
