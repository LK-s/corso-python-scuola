# Lezione 2 - Ripetere con for e range

# range(n) genera 0, 1, ..., n-1
for i in range(5):
    print("Giro numero", i)

# range(inizio, fine, passo): la fine è esclusa
for n in range(1, 11):
    print(f"{n} al quadrato = {n ** 2}")

# Tabellina
numero = 7
for k in range(1, 11):
    print(f"{numero} x {k:2d} = {numero * k:3d}")

# Accumulare un risultato: somma dei primi 100 numeri naturali
somma = 0
for n in range(1, 101):
    somma += n
print("Somma da 1 a 100:", somma)       # 5050
print("Formula di Gauss:", 100 * 101 // 2)
print("Sum:", sum(range(1, 101)))

# Conto alla rovescia (passo negativo)
for t in range(5, 0, -1):
    print(t)
print("Via!")
