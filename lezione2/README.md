# Lezione 2 – Decisioni, ripetizioni, funzioni

**Obiettivi:** far scegliere al programma (`if`), ripetere azioni (`for`, `while`), gestire
sequenze di dati (liste), organizzare il codice in funzioni.

**Esempi** (cartella `esempi/`): `01_booleani_confronti` · `02_if_elif_else` ·
`03_equazione_secondo_grado` · `04_for_range` · `05_liste` · `06_while` · `07_funzioni` · `08_numeri_primi`

## Riepilogo

### Confronti e logica
`==` uguale · `!=` diverso · `<` `<=` `>` `>=` · `and` `or` `not`.
**Attenzione:** `=` assegna, `==` confronta. Si può scrivere `0 < x < 10`.

### Indentazione
In Python i blocchi di codice si riconoscono dai **rientri** (4 spazi; Thonny li inserisce con il tasto Tab).
Dopo `if`, `elif`, `else`, `for`, `while`, `def` c'è sempre il simbolo `:` e il blocco rientrato.

```python
if ph < 7:
    print("acida")
elif ph == 7:
    print("neutra")
else:
    print("basica")
```

### Cicli
```python
for i in range(5):            # 0, 1, 2, 3, 4
    print(i)

for n in range(1, 11):        # 1 ... 10 (il 11 è escluso)
    print(n ** 2)

while condizione:             # si ripete finché la condizione è vera
    ...
```
- `range(inizio, fine, passo)`: la fine è **esclusa**.
- `break` esce dal ciclo, `continue` passa al giro successivo.
- Per accumulare una somma c'è anche la funzione pronta `sum()`: `sum(range(1, 101))` dà `5050`, come il ciclo con `somma += n`
  (esempio `04_for_range`).
- `print(x, end=" ")` stampa senza andare a capo (la riga successiva continua di seguito); un `print()` vuoto va a capo. Si usa in `08_numeri_primi`.
- Un `while` la cui condizione non diventa mai falsa è un **ciclo infinito**: si ferma con il pulsante Stop.

### Liste
```python
misure = [12.1, 11.8, 12.4]
misure[0]            # primo elemento (indici da 0)
misure[-1]           # ultimo
misure.append(12.0)  # aggiunge
len(misure)  sum(misure)  min(misure)  max(misure)  sorted(misure)
for m in misure:
    print(m)
```
Per costruire una lista da un'altra c'è una forma compatta, la *list comprehension*: `[n ** 2 for n in range(1, 11)]`
dà la lista dei quadrati da 1 a 100. Lo stesso risultato si ottiene con `list(map(lambda n: n ** 2, range(1, 11)))`, una forma più
avanzata (esempio `05_liste`): per ora basta saper leggere la prima.
Si può aggiungere una condizione: `[n for n in range(1, 101) if e_primo(n)]` tiene solo i primi, e gli elementi possono
essere coppie: `[(p, p + 2) for p in primi if e_primo(p + 2)]` dà i primi gemelli (esempio `08_numeri_primi`).

### Funzioni
```python
import math

def area_cerchio(raggio):
    return math.pi * raggio ** 2

a = area_cerchio(2)
```
- `def nome(parametri):` definisce, `return` restituisce un valore.
- Le variabili create dentro una funzione sono **locali**.
- Una funzione si definisce una volta e si usa quante volte si vuole.
- **Annotazioni di tipo** (facoltative): `def area(base: float, altezza: float) -> float:` dichiara i tipi dei parametri e del risultato.
  Python le ignora durante l'esecuzione, ma un controllore come `mypy` (`py -m pip install mypy`, poi `!mypy file.py` nella Shell di Thonny)
  scopre prima di eseguire gli errori di tipo, per esempio un testo passato dove serve un numero. Esempi in `07_funzioni`.
  Va installato per lo stesso interprete usato da Thonny (vedi la [guida a Thonny](../risorse/guida_thonny.md)).

### Debug passo-passo in Thonny
Pulsante **Debug** (icona con l'insetto, Ctrl+F5) e poi **Step over** (F6) / **Step into** (F7):
si vede il programma avanzare una riga alla volta e il valore delle variabili (menu *Visualizza → Variabili*).

### Controllare il codice con il linter (facoltativo)
Se avete installato Ruff (vedi la [guida a Thonny](../risorse/guida_thonny.md)), provate a lanciarlo sugli esempi:
`!ruff check 01_booleani_confronti.py`. Segnala dei **suggerimenti di stile**: per esempio `0 < x and x < 10` si può scrivere
`0 < x < 10`, e `not x == 5` si può scrivere `x != 5`. Sono consigli, non errori: i programmi funzionano comunque.
Ruff può anche correggere da solo con `--fix` (modifiche sicure) e `--fix --unsafe-fixes` (modifiche che potrebbero
cambiare il comportamento del programma). **Attenzione: `--fix` riscrive il file**; provatelo su una copia e confrontate
il risultato con l'originale.

## Esercizi

1. **Pari e multiplo di 3.** Chiedete un intero e dite se è pari o dispari e se è multiplo di 3.
   *Prova:* 18 → pari e multiplo di 3; 7 → dispari e non multiplo di 3.
2. **Giudizio.** Da voto (0–10) a giudizio: ≥9 Ottimo, ≥8 Distinto, ≥7 Buono, ≥6 Sufficiente,
   ≥5 Mediocre, altrimenti Insufficiente; segnalate i voti non validi.
   *Prova:* 9.5 → Ottimo; 6 → Sufficiente; 4 → Insufficiente; 11 → voto non valido.
3. **Equazione di 2° grado come funzione.** Scrivete `risolvi(a, b, c)` che restituisce la lista delle
   soluzioni reali (anche per `a = 0`). *Prova:* `risolvi(1, -5, 6)` → `[2.0, 3.0]`.
4. **Potenze e dispari.** Stampate le potenze di 2 da 2⁰ a 2¹⁰. Verificate che la somma dei primi
   n numeri dispari sia n² per n da 1 a 10. *Prova:* per n = 10 la somma è 100.
5. **Statistiche.** Data una lista di misure, calcolate media, minimo, massimo, escursione e
   quante misure superano la media. *Prova:* 12.1, 11.8, 12.4, 12.0, 11.9, 12.6, 12.2 → media 12.143,
   minimo 11.8, massimo 12.6, escursione 0.8, 3 misure sopra la media.
6. **Fattori primi.** Scrivete `fattori_primi(n)`. *Prova:* 360 → `[2, 2, 2, 3, 3, 5]`.
7. **Bonus – Indovina il numero.** Il computer sceglie un numero tra 1 e 100 (`import random`,
   `random.randint(1, 100)`); voi provate e il programma risponde «troppo alto/basso».
8. **Bonus – Tabella.** Stampate una tabella °C → °F da −10 a 40 con passo 10. *Prova:* −10 °C → 14.0 °F; 40 °C → 104.0 °F.
