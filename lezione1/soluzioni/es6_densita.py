# Esercizio 6 - Densità di un oggetto da massa e dimensioni
# Un parallelepipedo di cui si misurano massa (g) e lati (cm).
massa = float(input("Massa (g): "))
lato1 = float(input("Lato 1 (cm): "))
lato2 = float(input("Lato 2 (cm): "))
lato3 = float(input("Lato 3 (cm): "))

volume = lato1 * lato2 * lato3
densita = massa / volume

print(f"Volume: {volume:.2f} cm³")
print(f"Densità: {densita:.3f} g/cm³ = {densita * 1000:.0f} kg/m³")
