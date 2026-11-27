# Esercizio 7 (bonus) - Gli elementi raggruppati per gruppo della tavola periodica
import csv
from pathlib import Path

CARTELLA_DATI = Path(__file__).parent.parent / "dati"

gruppi = {}                                        # gruppo -> lista di simboli
with open(CARTELLA_DATI / "elementi.csv", encoding="utf-8", newline="") as f:
    for riga in csv.DictReader(f):
        gruppo = int(riga["gruppo"])
        if gruppo not in gruppi:
            gruppi[gruppo] = []
        gruppi[gruppo].append(riga["simbolo"])

for gruppo in sorted(gruppi):
    print(f"Gruppo {gruppo:2}: {' '.join(gruppi[gruppo])}")
