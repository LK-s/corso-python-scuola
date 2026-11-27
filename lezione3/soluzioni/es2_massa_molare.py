# Esercizio 2 - Massa molare da una formula scritta come dizionario
import csv
from pathlib import Path

CARTELLA_DATI = Path(__file__).parent.parent / "dati"

masse = {}
with open(CARTELLA_DATI / "elementi.csv", encoding="utf-8", newline="") as f:
    for riga in csv.DictReader(f):
        masse[riga["simbolo"]] = float(riga["massa"])


def massa_molare(formula):
    """formula: dizionario simbolo -> numero di atomi, per esempio {"H": 2, "O": 1}."""
    totale = 0
    for simbolo, quanti in formula.items():
        totale += masse[simbolo] * quanti
    return totale


print(f"H2O : {massa_molare({'H': 2, 'O': 1}):.3f} g/mol")
print(f"CO2 : {massa_molare({'C': 1, 'O': 2}):.3f} g/mol")
print(f"NaCl: {massa_molare({'Na': 1, 'Cl': 1}):.3f} g/mol")
