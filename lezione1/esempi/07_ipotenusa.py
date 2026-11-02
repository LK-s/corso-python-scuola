# Lezione 1 - Teorema di Pitagora e formula di Erone
# Dati due cateti calcoliamo ipotenusa, perimetro e area in due modi diversi,
# poi controlliamo che i risultati coincidano.
# Valori di prova: 3 e 4 (ipotenusa 5), poi 5 e 7.
import math

# --- Dati ---
cateto1 = float(input("Primo cateto: "))
cateto2 = float(input("Secondo cateto: "))

# --- Calcoli ---
ipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
perimetro = cateto1 + cateto2 + ipotenusa
area = cateto1 * cateto2 / 2

# Seconda strada per l'area: formula di Erone con il semiperimetro
s = perimetro / 2
area_erone = math.sqrt(s * (s - cateto1) * (s - cateto2) * (s - ipotenusa))

# --- Risultati ---
print(f"Ipotenusa: {ipotenusa:.3f}")
print(f"Perimetro: {perimetro:.3f}")
print(f"Area (cateti): {area:.3f}")
print(f"Area (Erone):  {area_erone:.3f}")

# --- Controlli ---
print("Controllo con math.hypot:", math.hypot(cateto1, cateto2))
# Un numero decimale "sa" dire se è in realtà intero
print("Terna pitagorica (ipotenusa intera)?", ipotenusa.is_integer())
