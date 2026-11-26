# Lezione 4 - Il grafico di una funzione, con un po' di numpy
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# np.linspace(inizio, fine, quanti) crea una sequenza di numeri equidistanti.
# Con 200 punti la curva appare liscia.
x = np.linspace(-2 * np.pi, 2 * np.pi, 200)

# Una funzione di numpy si applica a tutti i valori insieme: niente ciclo for
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="seno")
plt.plot(x, y2, label="coseno")
plt.axhline(0, color="black", linewidth=0.8)     # linea orizzontale sull'asse x
plt.title("Seno e coseno")
plt.xlabel("x (radianti)")
plt.legend()                                     # mostra le etichette (label)
plt.grid(True)
plt.show()

# Una parabola: anche le operazioni aritmetiche valgono per tutti i valori insieme
x = np.linspace(-1, 5, 200)
y = x ** 2 - 4 * x + 3                           # zeri in x = 1 e x = 3

plt.plot(x, y, label="y = x² − 4x + 3")
plt.scatter([1, 3], [0, 0], color="red", zorder=3, label="zeri")   # evidenzia due punti
plt.axhline(0, color="black", linewidth=0.8)
plt.title("Una parabola e i suoi zeri")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

# Salvare il grafico in un'immagine (prima di show, che poi chiude la figura)
plt.savefig(Path(__file__).parent / "parabola.png", dpi=150)
plt.show()
