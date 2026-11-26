# Calcolo simbolico con SymPy (2): derivate, integrali, limiti e grafici
#
# Richiede:   py -m pip install sympy matplotlib numpy
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

x = sp.symbols("x")

# --- Derivate ------------------------------------------------------------------------
f = x ** 3 - 3 * x
derivata = sp.diff(f, x)                                   # 3*x**2 - 3
print("f(x)  =", f)
print("f'(x) =", derivata)
print("f''(x) =", sp.diff(f, x, 2))                         # derivata seconda: 6*x
print("Punti con tangente orizzontale (f' = 0):", sp.solve(derivata, x))     # [-1, 1]

# Qualche derivata "da tabella"
print("\nd/dx sin(x)·x²  =", sp.diff(sp.sin(x) * x ** 2, x))
print("d/dx exp(2x)    =", sp.diff(sp.exp(2 * x), x))
print("d/dx ln(x)      =", sp.diff(sp.log(x), x))

# --- Integrali -----------------------------------------------------------------------
print("\nIntegrale indefinito di x²:       ", sp.integrate(x ** 2, x))                 # x**3/3
print("Integrale definito di x² da 0 a 3:", sp.integrate(x ** 2, (x, 0, 3)))           # 9
print("Integrale di sin(x) da 0 a π:     ", sp.integrate(sp.sin(x), (x, 0, sp.pi)))    # 2
print("Integrale di exp(−x²) su tutta la retta:", sp.integrate(sp.exp(-x ** 2), (x, -sp.oo, sp.oo)))   # sqrt(pi)

# --- Limiti --------------------------------------------------------------------------
print("\nLimite di sin(x)/x per x→0:     ", sp.limit(sp.sin(x) / x, x, 0))               # 1
print("Limite di (1 + 1/x)^x per x→∞:  ", sp.limit((1 + 1 / x) ** x, x, sp.oo))          # E
print("Limite di 1/x per x→0 da destra:", sp.limit(1 / x, x, 0, "+"))                   # oo

# --- Dal calcolo simbolico al grafico: lambdify -------------------------------------
# sp.lambdify trasforma una formula di SymPy in una funzione che numpy sa calcolare
# su molti valori insieme: così si possono disegnare funzione e derivata.
funzione = sp.lambdify(x, f, "numpy")
funzione_derivata = sp.lambdify(x, derivata, "numpy")

valori = np.linspace(-2.5, 2.5, 300)
plt.plot(valori, funzione(valori), label="f(x) = x³ − 3x")
plt.plot(valori, funzione_derivata(valori), label="f'(x) = 3x² − 3", linestyle="--")
plt.axhline(0, color="black", linewidth=0.8)
plt.title("Una funzione e la sua derivata")
plt.legend()
plt.grid(True)
plt.show()
