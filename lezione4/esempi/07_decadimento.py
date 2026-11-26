# Lezione 4 - Idee per la classe (2): decadimento esponenziale
# La quantità di una sostanza radioattiva si dimezza a intervalli regolari (tempo di dimezzamento).
import matplotlib.pyplot as plt
import numpy as np

QUANTITA_INIZIALE = 100.0     # grammi
DIMEZZAMENTO = 5.0            # giorni: provate a cambiarlo e a rilanciare il programma

t = np.linspace(0, 30, 300)                                  # tempo in giorni
quantita = QUANTITA_INIZIALE * 0.5 ** (t / DIMEZZAMENTO)     # N(t) = N0 · (1/2)^(t/T)

plt.plot(t, quantita, label=f"dimezzamento = {DIMEZZAMENTO:g} giorni")

# Evidenzia i primi tre dimezzamenti
tempi = [DIMEZZAMENTO * k for k in (1, 2, 3)]
resti = [QUANTITA_INIZIALE * 0.5 ** k for k in (1, 2, 3)]
plt.scatter(tempi, resti, color="red", zorder=3)
for tempo, resto in zip(tempi, resti):
    print(f"Dopo {tempo:g} giorni restano {resto:.1f} g")

plt.title("Decadimento di una sostanza radioattiva")
plt.xlabel("tempo (giorni)")
plt.ylabel("quantità (g)")
plt.legend()
plt.grid(True)
plt.show()
