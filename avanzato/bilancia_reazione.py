# Bilanciare una reazione chimica con SymPy
#
# Idea: per ogni elemento, gli atomi a sinistra devono essere tanti quanti a destra.
# Ogni elemento dà un'equazione lineare nei coefficienti incogniti: è un sistema, che SymPy risolve.
# Richiede:   py -m pip install sympy
import sympy as sp

# Ogni sostanza è un dizionario elemento -> numero di atomi (come nella lezione 3).
reagenti = [{"C": 3, "H": 8}, {"O": 2}]                 # C3H8 + O2
prodotti = [{"C": 1, "O": 2}, {"H": 2, "O": 1}]         # CO2 + H2O

sostanze = reagenti + prodotti
elementi = sorted({e for sostanza in sostanze for e in sostanza})     # ['C', 'H', 'O']

# Matrice: una riga per elemento, una colonna per sostanza.
# I prodotti contano con il segno meno, così per ogni riga la somma deve fare zero.
righe = []
for elemento in elementi:
    riga = [sostanza.get(elemento, 0) for sostanza in reagenti]
    riga += [-sostanza.get(elemento, 0) for sostanza in prodotti]
    righe.append(riga)
matrice = sp.Matrix(righe)
print("Matrice del sistema:")
sp.pprint(matrice)

# Le soluzioni di "matrice · coefficienti = 0" sono i coefficienti cercati (a meno di un fattore).
soluzione = matrice.nullspace()[0]
# Si moltiplica per il minimo comune denominatore per avere numeri interi.
soluzione = soluzione * sp.ilcm(*[termine.q for termine in soluzione])
coefficienti = [int(termine) for termine in soluzione]


def formula(sostanza):
    """Trasforma {'C': 3, 'H': 8} in 'C3H8'."""
    return "".join(e + (str(n) if n > 1 else "") for e, n in sostanza.items())


def lato(lista, coeff):
    return " + ".join(f"{c if c > 1 else ''}{formula(s)}" for c, s in zip(coeff, lista))


n = len(reagenti)
print("\nReazione bilanciata:")
print(lato(reagenti, coefficienti[:n]), "→", lato(prodotti, coefficienti[n:]))   # C3H8 + 5O2 → 3CO2 + 4H2O

# Provate con altre reazioni, per esempio:
#   Al + O2 → Al2O3              reagenti = [{"Al": 1}, {"O": 2}]      prodotti = [{"Al": 2, "O": 3}]
#   Fe + O2 → Fe2O3              reagenti = [{"Fe": 1}, {"O": 2}]      prodotti = [{"Fe": 2, "O": 3}]
