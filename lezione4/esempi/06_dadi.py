# Lezione 4 - Idee per la classe (1): una simulazione con i dadi
# Si lanciano due dadi molte volte e si confronta ciò che si ottiene con la probabilità teorica.
import random

import matplotlib.pyplot as plt

LANCI = 10000            # provate a cambiarlo: 100, 1000, 100000...

random.seed(42)          # risultati sempre uguali; togliete questa riga per averli diversi a ogni esecuzione

# Conta quante volte esce ogni somma (da 2 a 12)
frequenze = {somma: 0 for somma in range(2, 13)}
for _ in range(LANCI):
    somma = random.randint(1, 6) + random.randint(1, 6)
    frequenze[somma] += 1

somme = list(frequenze.keys())
osservate = [frequenze[s] / LANCI for s in somme]            # frequenze relative
teoriche = [(6 - abs(s - 7)) / 36 for s in somme]            # 1/36, 2/36, ..., 6/36, ..., 1/36

plt.bar(somme, osservate, color="tab:blue", label="simulazione")
plt.plot(somme, teoriche, "o-", color="red", label="teoria")
plt.title(f"Somma di due dadi: {LANCI} lanci")
plt.xlabel("somma")
plt.ylabel("frequenza relativa")
plt.xticks(somme)
plt.legend()
plt.show()
