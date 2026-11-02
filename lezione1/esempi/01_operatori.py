# Lezione 1 - Operatori aritmetici
# Eseguite il file (F5 in Thonny), osservate l'output, poi cambiate i numeri e riprovate.

print("Somma:            ", 7 + 2)
print("Differenza:       ", 7 - 2)
print("Prodotto:         ", 7 * 2)
print("Divisione:        ", 7 / 2)    # il risultato è sempre un numero decimale (float)
print("Divisione intera: ", 7 // 2)   # il quoziente, senza decimali
print("Resto (modulo):   ", 7 % 2)
print("Potenza:          ", 7 ** 2)

# Precedenza degli operatori: come in matematica
print(2 + 3 * 4)      # 14
print((2 + 3) * 4)    # 20
print(2 ** 3 ** 2)    # 512: la potenza si legge da destra, cioè 2 ** (3 ** 2)
print(-2 ** 2)        # -4: la potenza ha la precedenza sul segno meno

# I numeri decimali sono approssimati (vale per tutti i linguaggi)
print(0.1 + 0.2)              # 0.30000000000000004
print(0.1 + 0.2 == 0.3)       # False
print(round(0.1 + 0.2, 2))    # 0.3

# Gli interi, invece, sono esatti e senza limite di grandezza
print(2 ** 100)
