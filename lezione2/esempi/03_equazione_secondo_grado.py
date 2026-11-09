# Lezione 2 - Equazione di secondo grado: a x² + b x + c = 0
import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    print("Non è un'equazione di secondo grado.")
else:
    delta = b ** 2 - 4 * a * c
    print(f"Discriminante = {delta}")

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print(f"Due soluzioni reali: x1 = {x1:.4f}, x2 = {x2:.4f}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Una soluzione doppia: x = {x:.4f}")
    else:
        print("Nessuna soluzione reale.")
