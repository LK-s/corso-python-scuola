# Lezione 3 - I dizionari: una raccolta di coppie chiave -> valore

masse = {"H": 1.008, "C": 12.011, "N": 14.007, "O": 15.999}

print(masse["O"])               # si cerca con la chiave, non con la posizione
print(len(masse))               # numero di coppie

masse["Na"] = 22.990            # aggiunge una coppia
masse["H"] = 1.00794            # se la chiave esiste, cambia il valore

print("C" in masse)             # True: la chiave c'è
print("Xx" in masse)            # False

# get() non dà errore se la chiave manca: restituisce il valore indicato (o None)
print(masse.get("Fe"))
print(masse.get("Fe", "sconosciuto"))

# Scorrere un dizionario
for simbolo in masse:
    print(simbolo, masse[simbolo])

for simbolo, massa in masse.items():
    print(f"{simbolo:3} {massa:8.3f}")

# Un dizionario può contenere altri dizionari o liste
molecola = {"nome": "acqua", "formula": "H2O", "atomi": {"H": 2, "O": 1}}
print(molecola["atomi"]["H"])

# Massa molare dell'acqua: somma di (massa dell'elemento * numero di atomi)
massa_molare = 0
for simbolo, quanti in molecola["atomi"].items():
    massa_molare += masse[simbolo] * quanti
print(f"Massa molare di {molecola['formula']}: {massa_molare:.3f} g/mol")
