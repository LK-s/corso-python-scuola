# Lezione 1 – Primi passi

**Obiettivi:** usare Thonny, eseguire calcoli, memorizzare valori in variabili, leggere dati dall'utente,
stampare risultati formattati e leggere i messaggi di errore.

**Esempi** (cartella `esempi/`): `01_operatori` · `02_variabili` · `03_cerchio` · `04_input_e_stringhe` ·
`05_stringhe` · `06_conversioni` · `07_ipotenusa` · `08_frazioni` · `09_soluzione` · `10_errori_comuni`

Gli esempi `03`, `07` e `09` sono piccoli problemi organizzati in blocchi (dati, calcoli, risultati): lo schema
con cui si scrivono i programmi veri. Valori di prova per `07` e `09` sono indicati nei commenti iniziali dei file.

## Riepilogo

### Shell e script
- La **Shell** (in basso in Thonny) esegue un'istruzione per volta: ideale per provare.
- Uno **script** è un file `.py` con più istruzioni, eseguite dall'alto verso il basso.
- Nella Shell il risultato di un'espressione si vede subito; in uno script serve `print(...)`.
- Per eseguire uno script: pulsante verde ▶ oppure **F5** (menu *Esegui → Esegui lo script corrente*, *Run → Run current script*).
- Se il programma sembra bloccato (per esempio sta aspettando un valore da `input()`, oppure è in un ciclo infinito)
  si ferma con il pulsante rosso **Ferma** (*Stop*, **Ctrl+F2**). Quando chiede un valore, guardare nella Shell:
  è lì che bisogna scrivere.

### Commenti e rientri
- Tutto ciò che segue il simbolo **`#`** fino a fine riga è un **commento**: Python lo ignora. Serve a spiegare il codice
  a chi lo legge (voi stessi tra un mese compresi).
- I **rientri** (spazi all'inizio della riga) in Python hanno un significato: per ora le righe di un programma
  iniziano tutte dal margine sinistro. Una riga rientrata senza motivo dà `IndentationError`.
  I rientri servono dalla lezione 2.

### Operatori numerici

| Operazione | Simbolo | Esempio | Risultato |
| --- | --- | --- | --- |
| Somma, differenza | `+` `-` | `7 + 2` | `9` |
| Prodotto | `*` | `7 * 2` | `14` |
| Divisione | `/` | `7 / 2` | `3.5` |
| Quoziente intero | `//` | `7 // 2` | `3` |
| Resto | `%` | `7 % 2` | `1` |
| Potenza | `**` | `7 ** 2` | `49` |

Precedenza come in matematica; le parentesi tonde servono per cambiare l'ordine.
Per i decimali si usa il **punto**: `3.14`, non `3,14`.

### Tipi di dato principali

| Tipo | Significato | Esempio |
| --- | --- | --- |
| `int` | numero intero | `42` |
| `float` | numero decimale | `3.14` |
| `str` | testo | `"ciao"` |
| `bool` | vero/falso | `True`, `False` |

### Variabili
- `nome = valore` **assegna**: a sinistra il nome, a destra il valore.
- Nomi: lettere, cifre e `_`; non iniziano con una cifra; maiuscole e minuscole sono diverse.
- Scegliere nomi che spiegano: `raggio`, `massa_g`, non `x1`.

### Input e output
```python
nome = input("Come ti chiami? ")          # restituisce sempre testo
eta = int(input("Età: "))                 # int(...) converte in intero
peso = float(input("Peso (kg): "))        # float(...) converte in decimale
print(f"{nome}, {eta} anni, {peso:.1f} kg")   # f-string con 1 decimale
```

### Il modulo `math`
```python
import math
math.pi   math.sqrt(x)   math.sin(x)   math.log10(x)   math.floor(x)   math.ceil(x)
```
Le funzioni trigonometriche lavorano in **radianti**.

### Addendum: perché `0.1 + 0.2` non fa `0.3`
`0.1 + 0.2` dà `0.30000000000000004` e `0.1 + 0.2 == 0.3` è `False`. **Non è un limite di Python**: il risultato è
lo stesso in quasi tutti i linguaggi (C, Java, JavaScript, Fortran…), perché dipende da come i computer memorizzano i
numeri decimali (standard IEEE 754, in base 2): come 1/3 in base 10 ha infinite cifre, `0.1` ha infinite cifre in base 2
e va troncato. L'errore è minuscolo (dell'ordine di 10⁻¹⁶), ma per questo non si confrontano due `float` con `==`:
si arrotonda con `round()` o si controlla che la differenza sia piccola (lo faremo nella lezione 2).
Una raccolta del risultato in decine di linguaggi: <https://0.30000000000000004.com/>.

Quando servono risultati esatti o più cifre, ci sono strumenti dedicati:
- `fractions` (sotto): frazioni esatte; `decimal`: decimali in base 10, con la precisione scelta (per esempio per i calcoli con il denaro);
- `mpmath`: calcoli con migliaia di cifre (da installare, vedi [strumenti e librerie](../risorse/strumenti_e_librerie.md)).

### Numeri esatti: il modulo `fractions`
```python
from fractions import Fraction
Fraction(1, 3) + Fraction(1, 6)          # 1/2, esatto (con i float 0.1 + 0.2 != 0.3)
Fraction(math.pi).limit_denominator(1000)  # 355/113
```
Un `Fraction` è un numero che porta con sé numeratore e denominatore (`.numerator`, `.denominator`).
Anche un `float` ha le sue funzioni: `3.0.is_integer()` è `True`. Il punto dopo il nome richiama le funzioni
di quell'oggetto, come per le stringhe (`"testo".upper()`).

