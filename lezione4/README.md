# Lezione 4 – Grafici con matplotlib

**Obiettivi:** disegnare grafici di funzioni e di dati con `matplotlib`, usare `numpy` per calcolare molti valori in un colpo solo,
vedere qualche idea per portare Python in classe.

**Prima della lezione:** `matplotlib` e `numpy` devono essere installati (vedi lezione 3). Il programma
`../lezione3/esempi/verifica_librerie.py` controlla che ci siano e che funzionino i tipi di grafico usati negli esempi.

**Esempi** (cartella `esempi/`): `01_primo_grafico` · `02_funzioni` · `03_grafici_elementi` · `04_grafici_temperature` ·
`05_istogramma_voti` · idee per la classe: `06_dadi` · `07_decadimento` · `08_proiettile`

**Dati:** i programmi `03`, `04` e `05` leggono i file della cartella `../lezione3/dati/` (restano dove sono: non spostateli).

Quando si lancia un programma con un grafico si apre una finestra: va chiusa perché il programma continui (e finisca).

## Riepilogo

### Il primo grafico
```python
import matplotlib.pyplot as plt          # per convenzione si chiama plt

x = [0, 1, 2, 3, 4, 5]
y = [n ** 2 for n in x]

plt.plot(x, y)                           # linea; con marker="o" si vedono i punti
plt.title("I quadrati")
plt.xlabel("numero")
plt.ylabel("quadrato")
plt.grid(True)
plt.show()                               # mostra la finestra
```
- `plt.plot(x, y)` ha bisogno di due sequenze della stessa lunghezza.
- `plt.scatter(x, y)` disegna solo i punti, `plt.bar(etichette, valori)` le barre, `plt.hist(valori, bins=...)` un istogramma.
- Stile: `color="tab:red"`, `linestyle="--"`, `marker="o"`. Più linee nello stesso grafico: più chiamate a `plt.plot`, ciascuna con
  `label="..."`, poi `plt.legend()`.
- `plt.savefig("grafico.png", dpi=150)` salva il grafico in un'immagine (prima di `plt.show()`).

### numpy: quanto basta
Per disegnare una funzione servono tanti valori di `x`. `numpy` li crea e calcola la funzione su tutti insieme, senza ciclo `for`.
```python
import numpy as np

x = np.linspace(-1, 5, 200)              # 200 numeri equidistanti da -1 a 5
y = x ** 2 - 4 * x + 3                   # calcolato per tutti i valori
plt.plot(x, y)
```
Le funzioni matematiche sono quelle di `numpy` (`np.sin`, `np.cos`, `np.exp`, `np.sqrt`, `np.pi`…): quelle del modulo `math`
funzionano solo su un numero alla volta.

### Dai dati al grafico
Si leggono i dati dal file (lezione 3), si costruiscono le liste di valori, si disegna.
```python
massa = [float(riga["massa"]) for riga in righe]
plt.scatter(numeri_atomici, massa)
```

### Più grafici in una finestra
```python
figura, (sinistra, destra) = plt.subplots(1, 2, figsize=(12, 4.5))
sinistra.plot(x, y)                      # con "assi" si usano set_title, set_xlabel, set_ylabel
destra.bar(etichette, valori)
figura.tight_layout()
plt.show()
```

## Esercizi

Salvate ogni esercizio in un file diverso. Le soluzioni sono in `soluzioni/`: provate prima da soli. I dati sono in
`../lezione3/dati/`.

1. **Una funzione.** Disegnate y = x³ − 3x per x tra −3 e 3, con titolo, etichette degli assi e griglia.
   *Prova: la curva passa per l'origine e ha un massimo in x = −1 e un minimo in x = 1.*
2. **Retta e parabola.** Disegnate nello stesso grafico y = x² e y = x + 2 per x tra −2 e 3, con legenda, e segnate i due
   punti d'incontro. *Prova: intersezioni in (−1, 1) e (2, 4).*
3. **Masse atomiche.** Da `elementi.csv` fate un grafico a barre della massa dei primi dieci elementi, con i simboli sull'asse x.
   *Prova: la barra più alta è il neon (20.18).*
4. **Temperature.** Da `temperature_mensili.csv` disegnate la temperatura media di ogni mese (media tra minima e massima).
   *Prova: il mese più caldo è luglio, 24.5 °C.*
5. **Voti.** Da `voti_classe.csv` disegnate un box plot dei voti, uno per materia.
   *Prova: mediane matematica 6.75, fisica 6.5, chimica 7.25.*
6. **Bonus – Decadimento.** Prendete `esempi/07_decadimento.py` e disegnate tre curve con tempi di dimezzamento 2, 5 e 10 giorni.
   *Prova: dopo 10 giorni restano 3.1 g, 25 g e 50 g.*
7. **Bonus – Tre dadi.** Simulate 10000 lanci di tre dadi e disegnate la distribuzione della somma.
   *Prova: le somme più frequenti sono 10 e 11.*

## Mini-progetto (a casa)

Scegliete un argomento che vi interessa e producete **un grafico completo** (titolo, etichette, legenda se serve), salvato in un
file `.png`. Due strade:
- **Dati vostri:** costruite un piccolo file CSV (per esempio con Excel, salvando come «CSV») e disegnatelo con quello che avete
  imparato nelle lezioni 3 e 4.
- **Una variazione degli esempi `06`, `07` o `08`:** cambiate i parametri, aggiungete una curva, un confronto, un secondo grafico.

## Per approfondire
- La galleria ufficiale di matplotlib (<https://matplotlib.org/stable/gallery/index.html>) mostra ogni tipo di grafico con il codice.
- In [`../avanzato/`](../avanzato/README.md): `parabola.py` e `statistica_dati.py` (grafici più elaborati, anche interattivi) e tre esempi con
  **SymPy**, il calcolo simbolico (equazioni, derivate, integrali, limiti, bilanciamento di una reazione).
- Altri ambienti per lavorare con Python: Jupyter, Google Colab e VS Code, descritti nel [pre-corso](../pre-corso/README.md) e in
  [strumenti e librerie](../risorse/strumenti_e_librerie.md).
