# Lezione 3 - Importare un modulo nostro e uno della libreria standard
import statistics

import miei_strumenti                      # il file miei_strumenti.py, accanto a questo
from miei_strumenti import e_primo         # oppure solo una funzione

voti = [6, 7.5, 8, 5.5]
print(miei_strumenti.media(voti))
print(statistics.median(voti))             # la mediana, dalla libreria standard
print(e_primo(97))

eta = miei_strumenti.leggi_numero("Quanti anni hai? ")
print(f"Tra 10 anni ne avrai {eta + 10:.0f}")
