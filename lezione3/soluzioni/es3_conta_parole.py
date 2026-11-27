# Esercizio 3 - Quante volte compare ogni parola
frase = input("Scrivi una frase: ")

frequenze = {}
for parola in frase.lower().split():
    frequenze[parola] = frequenze.get(parola, 0) + 1

for parola, quante in frequenze.items():
    print(parola, quante)
