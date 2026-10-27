"""Controllo dell'installazione: aprite questo file in Thonny ed eseguitelo (F5)."""
import math
import sys

print("Versione di Python:", sys.version.split()[0])
print("Percorso dell'interprete:", sys.executable)

if sys.version_info >= (3, 15):
    print("OK: state usando Python 3.15 o successivo.")
else:
    print("Attenzione: la versione è precedente alla 3.15.")
    print("Controllate Strumenti -> Opzioni -> Interprete in Thonny.")

print()
print("Prova di calcolo: la radice quadrata di 2 è", math.sqrt(2))
print("Prova di accenti e simboli: °C  µm  ≤  π  è  à  ù")
