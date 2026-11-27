# Esercizio 1 - Cercare un elemento per simbolo
import csv
from pathlib import Path

CARTELLA_DATI = Path(__file__).parent.parent / "dati"

elementi = {}                                     # simbolo -> riga con tutti i dati
with open(CARTELLA_DATI / "elementi.csv", encoding="utf-8", newline="") as f:
    for riga in csv.DictReader(f):
        elementi[riga["simbolo"]] = riga

simbolo = input("Simbolo dell'elemento: ").strip().capitalize()
if simbolo in elementi:
    e = elementi[simbolo]
    print(f"{e['nome']}, numero atomico {e['numero_atomico']}, massa {float(e['massa']):.3f}")
else:
    print("Elemento non trovato")
