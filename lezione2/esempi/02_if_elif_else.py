# Lezione 2 - Decisioni con if / elif / else

# 1) Segno di un numero
numero = float(input("Scrivi un numero: "))

if numero > 0:
    print("positivo")
elif numero < 0:
    print("negativo")
else:
    print("zero")

# 2) Acido, neutro o basico? (soluzioni acquose a 25 °C)
ph = float(input("Valore di pH: "))

if ph < 0 or ph > 14:
    print("Valore di pH non valido")
elif ph < 7:
    print("soluzione acida")
elif ph == 7:
    print("soluzione neutra")
else:
    print("soluzione basica")
