# Calcolo simbolico con SymPy (1): espressioni ed equazioni
#
# SymPy lavora con le formule come farebbe una persona con carta e penna: non con numeri,
# ma con simboli. Va installato una volta sola:   py -m pip install sympy
#
# Come usare questo file: eseguitelo e leggete i risultati accanto al codice;
# poi cambiate le formule e rilanciate.
import sympy as sp

# --- Simboli -------------------------------------------------------------------------
# Un simbolo è una "x" che resta una lettera: nessun valore, solo un nome.
x, y = sp.symbols("x y")

# --- Espressioni: espandere, scomporre, semplificare ---------------------------------
espressione = (x + 2) * (x - 3)
print("Espressione:   ", espressione)
print("Sviluppata:    ", sp.expand(espressione))               # x**2 - x - 6
print("Scomposta:     ", sp.factor(x ** 2 - 5 * x + 6))        # (x - 3)*(x - 2)
print("Semplificata:  ", sp.simplify((x ** 2 - 1) / (x - 1)))  # x + 1

# --- Sostituire un valore ------------------------------------------------------------
print("Per x = 4:     ", espressione.subs(x, 4))               # 6
print("Valore decimale:", sp.sqrt(2).evalf(10))                # 1.414213562

# --- Equazioni -----------------------------------------------------------------------
# sp.Eq(sinistra, destra) rappresenta l'equazione; sp.solve la risolve.
print("\nx² − 5x + 6 = 0  →", sp.solve(sp.Eq(x ** 2 - 5 * x + 6, 0), x))     # [2, 3]
print("x² + 1 = 0       →", sp.solve(sp.Eq(x ** 2 + 1, 0), x))              # [-I, I]: soluzioni complesse
print("x² = 2           →", sp.solve(sp.Eq(x ** 2, 2), x))                  # [-sqrt(2), sqrt(2)]

# --- Equazioni con parametri: la formula risolutiva -----------------------------------
# Con più simboli si ottiene la soluzione generale.
a, b, c = sp.symbols("a b c")
print("\nax² + bx + c = 0 →")
for soluzione in sp.solve(sp.Eq(a * x ** 2 + b * x + c, 0), x):
    print("   x =", soluzione)

# --- Sistemi di equazioni ------------------------------------------------------------
sistema = [sp.Eq(x + y, 5), sp.Eq(x - y, 1)]
print("\nSistema x + y = 5, x − y = 1 →", sp.solve(sistema, [x, y]))           # {x: 3, y: 2}

# --- Formule scritte bene ------------------------------------------------------------
# sp.latex produce il codice LaTeX, da incollare in un documento o in una presentazione.
print("\nLaTeX:", sp.latex(sp.Eq(x ** 2 - 5 * x + 6, 0)))
sp.pprint(sp.Integral(sp.sqrt(x), (x, 0, 4)))              # formula in "arte ASCII" nella Shell
