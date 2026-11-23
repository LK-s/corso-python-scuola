# Esercizio 4 - Potenze di 2 e somma dei numeri dispari

for esponente in range(0, 11):
    print(f"2^{esponente} = {2 ** esponente}")

# La somma dei primi n numeri dispari è n al quadrato: verifichiamolo
for n in range(1, 11):
    somma = 0
    for k in range(n):
        somma += 2 * k + 1          # k-esimo numero dispari
    print(f"Somma dei primi {n} dispari = {somma} (n^2 = {n ** 2})", somma == n ** 2)
