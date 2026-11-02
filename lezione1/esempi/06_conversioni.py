# Lezione 1 - Conversioni di unità di misura

velocita_kmh = float(input("Velocità in km/h: "))
velocita_ms = velocita_kmh / 3.6
print(f"{velocita_kmh} km/h = {velocita_ms:.2f} m/s")

celsius = float(input("Temperatura in °C: "))
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15
print(f"{celsius} °C = {fahrenheit:.1f} °F = {kelvin:.2f} K")
