"""Visualizzare i dati di una lista: media, distribuzione e grafici probabilistici.

Parte dalla lista di misure dell'esercizio 5 della lezione 2 e arriva a grafici che si usano nei laboratori
e nello studio della probabilità. Per avere abbastanza dati i numeri vengono simulati con il modulo random
(la lista è sempre una lista: cambia solo quanti elementi ha).

Richiede matplotlib, che non è incluso in Python. Si installa dal Prompt dei comandi con
    py -m pip install matplotlib
(per lo stesso interprete usato da Thonny, vedi la guida a Thonny nella cartella risorse).

Lo script apre cinque finestre, una dopo l'altra: chiudere la finestra per passare alla successiva.
  1) la lista di misure dell'esercizio 5, con media e deviazione standard
  2) 1000 misure simulate: istogramma e curva normale (gaussiana)
  3) diagramma a scatola (box plot) e funzione di distribuzione cumulativa
  4) grafico di probabilità normale (Q-Q plot): dati normali e dati non normali a confronto
  5) teorema del limite centrale: la somma di molti dadi assomiglia a una curva normale
"""
import math
import random
import statistics
from statistics import NormalDist

import matplotlib.pyplot as plt

random.seed(42)          # numeri casuali riproducibili; togliere per risultati diversi a ogni esecuzione


def curva_normale(media, sigma, x_min, x_max, quanti=200):
    """Ascisse e ordinate della densità di probabilità normale con la media e la deviazione date."""
    passo = (x_max - x_min) / (quanti - 1)
    xs = [x_min + i * passo for i in range(quanti)]
    normale = NormalDist(media, sigma)           # oggetto "distribuzione normale" della libreria standard
    return xs, [normale.pdf(x) for x in xs]


# ---------------------------------------------------------------------------
# 1) Una lista di misure, con media e deviazione standard
# ---------------------------------------------------------------------------
def misure_con_media():
    misure = [12.1, 11.8, 12.4, 12.0, 11.9, 12.6, 12.2]       # la lista dell'esercizio 5
    media = statistics.mean(misure)
    sigma = statistics.stdev(misure)
    print(f"Media {media:.3f}, deviazione standard {sigma:.3f}")

    numeri = list(range(1, len(misure) + 1))
    plt.plot(numeri, misure, "o", label="misure")
    plt.axhline(media, color="red", label=f"media = {media:.2f}")
    plt.axhspan(media - sigma, media + sigma, color="red", alpha=0.15, label="media ± deviazione standard")
    plt.xlabel("numero della misura")
    plt.ylabel("valore")
    plt.title("Sette misure ripetute")
    plt.legend()
    plt.show()


# ---------------------------------------------------------------------------
# 2) Tante misure: l'istogramma e la curva normale
# ---------------------------------------------------------------------------
def istogramma_e_curva(dati):
    media = statistics.mean(dati)
    sigma = statistics.stdev(dati)
    plt.hist(dati, bins=30, density=True, alpha=0.6, label="dati")    # density: l'area totale vale 1
    xs, ys = curva_normale(media, sigma, min(dati), max(dati))
    plt.plot(xs, ys, color="red", label="curva normale")
    plt.title(f"{len(dati)} misure: media {media:.3f}, deviazione standard {sigma:.3f}")
    plt.xlabel("valore")
    plt.ylabel("densità di probabilità")
    plt.legend()
    plt.show()


# ---------------------------------------------------------------------------
# 3) Box plot e funzione di distribuzione cumulativa
# ---------------------------------------------------------------------------
def scatola_e_cumulativa(dati):
    media = statistics.mean(dati)
    sigma = statistics.stdev(dati)
    _, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

    ax1.boxplot(dati)                     # scatola = dal 1° al 3° quartile, riga = mediana
    ax1.set_title("Box plot: mediana, quartili, valori anomali")
    ax1.set_ylabel("valore")

    ordinati = sorted(dati)
    n = len(ordinati)
    frazioni = [(i + 1) / n for i in range(n)]            # quota di dati minori o uguali a ciascun valore
    ax2.step(ordinati, frazioni, where="post", label="dati")
    normale = NormalDist(media, sigma)
    ax2.plot(ordinati, [normale.cdf(x) for x in ordinati], color="red", linestyle="--", label="normale teorica")
    ax2.set_title("Distribuzione cumulativa")
    ax2.set_xlabel("valore")
    ax2.set_ylabel("probabilità di un dato ≤ valore")
    ax2.legend()
    plt.show()


# ---------------------------------------------------------------------------
# 4) Grafico di probabilità normale (Q-Q plot)
# ---------------------------------------------------------------------------
def quantili_normali(dati):
    """Per i dati ordinati, i valori che una distribuzione normale standard assegnerebbe ai loro quantili."""
    n = len(dati)
    return [NormalDist().inv_cdf((i + 0.5) / n) for i in range(n)]


def grafico_probabilita(normali, non_normali):
    _, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))
    for ax, dati, nome in ((ax1, normali, "dati normali"),
                           (ax2, non_normali, "dati non normali (tempi di attesa)")):
        ordinati = sorted(dati)
        teorici = quantili_normali(ordinati)
        media = statistics.mean(dati)
        sigma = statistics.stdev(dati)
        ax.plot(teorici, ordinati, "o", markersize=3, label="dati")
        ax.plot([teorici[0], teorici[-1]], [media + sigma * teorici[0], media + sigma * teorici[-1]],
                color="red", label="se i dati fossero normali")
        ax.set_title(nome)
        ax.set_xlabel("quantili teorici della normale")
        ax.set_ylabel("quantili dei dati")
        ax.legend()
    plt.show()


# ---------------------------------------------------------------------------
# 5) Teorema del limite centrale: somma di k dadi
# ---------------------------------------------------------------------------
def limite_centrale():
    _, assi = plt.subplots(1, 4, figsize=(14, 3.8))
    for ax, k in zip(assi, (1, 2, 5, 30)):
        somme = [sum(random.randint(1, 6) for _ in range(k)) for _ in range(5000)]
        bordi = [x - 0.5 for x in range(k, 6 * k + 2)]      # un riquadro per ogni possibile somma
        ax.hist(somme, bins=bordi, density=True, alpha=0.6)
        media = 3.5 * k                                     # media e varianza della somma di k dadi
        sigma = math.sqrt(35 / 12 * k)
        x_min = max(k - 0.5, media - 4 * sigma)             # si mostra solo la zona dove stanno i dati
        x_max = min(6 * k + 0.5, media + 4 * sigma)
        xs, ys = curva_normale(media, sigma, x_min, x_max)
        ax.plot(xs, ys, color="red")
        ax.set_xlim(x_min, x_max)
        ax.set_title(f"somma di {k} dad{'o' if k == 1 else 'i'}")
    plt.show()


misure_con_media()

# Mille misure di una stessa grandezza, con un errore casuale (distribuzione normale)
misure_simulate = [random.gauss(12.1, 0.3) for _ in range(1000)]
# Mille tempi di attesa (distribuzione esponenziale): hanno la stessa media ma non sono normali
tempi_attesa = [random.expovariate(1 / 12.1) for _ in range(1000)]

istogramma_e_curva(misure_simulate)
scatola_e_cumulativa(misure_simulate)
grafico_probabilita(misure_simulate, tempi_attesa)
limite_centrale()
