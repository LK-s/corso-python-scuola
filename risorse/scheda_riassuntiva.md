# Scheda riassuntiva (lezioni 1 e 2)

Da stampare (fronte e retro) e tenere accanto alla tastiera. Gli esempi sono stati provati con Python 3.15.

## Numeri e operatori

| Operazione | Simbolo | Esempio | Risultato |
| --- | --- | --- | --- |
| Somma, differenza | `+` `-` | `7 + 2` | `9` |
| Prodotto | `*` | `7 * 2` | `14` |
| Divisione | `/` | `7 / 2` | `3.5` |
| Quoziente intero | `//` | `7 // 2` | `3` |
| Resto | `%` | `7 % 2` | `1` |
| Potenza | `**` | `7 ** 2` | `49` |

Decimali con il **punto** (`3.14`). `-7 // 2` dà `-4` e `-7 % 2` dà `1` (il quoziente è arrotondato per difetto).
I decimali sono approssimati in **tutti** i linguaggi: `0.1 + 0.2` dà `0.30000000000000004`, quindi non si confrontano con `==`
(per risultati esatti: `fractions`, `decimal`).

## Tipi e conversioni

| Tipo | Esempio | Conversione | Tipo restituito da `type(...)` |
| --- | --- | --- | --- |
| intero | `42` | `int("42")` | `int` |
| decimale | `3.14` | `float("3.5")` | `float` |
| testo | `"ciao"` | `str(7)` | `str` |
| vero/falso | `True`, `False` | | `bool` |

`input()` restituisce **sempre testo**: `eta = int(input("Età: "))`, `peso = float(input("Peso: "))`.

## Variabili e commenti

```python
raggio = 2.5          # assegna: a sinistra il nome, a destra il valore
contatore += 1        # forma abbreviata di contatore = contatore + 1
# una riga che inizia con # è un commento
```
Nomi: lettere, cifre e `_`; non iniziano con una cifra; maiuscole e minuscole sono diverse.

## Stampare

```python
print("Raggio:", raggio)
print(f"Area: {area:.2f} cm²")       # f-string
print(x, end=" ")                 # non va a capo: la stampa successiva continua sulla stessa riga
```

| Formato | Significato | Esempio con `3.14159` |
| --- | --- | --- |
| `{x:.2f}` | 2 decimali | `3.14` |
| `{x:8.3f}` | 3 decimali, larghezza 8 | `   3.142` |
| `{n:5d}` | intero, larghezza 5 | `   42` |
| `{x:.0f}` | nessun decimale | `3` |

## Funzioni già pronte

| Funzione | Cosa fa | Esempio |
| --- | --- | --- |
| `abs(x)` | valore assoluto | `abs(-4)` → `4` |
| `round(x, n)` | arrotonda a `n` decimali | `round(3.14159, 2)` → `3.14` |
| `len(s)` | lunghezza | `len("Chimica")` → `7` |
| `sum(l)` `min(l)` `max(l)` | somma, minimo, massimo di una lista | `sum([1, 2, 3])` → `6` |
| `sorted(l)` | lista ordinata | `sorted([3, 1, 2])` → `[1, 2, 3]` |
| `type(x)` | tipo di un valore | `type(3.5)` → `float` |
| `help(nome)` | documentazione (nella Shell) | `help(round)` |

Attenzione: `round(2.5)` dà `2` e `round(3.5)` dà `4` (con un valore esattamente a metà Python sceglie il numero pari).

## Il modulo `math`

```python
import math
math.pi   math.sqrt(x)   math.sin(x)   math.cos(x)   math.log10(x)   math.floor(x)   math.ceil(x)   math.hypot(a, b)
```
Le funzioni trigonometriche lavorano in **radianti**.

## Frazioni esatte

```python
from fractions import Fraction
Fraction(1, 3) + Fraction(1, 6)             # 1/2
Fraction(math.pi).limit_denominator(1000)   # 355/113
```

## Testo

```python
s = "Chimica"
len(s)  s[0]  s[-1]  s[0:4]  s.upper()  s.lower()  s.replace("i", "I")  s.count("i")   # s[0:4] = "Chim" (il 4 è escluso)
"ab" + "cd"    # "abcd"      "ab" * 3    # "ababab"
```

## Confronti e logica

`==` uguale · `!=` diverso · `<` `<=` `>` `>=` · `and` `or` `not` · `0 < x < 10`.
**`=` assegna, `==` confronta.**

## Decisioni

```python
if ph < 7:
    print("acida")
elif ph == 7:
    print("neutra")
else:
    print("basica")
```
Dopo `if`, `elif`, `else`, `for`, `while`, `def` c'è sempre `:` e il blocco **rientrato** (4 spazi).

## Cicli

```python
for i in range(5):           # 0, 1, 2, 3, 4
    print(i)
for n in range(1, 11):       # da 1 a 10 (l'11 è escluso)
    print(n ** 2)
while condizione:            # ripete finché la condizione è vera
    ...
```
`range(inizio, fine, passo)`: la fine è **esclusa**. `break` esce dal ciclo, `continue` passa al giro successivo.
Per sommare c'è anche `sum(range(1, 101))` (dà `5050`).

## Liste

```python
misure = [12.1, 11.8, 12.4]
misure[0]            # primo (gli indici partono da 0)
misure[-1]           # ultimo
misure.append(12.0)  # aggiunge in fondo
for m in misure:
    print(m)
quadrati = [n ** 2 for n in range(1, 11)]   # lista costruita da un'altra (list comprehension)
```

## Funzioni

```python
def area_cerchio(raggio):
    return math.pi * raggio ** 2

a = area_cerchio(2)
```
Le variabili create dentro una funzione sono **locali**.

Annotazioni di tipo (facoltative): `def area(base: float, altezza: float) -> float:`. Python le ignora quando esegue il programma;
un controllore come `mypy` le usa per trovare errori di tipo prima di eseguirlo.

## Errori frequenti

| Errore | Causa tipica |
| --- | --- |
| `SyntaxError` | virgolette o parentesi mancanti, `:` dimenticato |
| `IndentationError` | rientri sbagliati |
| `NameError` | nome scritto male o non ancora definito |
| `TypeError` | operazione tra tipi diversi (`"età: " + 15`) |
| `ValueError` | valore non convertibile (`int("ciao")`; `3,5` invece di `3.5`) |
| `ZeroDivisionError` | divisione per zero |

Si legge sempre l'**ultima riga** del messaggio.

## Thonny

| Azione | Scorciatoia |
| --- | --- |
| Esegui | **F5** |
| Ferma | **Ctrl+F2** |
| Suggerimenti mentre si scrive | **Ctrl+Spazio** (Shell: Tab) |
| Info sui parametri | **Ctrl+Maiusc+Spazio** |
| Debug passo-passo | **Ctrl+F5**, poi **F6** / **F7** |
| Commenta righe selezionate | **Ctrl+3** |
| Controllo del codice con il linter (facoltativo) | nella Shell: `!ruff check nomefile.py` |

Più dettagli nella [guida a Thonny](guida_thonny.md).
