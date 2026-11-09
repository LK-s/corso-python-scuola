# Lezione 2 - Il ciclo while: si ripete finché una condizione è vera

# 1) Quante volte si può dimezzare 1000 prima di scendere sotto 1?
valore = 1000
passi = 0
while valore >= 1:
    valore = valore / 2
    passi += 1
print("Dimezzamenti:", passi)

# 2) Congettura di Collatz: se n è pari -> n/2, se dispari -> 3n+1.
#    Si arriva sempre a 1? Nessuno lo ha dimostrato!
#    Approfondimento: https://it.wikipedia.org/wiki/Congettura_di_Collatz
n = int(input("Numero di partenza: "))
passi = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    passi += 1
print("Passi per arrivare a 1:", passi)

# 3) Attenzione ai cicli infiniti: la condizione deve poter diventare falsa.
#    In Thonny si interrompe un programma con il pulsante rosso (Stop) o Ctrl+C.
