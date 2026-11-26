# Esempi avanzati

Script da guardare con calma dopo il corso. Non servono per seguire le lezioni.
Le librerie esterne si installano una volta sola con `py -m pip install nome_libreria` (vedi lezione 3).

| File | Cosa mostra | Richiede |
| --- | --- | --- |
| [`monte_carlo_pi.py`](monte_carlo_pi.py) | Stima di π con numeri casuali (metodo Monte Carlo) | — |
| [`metodo_di_newton.py`](metodo_di_newton.py) | Risolvere equazioni con il metodo di Newton, con funzioni passate come argomenti | — |
| [`gestione_errori.py`](gestione_errori.py) | Gestire gli errori con `try` / `except`, `else`, `finally` e `raise`: prevedere i problemi invece di far fermare il programma | — |
| [`parabola.py`](parabola.py) | Disegnare la parabola e le soluzioni dell'equazione di secondo grado con matplotlib, fino ai cursori interattivi per a, b, c | matplotlib |
| [`statistica_dati.py`](statistica_dati.py) | Dati di una lista con matplotlib: istogramma e curva normale, box plot, distribuzione cumulativa, grafico di probabilità normale (Q-Q), teorema del limite centrale | matplotlib |
| [`calcolo_simbolico.py`](calcolo_simbolico.py) | SymPy (1): sviluppare e scomporre espressioni, risolvere equazioni e sistemi, formula risolutiva con parametri, formule in LaTeX | sympy |
| [`analisi_simbolica.py`](analisi_simbolica.py) | SymPy (2): derivate, integrali e limiti; dal calcolo simbolico al grafico con `lambdify` | sympy, matplotlib, numpy |
| [`bilancia_reazione.py`](bilancia_reazione.py) | Bilanciare una reazione chimica trasformandola in un sistema di equazioni risolto con SymPy | sympy |

Altri esempi (per esempio simulazioni) potranno essere aggiunti in seguito.

**Suggerimento:** cambiate un numero alla volta e osservate cosa succede. Per esempio, in
`monte_carlo_pi.py` provate a togliere `random.seed(42)` ed eseguite più volte.
