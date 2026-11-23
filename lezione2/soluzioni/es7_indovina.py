# Esercizio 7 (bonus) - Indovina il numero
import random

segreto = random.randint(1, 100)
tentativi = 0

print("Ho pensato a un numero tra 1 e 100.")
while True:
    proposta = int(input("Il tuo tentativo: "))
    tentativi += 1
    if proposta < segreto:
        print("Troppo basso")
    elif proposta > segreto:
        print("Troppo alto")
    else:
        print(f"Esatto! Ci sei riuscito in {tentativi} tentativi.")
        break
