# Esempi avanzati

Script da guardare con calma dopo il corso. Non servono per seguire le lezioni.
Quasi tutti usano solo la libreria standard di Python; `parabola.py` e `statistica_dati.py` richiedono anche matplotlib
(`py -m pip install matplotlib`).

| File | Cosa mostra |
| --- | --- |
| [`monte_carlo_pi.py`](monte_carlo_pi.py) | Stima di π con numeri casuali (metodo Monte Carlo) |
| [`metodo_di_newton.py`](metodo_di_newton.py) | Risolvere equazioni con il metodo di Newton, con funzioni passate come argomenti |
| [`parabola.py`](parabola.py) | Disegnare la parabola e le soluzioni dell'equazione di secondo grado con matplotlib, fino ai cursori interattivi per a, b, c |
| [`statistica_dati.py`](statistica_dati.py) | Dati di una lista con matplotlib: istogramma e curva normale, box plot, distribuzione cumulativa, grafico di probabilità normale (Q-Q), teorema del limite centrale |

Altri esempi (per esempio simulazioni e calcolo simbolico) potranno essere aggiunti in seguito.

**Suggerimento:** cambiate un numero alla volta e osservate cosa succede. Per esempio, in
`monte_carlo_pi.py` provate a togliere `random.seed(42)` ed eseguite più volte.
