# Lezione 4 - Dal file CSV al grafico: i primi 36 elementi della tavola periodica
import csv
from pathlib import Path

import matplotlib.pyplot as plt

CARTELLA_DATI = Path(__file__).parent.parent.parent / "lezione3" / "dati"

elementi = []
try:
    with open(CARTELLA_DATI / "elementi.csv", encoding="utf-8", newline="") as f:
        for riga in csv.DictReader(f):
            riga["massa"] = float(riga["massa"])
            riga["numero_atomico"] = int(riga["numero_atomico"])
            elementi.append(riga)
except FileNotFoundError:
    print("Non trovo elementi.csv: controllare la cartella lezione3/dati")

# Una lista per ogni colonna che serve al grafico
numeri = [e["numero_atomico"] for e in elementi]
masse = [e["massa"] for e in elementi]

# Grafico 1: la massa cresce con il numero atomico
plt.scatter(numeri, masse)
for e in elementi:
    if e["gruppo"] == "18":                      # scrive il simbolo solo accanto ai gas nobili
        plt.annotate(e["simbolo"], (e["numero_atomico"], e["massa"]),
                     textcoords="offset points", xytext=(6, -12))
plt.title("Massa atomica e numero atomico")
plt.xlabel("numero atomico")
plt.ylabel("massa atomica (u)")
plt.grid(True)
plt.show()

# Grafico 2: grafico a barre delle masse dei primi dieci elementi
primi = elementi[:10]
simboli = [e["simbolo"] for e in primi]
plt.bar(simboli, [e["massa"] for e in primi], color="tab:green")
plt.title("Massa atomica dei primi dieci elementi")
plt.ylabel("massa atomica (u)")
plt.show()