### Moduli, librerie e versioni di Python
`math` fa parte della **libreria standard**: è già dentro Python e basta `import math`.
Le altre librerie (NumPy, matplotlib, SymPy…) vanno prima installate con `pip` e le useremo nelle ultime lezioni.
Poiché le librerie vengono aggiornate dopo ogni nuova versione di Python, una libreria può non essere ancora
pronta per la 3.15: in quel caso si usa una versione precedente (per esempio la 3.14), che si affianca alla 3.15
con `py install 3.14`. Indicazioni e prove di compatibilità in [`../risorse/strumenti_e_librerie.md`](../risorse/strumenti_e_librerie.md).

### Farsi aiutare da Thonny
Non serve ricordare a memoria tutti i nomi: Thonny aiuta a scoprire cosa si può scrivere e come si usa.

| Cosa si vuole | Come |
| --- | --- |
| **Vedere cosa si può scrivere**, per esempio dopo `math.` o dopo `"testo".` | Premere **Ctrl+Spazio** (menu *Modifica → Auto-completamento*, *Edit → Auto-complete*): compare l'elenco dei nomi possibili, con la documentazione accanto. Scegliere con le frecce e **Invio**. Nella Shell basta il tasto **Tab** |
| **Vedere i parametri** di una funzione, per esempio di `round(` | Dopo la parentesi aperta premere **Ctrl+Maiusc+Spazio** (*Modifica → Mostra info sui parametri*) |
| **Leggere la spiegazione** di un comando | Nella Shell: `help(round)`, `help(math.sqrt)`, `help(str)`. Con `dir(str)` si elencano tutti i metodi delle stringhe |
| **Vedere il codice** di una funzione | **Ctrl+clic** sul nome nell'editor: si apre il punto in cui è definita. Funziona bene con le funzioni scritte in Python, comprese le nostre; per quelle scritte in C (come `math.sqrt`) il codice Python non esiste |

Per **vedere il valore delle variabili** mentre il programma gira: menu *Visualizza → Variabili* (*View → Variables*).
Compare un pannello con i nomi e i valori di tutto ciò che il programma ha definito. Altri consigli su Thonny
(caratteri più grandi, debug, scorciatoie) sono nella [guida a Thonny](../risorse/guida_thonny.md).

Per avere i suggerimenti **senza premere nulla** mentre si scrive: **Strumenti → Opzioni → Editor** (*Tools → Options → Editor*)
e spuntare *Proponi automaticamente suggerimenti durante la digitazione* e
*Mostra automaticamente le info del parametro dopo aver digitato '('*. Per chi inizia è un aiuto prezioso.
(Verificato su Thonny 5.0.0.)

### Messaggi di errore
Leggere sempre l'**ultima riga**: dice il tipo di errore e la riga del programma.

| Errore | Significato tipico |
| --- | --- |
| `SyntaxError` | scritto male: virgolette o parentesi mancanti, `:` dimenticato |
| `IndentationError` | riga rientrata (o non rientrata) quando non dovrebbe |
| `NameError` | nome non definito: errore di battitura o variabile non ancora creata |
| `TypeError` | operazione tra tipi incompatibili (`"età: " + 15`) |
| `ValueError` | valore non convertibile (`int("ciao")`). Capita spesso scrivendo `3,5` invece di `3.5` quando il programma chiede un `float`: i decimali vogliono il **punto** |
| `ZeroDivisionError` | divisione per zero |

## Esercizi

Salvate ogni esercizio in un file diverso (`es1.py`, `es2.py`, …). Le soluzioni sono in `soluzioni/`: provate a risolvere gli esercizi prima di guardarle.

1. **Sfera.** Chiedete il raggio e stampate volume (4/3 π r³) e superficie (4 π r²) con 3 decimali.
   *Prova: raggio 2 → volume 33.510, superficie 50.265.*
2. **Temperature.** Chiedete una temperatura in °F e stampate il valore in °C e in K.
   *Prova: 98.6 °F → 37.00 °C, 310.15 K.*
3. **Media di tre voti.** Chiedete tre voti e stampate la media con 2 decimali e arrotondata all'intero.
   *Prova: 6, 7.5, 8 → 7.17 e 7.*
4. **Divisione con resto.** Chiedete due numeri interi, dividendo e divisore. Calcolate quoziente e resto
   (con `//` e `%`) e stampate una riga che mostra che il conto torna: dividendo = divisore * quoziente + resto.
   *Prova: dividendo 47 e divisore 5 → stampa `47 = 5 * 9 + 2`.*
5. **Interesse composto.** Capitale, tasso annuo in % e anni: stampate montante C·(1+r)ⁿ e interessi.
   *Prova: 1000 €, 3 %, 10 anni → 1343.92 €.*
6. **Densità.** Massa in grammi e tre lati in cm di un parallelepipedo: stampate volume e densità
   in g/cm³ e in kg/m³. *Prova: 540 g, 2×3×10 cm → 9.000 g/cm³.*

**Per chi ha finito:** cambiate l'esercizio 5 in modo che mostri il montante per ognuno degli anni
(lo faremo con un ciclo nella lezione 2).

## Compiti per la lezione 2 (facoltativi)
- Terminare gli esercizi non finiti.
- Provare nella Shell: `7 / 2`, `7 // 2`, `-7 // 2`, `-7 % 2`, `2 ** 0.5`, `10 ** -2`.
- Scrivere un programma che converte ore, minuti e secondi in secondi totali.

## Per approfondire
- `help(print)` nella Shell mostra la documentazione di una funzione (vedi «Farsi aiutare da Thonny»).
- Tutorial ufficiale (in italiano): <https://docs.python.org/it/3/tutorial/>
- *Think Python* (libro gratuito, in inglese): <https://allendowney.github.io/ThinkPython/>
