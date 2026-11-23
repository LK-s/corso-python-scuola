# Lezione 3 - Scrivere e leggere un file di testo
from pathlib import Path

# Il file viene creato nella stessa cartella di questo script
percorso = Path(__file__).parent / "appunti.txt"

# "w" = scrittura (se il file esiste, viene sostituito)
with open(percorso, "w", encoding="utf-8") as f:
    f.write("Prima riga\n")
    f.write("Seconda riga, con le lettere accentate: è à ù\n")
    f.write("Terza riga\n")

# "r" = lettura. with chiude il file da solo alla fine del blocco.
try:
    with open(percorso, encoding="utf-8") as f:
        for numero, riga in enumerate(f, start=1):
            print(numero, riga.strip())      # strip() toglie lo "a capo" finale
except FileNotFoundError:
    print("File non trovato:", percorso)

# "a" = aggiunge in fondo senza cancellare
with open(percorso, "a", encoding="utf-8") as f:
    f.write("Una riga aggiunta\n")

# Si può anche leggere tutto il file in una sola stringa
with open(percorso, encoding="utf-8") as f:
    contenuto = f.read()
print(len(contenuto.splitlines()), "righe in totale")
