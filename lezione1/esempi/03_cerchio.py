# Lezione 1 - Il modulo math: un'aiuola circolare
# Problema: quanta rete serve per recintare un'aiuola circolare e quanta terra per riempirla?
# Il programma è organizzato in tre blocchi: dati, calcoli, risultati.
import math

# --- Dati ---
raggio = 4.5          # metri
profondita = 0.30     # metri di terra

# --- Calcoli ---
circonferenza = 2 * math.pi * raggio
area = math.pi * raggio ** 2
volume_terra = area * profondita

# --- Risultati ---
print(f"Aiuola di raggio {raggio} m")
print(f"Rete per la recinzione: {circonferenza:.2f} m")
print(f"Superficie: {area:.2f} m²")
print(f"Terra necessaria: {volume_terra:.2f} m³")

# --- Quanto è buona un'approssimazione di π? ---
# math.pi ha 15-16 cifre esatte; confrontiamo con due valori che si usano a scuola
area_scuola = 3.14 * raggio ** 2
print(f"Con π = 3.14 l'area risulta {area_scuola:.2f} m²: differenza di {abs(area - area_scuola):.3f} m²")

# --- Altre funzioni utili del modulo math ---
print(math.sqrt(144))      # radice quadrata
print(math.sin(math.pi / 6))
print(math.log10(1000))
print(math.floor(3.7), math.ceil(3.2))
