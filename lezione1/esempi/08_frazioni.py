# Lezione 1 - Numeri esatti: le frazioni
# I decimali sono approssimati (vedi 01_operatori). Il modulo fractions offre un tipo di numero
# che conserva numeratore e denominatore: i calcoli restano esatti.
from fractions import Fraction
import math

# --- Calcoli esatti ---
a = Fraction(1, 3)
b = Fraction(1, 6)
print(f"{a} + {b} = {a + b}")
print(f"{a} * {b} = {a * b}")
print(f"({a}) / ({b}) = {a / b}")
print("In decimale:", float(a + b))

# Il confronto che con i float falliva, qui funziona
print(0.1 + 0.2 == 0.3)
print(Fraction(1, 10) + Fraction(2, 10) == Fraction(3, 10))

# --- Approssimazioni razionali di π (22/7 di Archimede, 355/113 di Metius) ---
archimede = Fraction(22, 7)
metius = Fraction(355, 113)

print()
print("Frazione   Valore       Errore")
print(f"22/7       {float(archimede):.8f}   {abs(float(archimede) - math.pi):.8f}")
print(f"355/113    {float(metius):.8f}   {abs(float(metius) - math.pi):.8f}")

# Trovare la migliore frazione con denominatore limitato: la fa il computer
frazione_100 = Fraction(math.pi).limit_denominator(100)
frazione_1000 = Fraction(math.pi).limit_denominator(1000)
print()
print("Miglior frazione con denominatore <= 100:  ", frazione_100)
print("Miglior frazione con denominatore <= 1000: ", frazione_1000)

# Numeratore e denominatore sono accessibili
print("Numeratore e denominatore:", frazione_1000.numerator, frazione_1000.denominator)
