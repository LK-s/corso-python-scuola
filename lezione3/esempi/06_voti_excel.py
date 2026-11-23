# Lezione 3 - CSV "all'italiana": separatore ; e virgola decimale (come li salva Excel)
import csv
from pathlib import Path

CARTELLA_DATI = Path(__file__).parent.parent / "dati"


def a_numero(testo):
    """Trasforma '7,5' in 7.5."""
    return float(testo.replace(",", "."))


with open(CARTELLA_DATI / "voti_classe.csv", encoding="utf-8", newline="") as f:
    lettore = csv.DictReader(f, delimiter=";")        # il separatore è il punto e virgola
    for riga in lettore:
        voti = [a_numero(riga[materia]) for materia in ("matematica", "fisica", "chimica")]
        media = sum(voti) / len(voti)
        giudizio = "ha almeno un'insufficienza" if min(voti) < 6 else ""
        print(f"{riga['studente']:8} media {media:4.2f} {giudizio}")
