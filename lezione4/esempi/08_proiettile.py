# Lezione 4 - Idee per la classe (3): la traiettoria di un proiettile
# Quale angolo di lancio dà la gittata maggiore? Si confrontano tre angoli (senza attrito dell'aria).
import matplotlib.pyplot as plt
import numpy as np

VELOCITA = 20.0           # m/s
G = 9.81                  # m/s²

for angolo in (30, 45, 60):                      # gradi: provate altri angoli
    a = np.radians(angolo)                       # i calcoli vogliono i radianti
    durata = 2 * VELOCITA * np.sin(a) / G        # tempo di volo
    t = np.linspace(0, durata, 100)
    x = VELOCITA * np.cos(a) * t
    y = VELOCITA * np.sin(a) * t - 0.5 * G * t ** 2
    plt.plot(x, y, label=f"{angolo}°")
    print(f"Angolo {angolo}°: gittata {x[-1]:.1f} m, altezza massima {y.max():.1f} m")

plt.title("Traiettorie con velocità iniziale di 20 m/s")
plt.xlabel("distanza (m)")
plt.ylabel("altezza (m)")
plt.axis("equal")                                # stessa scala sui due assi
plt.legend()
plt.grid(True)
plt.show()
