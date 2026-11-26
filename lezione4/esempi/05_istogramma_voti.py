# Lezione 4 - Istogramma e box plot: i voti di una classe (dati inventati)
import csv
from pathlib import Path

import matplotlib.pyplot as plt

CARTELLA_DATI = Path(__file__).parent.parent.parent / "lezione3" / "dati"


def a_numero(testo):
    """Converte un numero scritto all'italiana (7,5) in un float."""
    return float(testo.replace(",", "."))


materie = ["matematica", "fisica", "chimica"]
voti = {materia: [] for materia in materie}     # un dizionario di liste, una per materia
try:
    with open(CARTELLA_DATI / "voti_classe.csv", encoding="utf-8", newline="") as f:
        for riga in csv.DictReader(f, delimiter=";"):
            for materia in materie:
                voti[materia].append(a_numero(riga[materia]))
except FileNotFoundError:
    print("Non trovo voti_classe.csv: controllare la cartella lezione3/dati")

# Istogramma: quanti voti cadono in ciascun intervallo (bins) tra 0 e 10
tutti = [v for lista in voti.values() for v in lista]
plt.hist(tutti, bins=range(0, 11), edgecolor="black")
plt.title("Distribuzione di tutti i voti")
plt.xlabel("voto")
plt.ylabel("numero di voti")
plt.show()

# Box plot: confronta le tre materie (mediana, quartili, valori estremi)
plt.boxplot([voti[m] for m in materie], tick_labels=materie)
plt.axhline(6, color="red", linestyle="--", linewidth=1)    # soglia di sufficienza
plt.title("Voti per materia")
plt.ylabel("voto")
plt.show()
