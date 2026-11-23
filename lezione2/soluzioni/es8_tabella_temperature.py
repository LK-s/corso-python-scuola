# Esercizio 8 (bonus) - Tabella di conversione Celsius -> Fahrenheit
print(" °C      °F")
print("-----------")
for celsius in range(-10, 41, 10):
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius:3d}  {fahrenheit:6.1f}")
