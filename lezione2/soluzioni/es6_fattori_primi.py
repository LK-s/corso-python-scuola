# Esercizio 6 - Scomposizione in fattori primi


def fattori_primi(n):
    fattori = []
    divisore = 2
    while n > 1:
        if n % divisore == 0:
            fattori.append(divisore)
            n = n // divisore
        else:
            divisore += 1
    return fattori


for numero in [12, 60, 97, 360, 1001]:
    print(numero, "=", " x ".join(str(f) for f in fattori_primi(numero)))
