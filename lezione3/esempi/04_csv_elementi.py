# Lezione 3 - Leggere un file CSV: i primi 36 elementi della tavola periodica
import csv
from pathlib import Path

CARTELLA_DATI = Path(__file__).parent.parent / "dati"

# DictReader legge ogni riga come un dizionario: le chiavi sono i nomi delle colonne
elementi = []
try:
    with open(CARTELLA_DATI / "elementi.csv", encoding="utf-8", newline="") as f:
        for riga in csv.DictReader(f):
            riga["massa"] = float(riga["massa"])             # nel file tutto è testo
            riga["numero_atomico"] = int(riga["numero_atomico"])
            elementi.append(riga)
except FileNotFoundError:
    print("Non trovo elementi.csv: controllare la cartella dati")
    elementi = []

print(len(elementi), "elementi letti")
print(elementi[0])

# Un dizionario simbolo -> massa, per cercare al volo
masse = {e["simbolo"]: e["massa"] for e in elementi}
print("Massa del ferro:", masse["Fe"])

# Filtrare: i gas nobili (gruppo 18)
nobili = [e["nome"] for e in elementi if e["gruppo"] == "18"]
print("Gas nobili:", ", ".join(nobili))

# Gli elementi più pesanti di 70
for e in elementi:
    if e["massa"] > 70:
        print(f"{e['simbolo']:3} {e['nome']:10} {e['massa']:7.3f}")
