# Lezione 4 - Più grafici in una finestra: le temperature di un anno (dati di esempio)
import csv
from pathlib import Path

import matplotlib.pyplot as plt

CARTELLA_DATI = Path(__file__).parent.parent.parent / "lezione3" / "dati"

mesi = []
minime = []
massime = []
try:
    with open(CARTELLA_DATI / "temperature_mensili.csv", encoding="utf-8", newline="") as f:
        for riga in csv.DictReader(f):
            mesi.append(riga["mese"][:3])        # abbreviazione: Gen, Feb, Mar...
            minime.append(float(riga["minima"]))
            massime.append(float(riga["massima"]))
except FileNotFoundError:
    print("Non trovo temperature_mensili.csv: controllare la cartella lezione3/dati")

escursioni = [mx - mn for mn, mx in zip(minime, massime)]

# plt.subplots crea una figura con più "assi" affiancati: qui 1 riga e 2 colonne
figura, (sinistra, destra) = plt.subplots(1, 2, figsize=(12, 4.5))

sinistra.plot(mesi, massime, marker="o", color="tab:red", label="massima")
sinistra.plot(mesi, minime, marker="o", color="tab:blue", label="minima")
sinistra.fill_between(mesi, minime, massime, color="gray", alpha=0.2)   # area tra le due curve
sinistra.set_title("Temperature minime e massime")
sinistra.set_ylabel("°C")
sinistra.legend()
sinistra.grid(True)

destra.bar(mesi, escursioni, color="tab:orange")
destra.set_title("Escursione termica")
destra.set_ylabel("°C")

figura.tight_layout()            # evita che i testi si sovrappongano
plt.show()
