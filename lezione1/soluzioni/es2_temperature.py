# Esercizio 2 - Da Fahrenheit a Celsius e Kelvin
fahrenheit = float(input("Temperatura in °F: "))
celsius = (fahrenheit - 32) * 5 / 9
kelvin = celsius + 273.15

print(f"{fahrenheit} °F = {celsius:.2f} °C = {kelvin:.2f} K")
