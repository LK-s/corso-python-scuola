# Esercizio 1 - Sfera: volume e superficie dato il raggio
import math

raggio = float(input("Raggio della sfera: "))
volume = 4 / 3 * math.pi * raggio**3
superficie = 4 * math.pi * raggio**2

print(f"Volume:     {volume:.3f}")
print(f"Superficie: {superficie:.3f}")
