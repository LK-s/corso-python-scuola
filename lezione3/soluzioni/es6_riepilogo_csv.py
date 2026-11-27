# Esercizio 6 - Scrivere un file CSV con la media di ogni studente
import csv
from pathlib import Path

CARTELLA_DATI = Path(__file__).parent.parent / "dati"
MATERIE = ("matematica", "fisica", "chimica")

with open(CARTELLA_DATI / "voti_classe.csv", encoding="utf-8", newline="") as f:
    righe = list(csv.DictReader(f, delimiter=";"))

with open(CARTELLA_DATI / "riepilogo_voti.csv", "w", encoding="utf-8", newline="") as f:
    scrittore = csv.writer(f)
    scrittore.writerow(["studente", "media"])
    for riga in righe:
        voti = [float(riga[m].replace(",", ".")) for m in MATERIE]
        scrittore.writerow([riga["studente"], f"{sum(voti) / len(voti):.2f}"])

print(f"Scritte {len(righe)} righe in riepilogo_voti.csv")
