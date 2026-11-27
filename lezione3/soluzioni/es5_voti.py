# Esercizio 5 - Voti di una classe: media per materia e insufficienze
import csv
from pathlib import Path

CARTELLA_DATI = Path(__file__).parent.parent / "dati"
MATERIE = ("matematica", "fisica", "chimica")

totali = {materia: 0 for materia in MATERIE}
con_insufficienze = []
studenti = 0

with open(CARTELLA_DATI / "voti_classe.csv", encoding="utf-8", newline="") as f:
    for riga in csv.DictReader(f, delimiter=";"):
        studenti += 1
        insufficiente = False
        for materia in MATERIE:
            voto = float(riga[materia].replace(",", "."))
            totali[materia] += voto
            if voto < 6:
                insufficiente = True
        if insufficiente:
            con_insufficienze.append(riga["studente"])

for materia in MATERIE:
    print(f"Media di {materia}: {totali[materia] / studenti:.2f}")
print(f"Con almeno un'insufficienza ({len(con_insufficienze)}):", ", ".join(con_insufficienze))
