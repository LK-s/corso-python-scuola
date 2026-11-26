# Verifica delle librerie per la lezione 4: numpy e matplotlib (e, facoltativa, sympy)
# Si esegue con il pulsante verde di Thonny (F5). Non apre finestre.
import sys

print("Python", sys.version.split()[0])
print("Percorso:", sys.executable)
print()

problemi = 0

# --- numpy: lo stesso calcolo che useremo per disegnare le funzioni ---
try:
    import numpy as np

    x = np.linspace(-1, 5, 200)
    y = x ** 2 - 4 * x + 3
    print(f"OK: numpy {np.__version__} (200 valori calcolati)")
except ImportError:
    print("MANCA: numpy. Installare con:  py -m pip install numpy")
    problemi += 1

# --- matplotlib: prova a disegnare i tipi di grafico degli esempi, senza aprire finestre ---
try:
    import matplotlib

    matplotlib.use("Agg")                  # solo per questa prova: disegna in memoria
    import matplotlib.pyplot as plt

    plt.plot([0, 1, 2], [0, 1, 4])         # plot (esempi 01, 02, 07, 08)
    plt.scatter([0, 1, 2], [0, 1, 4])      # scatter (esempio 03)
    plt.bar(["a", "b"], [1, 2])            # barre (esempi 03, 04, 06)
    plt.hist([1, 2, 2, 3], bins=range(0, 5))                     # istogramma (esempio 05)
    plt.boxplot([[1, 2, 3], [2, 3, 4]], tick_labels=["a", "b"])  # box plot (esempio 05)
    figura, assi = plt.subplots(1, 2)      # più grafici in una finestra (esempio 04)
    plt.close("all")
    print(f"OK: matplotlib {matplotlib.__version__} (tutti i tipi di grafico degli esempi funzionano)")
except ImportError:
    print("MANCA: matplotlib. Installare con:  py -m pip install matplotlib")
    problemi += 1
except TypeError as errore:
    print(f"matplotlib è installato ma troppo vecchio per gli esempi ({errore}).")
    print("Aggiornare con:  py -m pip install --upgrade matplotlib")
    problemi += 1

# --- sympy: facoltativa, serve solo per gli esempi nella cartella avanzato ---
try:
    import sympy

    print(f"OK: sympy {sympy.__version__} (facoltativa)")
except ImportError:
    print("sympy non installata (facoltativa, solo per avanzato):  py -m pip install sympy")

print()
if problemi == 0:
    print("Tutto pronto per la lezione 4.")
else:
    print(f"Da sistemare: {problemi}. Dopo l'installazione eseguite di nuovo questo programma.")
