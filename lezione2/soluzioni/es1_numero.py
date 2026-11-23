# Esercizio 1 - Pari o dispari? Multiplo di 3?
n = int(input("Scrivi un numero intero: "))

if n % 2 == 0:
    print(f"{n} è pari")
else:
    print(f"{n} è dispari")

if n % 3 == 0:
    print(f"{n} è multiplo di 3")
else:
    print(f"{n} non è multiplo di 3")
