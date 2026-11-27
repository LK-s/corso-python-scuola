# Esercizio 4 - Temperature mensili: escursione minima e mesi sopra la media
import csv
from pathlib import Path

CARTELLA_DATI = Path(__file__).parent.parent / "dati"

mesi, minime, massime = [], [], []
with open(CARTELLA_DATI / "temperature_mensili.csv", encoding="utf-8", newline="") as f:
    for riga in csv.DictReader(f):
        mesi.append(riga["mese"])
        minime.append(float(riga["minima"]))
        massime.append(float(riga["massima"]))

escursioni = [tmax - tmin for tmin, tmax in zip(minime, massime)]
posizione = escursioni.index(min(escursioni))
print(f"Escursione minima: {mesi[posizione]} ({escursioni[posizione]:.0f} °C)")

media_massime = sum(massime) / len(massime)
sopra = [mese for mese, tmax in zip(mesi, massime) if tmax > media_massime]
print(f"Media delle massime: {media_massime:.1f} °C")
print(f"Mesi con massima sopra la media: {len(sopra)}")
print(", ".join(sopra))
