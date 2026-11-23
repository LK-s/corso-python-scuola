# Lezione 3 - Elaborare dati da un CSV: le temperature di un anno (dati di esempio)
import csv
from pathlib import Path

CARTELLA_DATI = Path(__file__).parent.parent / "dati"

mesi = []
minime = []
massime = []
with open(CARTELLA_DATI / "temperature_mensili.csv", encoding="utf-8", newline="") as f:
    for riga in csv.DictReader(f):
        mesi.append(riga["mese"])
        minime.append(float(riga["minima"]))
        massime.append(float(riga["massima"]))

media_min = sum(minime) / len(minime)
media_max = sum(massime) / len(massime)
print(f"Media delle minime:  {media_min:.1f} °C")
print(f"Media delle massime: {media_max:.1f} °C")

# Il mese più caldo: la posizione del valore massimo
posizione = massime.index(max(massime))
print(f"Mese più caldo: {mesi[posizione]} ({massime[posizione]} °C)")

# Escursione termica mese per mese
for mese, tmin, tmax in zip(mesi, minime, massime):
    print(f"{mese:10} {tmin:5.1f} {tmax:5.1f}  escursione {tmax - tmin:4.1f}")

# Scrivere un nuovo CSV con le medie giornaliere
with open(CARTELLA_DATI / "temperature_medie.csv", "w", encoding="utf-8", newline="") as f:
    scrittore = csv.writer(f)
    scrittore.writerow(["mese", "media"])
    for mese, tmin, tmax in zip(mesi, minime, massime):
        scrittore.writerow([mese, (tmin + tmax) / 2])
print("Scritto temperature_medie.csv")
