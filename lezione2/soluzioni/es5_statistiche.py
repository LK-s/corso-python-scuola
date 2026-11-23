# Esercizio 5 - Statistiche elementari su una lista di misure
misure = [12.1, 11.8, 12.4, 12.0, 11.9, 12.6, 12.2]

media = sum(misure) / len(misure)
minimo = min(misure)
massimo = max(misure)

sopra = 0
for m in misure:
    if m > media:
        sopra += 1

print(f"Numero di misure: {len(misure)}")
print(f"Media: {media:.3f}")
print(f"Minimo: {minimo}  Massimo: {massimo}  Escursione: {massimo - minimo:.1f}")
print(f"Misure sopra la media: {sopra}")
