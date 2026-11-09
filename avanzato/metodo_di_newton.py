"""Metodo di Newton per risolvere f(x) = 0 (solo libreria standard).

x_nuovo = x - f(x) / f'(x)
Esempi: radice quadrata di 2 e soluzione di cos(x) = x.
"""
import math


def newton(f, derivata, x0, tolleranza=1e-12, max_passi=50):
    x = x0
    for passo in range(1, max_passi + 1):
        x_nuovo = x - f(x) / derivata(x)
        if abs(x_nuovo - x) < tolleranza:
            return x_nuovo, passo
        x = x_nuovo
    raise RuntimeError("Il metodo non converge")


# sqrt(2) è la soluzione positiva di x^2 - 2 = 0
x, passi = newton(lambda x: x ** 2 - 2, lambda x: 2 * x, 1.0)
print(f"sqrt(2) ≈ {x!r} in {passi} passi (math.sqrt: {math.sqrt(2)!r})")

# soluzione di cos(x) - x = 0
x, passi = newton(lambda x: math.cos(x) - x, lambda x: -math.sin(x) - 1, 1.0)
print(f"cos(x) = x per x ≈ {x:.10f} in {passi} passi")
