# Verifica delle librerie per la lezione 4: matplotlib e numpy
# Si esegue con il pulsante verde di Thonny (F5).
import sys

print("Python", sys.version.split()[0])
print("Percorso:", sys.executable)

for nome in ("numpy", "matplotlib"):
    try:
        modulo = __import__(nome)
        print(f"OK: {nome} {modulo.__version__}")
    except ImportError:
        print(f"MANCA: {nome}. Installare con:  py -m pip install {nome}")
