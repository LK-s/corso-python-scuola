# Esercizio 2 - Da voto numerico a giudizio
voto = float(input("Voto (0-10): "))

if voto < 0 or voto > 10:
    print("Voto non valido")
elif voto >= 9:
    print("Ottimo")
elif voto >= 8:
    print("Distinto")
elif voto >= 7:
    print("Buono")
elif voto >= 6:
    print("Sufficiente")
elif voto >= 5:
    print("Mediocre")
else:
    print("Insufficiente")
