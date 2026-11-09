"""Disegnare la parabola y = a x^2 + b x + c e vedere le soluzioni dell'equazione di secondo grado.

Richiede matplotlib, che non è incluso in Python. Si installa dal Prompt dei comandi con
    py -m pip install matplotlib
(per lo stesso interprete usato da Thonny, vedi la guida a Thonny nella cartella risorse).

Lo script apre quattro finestre, una dopo l'altra: chiudere la finestra per passare alla successiva.
  1) la parabola
  2) la parabola con le soluzioni e il vertice
  3) i tre casi del discriminante affiancati
  4) la parabola con i cursori per a, b, c (da provare muovendo i cursori)
"""
import math

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Per uno stile "disegnato a mano" mettere True (curiosità, non cambia i calcoli).
# Gli avvisi 'findfont' sul carattere xkcd mancante sono innocui: il tratto resta a mano libera.
STILE_A_MANO = False


def risolvi(a, b, c):
    """Soluzioni reali di a x^2 + b x + c = 0 (come nell'esercizio 3 della lezione 2)."""
    if a == 0:
        return [-c / b] if b != 0 else []
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return []
    radice = math.sqrt(delta)
    return sorted({(-b - radice) / (2 * a), (-b + radice) / (2 * a)})   # l'insieme toglie il doppione se delta = 0


def punti_parabola(a, b, c, x_min, x_max, quanti=200):
    """Due liste, le ascisse e le ordinate, con 'quanti' punti equidistanti tra x_min e x_max."""
    passo = (x_max - x_min) / (quanti - 1)
    xs = [x_min + i * passo for i in range(quanti)]
    ys = [a * x ** 2 + b * x + c for x in xs]
    return xs, ys


def titolo(a, b, c):
    return f"y = {a:g}·x² {b:+g}·x {c:+g}"


# ---------------------------------------------------------------------------
# 1) La parabola: il disegno si fa con pochissime righe
# ---------------------------------------------------------------------------
def parabola_base(a, b, c):
    xs, ys = punti_parabola(a, b, c, -2, 6)
    plt.plot(xs, ys)                      # una linea che passa per i punti
    plt.axhline(0, color="black")         # l'asse x
    plt.grid(True)
    plt.title(titolo(a, b, c))
    plt.show()                            # apre la finestra


# ---------------------------------------------------------------------------
# 2) Con le soluzioni (calcolate dalla funzione risolvi) e il vertice
# ---------------------------------------------------------------------------
def disegna(ax, a, b, c, x_min=None, x_max=None):
    """Disegna nel riquadro 'ax' la parabola, le soluzioni e il vertice."""
    soluzioni = risolvi(a, b, c)
    if a != 0:
        x_vertice = -b / (2 * a)
        distanza = max([abs(x - x_vertice) for x in soluzioni] + [1]) + 1
        x_min = x_vertice - distanza if x_min is None else x_min
        x_max = x_vertice + distanza if x_max is None else x_max
    else:                                 # se a = 0 non è una parabola ma una retta: nessun vertice
        x_min = -6 if x_min is None else x_min
        x_max = 6 if x_max is None else x_max
    xs, ys = punti_parabola(a, b, c, x_min, x_max)
    ax.plot(xs, ys)
    ax.axhline(0, color="black", linewidth=1)
    ax.grid(True)
    ax.set_title(titolo(a, b, c))

    for i, x in enumerate(soluzioni):     # un punto rosso per ogni soluzione
        ax.plot(x, 0, "o", color="red")
        # la prima etichetta a sinistra del punto, la seconda a destra, per non sovrapporle
        ax.annotate(f"x = {x:.2f}", (x, 0), textcoords="offset points",
                    xytext=(-6 if i == 0 and len(soluzioni) == 2 else 6, 8),
                    ha="right" if i == 0 and len(soluzioni) == 2 else "left")
    if a != 0:                            # il vertice
        y_vertice = a * x_vertice ** 2 + b * x_vertice + c
        ax.plot(x_vertice, y_vertice, "s", color="green")
        ax.annotate("vertice", (x_vertice, y_vertice), textcoords="offset points", xytext=(6, -14))


def parabola_con_soluzioni(a, b, c):
    _, ax = plt.subplots()
    disegna(ax, a, b, c)
    print(f"Soluzioni di {titolo(a, b, c)} = 0:", risolvi(a, b, c))
    plt.show()


# ---------------------------------------------------------------------------
# 3) I tre casi del discriminante, uno accanto all'altro
# ---------------------------------------------------------------------------
def tre_casi():
    casi = [(1, -5, 6, "Δ > 0: due soluzioni"),
            (1, -4, 4, "Δ = 0: una soluzione doppia"),
            (1, -2, 3, "Δ < 0: nessuna soluzione reale")]
    _, assi = plt.subplots(1, 3, figsize=(13, 4), sharey=True)    # tre riquadri affiancati
    for ax, (a, b, c, descrizione) in zip(assi, casi):
        disegna(ax, a, b, c, x_min=-2, x_max=6)
        ax.set_title(f"{descrizione}\n{titolo(a, b, c)}")
    plt.show()


# ---------------------------------------------------------------------------
# 4) Cursori: si muovono a, b, c e il grafico si aggiorna da solo
# ---------------------------------------------------------------------------
def con_cursori():
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.32)      # lascia spazio sotto per i cursori

    def nuovo_cursore(posizione, nome, minimo, massimo, iniziale):
        riquadro = fig.add_axes([0.15, posizione, 0.7, 0.03])
        return Slider(riquadro, nome, minimo, massimo, valinit=iniziale, valstep=0.1)

    cursore_a = nuovo_cursore(0.20, "a", -3, 3, 1)
    cursore_b = nuovo_cursore(0.14, "b", -6, 6, -5)
    cursore_c = nuovo_cursore(0.08, "c", -8, 8, 6)

    def aggiorna(_):                      # chiamata ad ogni movimento di un cursore
        ax.clear()
        disegna(ax, cursore_a.val, cursore_b.val, cursore_c.val, x_min=-6, x_max=6)
        ax.set_ylim(-10, 10)
        fig.canvas.draw_idle()

    for cursore in (cursore_a, cursore_b, cursore_c):
        cursore.on_changed(aggiorna)
    aggiorna(None)                        # primo disegno
    plt.show()


if STILE_A_MANO:
    plt.xkcd()

parabola_base(1, -5, 6)
parabola_con_soluzioni(1, -5, 6)
tre_casi()
con_cursori()
