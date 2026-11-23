# Lezione 3 – Dati: dizionari e file

**Obiettivi:** organizzare i dati con i dizionari, leggere e scrivere file di testo e CSV, riusare il proprio codice con i moduli,
installare una libreria con `pip`.

**Esempi** (cartella `esempi/`): `01_dizionari` · `02_frequenze` · `03_file_di_testo` · `04_csv_elementi` ·
`05_csv_temperature` · `06_voti_excel` · `07_usare_un_modulo` (con `miei_strumenti.py`) · `verifica_librerie`

**Dati** (cartella `dati/`): `elementi.csv` (i primi 36 elementi, con masse arrotondate), `temperature_mensili.csv`
(dodici mesi, **dati di esempio** non misurati) e `voti_classe.csv` (voti **inventati** di una classe, nel formato che usa Excel in italiano).

I programmi cercano i file dei dati partendo dalla posizione del programma stesso: funzionano da qualunque cartella li si lanci, purché
le cartelle `esempi/` e `dati/` restino dove sono.

## Riepilogo

### Dizionari
Un **dizionario** associa a ogni **chiave** un **valore**. Si cerca per chiave, non per posizione.
```python
masse = {"H": 1.008, "C": 12.011, "O": 15.999}
masse["O"]                     # 15.999
masse["Na"] = 22.990           # aggiunge (o cambia) una coppia
"C" in masse                   # True: controlla le chiavi
masse.get("Fe", "assente")     # nessun errore se la chiave manca
for simbolo, massa in masse.items():
    print(simbolo, massa)
```
- Le chiavi sono uniche: assegnare a una chiave esistente ne cambia il valore.
- Un dizionario può contenere liste o altri dizionari.
- Per contare: `conteggi[x] = conteggi.get(x, 0) + 1` (esempio `02_frequenze`).

### Testo: qualche metodo utile
`"a b c".split()` → `['a', 'b', 'c']` · `" ciao\n".strip()` → `'ciao'` · `", ".join(lista)` · `testo.lower()` · `testo.replace(",", ".")`.

### File di testo
```python
with open("appunti.txt", "w", encoding="utf-8") as f:    # "w" scrive, "a" aggiunge, "r" legge
    f.write("Prima riga\n")

with open("appunti.txt", encoding="utf-8") as f:
    for riga in f:
        print(riga.strip())
```
- `with` chiude il file da solo alla fine del blocco.
- `encoding="utf-8"` evita problemi con le lettere accentate su Windows.
- Il nome del file si può scrivere con `Path` (modulo `pathlib`): `Path(__file__).parent / "dati" / "file.csv"` indica un file
  nella cartella accanto al programma, senza dipendere dalla cartella da cui lo si lancia.

### File CSV
Un file **CSV** è una tabella in forma di testo: una riga per record, i campi separati da un carattere (di solito `,`).
```python
import csv

with open("elementi.csv", encoding="utf-8", newline="") as f:
    for riga in csv.DictReader(f):          # ogni riga è un dizionario
        print(riga["simbolo"], float(riga["massa"]))
```
- Nel file tutto è **testo**: i numeri vanno convertiti con `int()` o `float()`.
- Excel in italiano salva con il **punto e virgola** come separatore e la **virgola** come decimale:
  `csv.DictReader(f, delimiter=";")` e `float(testo.replace(",", "."))` (esempio `06_voti_excel`).
- Per scrivere: `csv.writer(f)` e `scrittore.writerow([...])` (esempio `05_csv_temperature`).

### Moduli e `import`
Un modulo è un file `.py` con funzioni da riusare. Il file `miei_strumenti.py` si importa con `import miei_strumenti` e si usa
con `miei_strumenti.media(...)`; con `from miei_strumenti import e_primo` si importa una funzione sola.
I moduli della libreria standard (`math`, `csv`, `statistics`, `pathlib`…) si importano allo stesso modo.

### Installare una libreria con `pip`
Le librerie che non fanno parte della libreria standard si installano da PyPI. Nella finestra dei comandi di Windows (`cmd`):
```
py -m pip install matplotlib
py -m pip list
```
In alternativa, da Thonny: **Strumenti → Gestisci pacchetti…**. Va installata per **lo stesso Python** che Thonny usa
(vedi la [guida a Thonny](../risorse/guida_thonny.md)). Il programma `esempi/verifica_librerie.py` controlla se `numpy` e
`matplotlib`, che servono nella lezione 4, sono installati e come installarli. Se `pip` risponde «No matching distribution found», la
libreria non è ancora pronta per Python 3.15 (vedi [strumenti e librerie](../risorse/strumenti_e_librerie.md)).

## Esercizi

Salvate ogni esercizio in un file diverso. Le soluzioni sono in `soluzioni/`: provate a risolvere gli esercizi prima di guardarle.
I dati si trovano in `dati/`; nelle soluzioni la lettura dei file è scritta come negli esempi.

1. **Cerca un elemento.** Leggete `elementi.csv` e chiedete un simbolo: stampate nome, numero atomico e massa; se il simbolo
   non esiste, scrivete «Elemento non trovato». *Prova: Fe → Ferro, numero atomico 26, massa 55.845.*
2. **Massa molare.** Scrivete `massa_molare(formula)`, dove `formula` è un dizionario come `{"H": 2, "O": 1}`.
   *Prova: acqua 18.015 g/mol; CO₂ 44.009; NaCl 58.440.*
3. **Conta le parole.** Chiedete una frase e stampate quante volte compare ogni parola, senza distinguere maiuscole e minuscole.
   *Prova: «La la casa» → la 2, casa 1.*
4. **Temperature.** Da `temperature_mensili.csv` trovate il mese con la minore escursione termica (massima − minima) e i mesi in cui
   la massima supera la media delle massime. *Prova: Dicembre (6 °C); 6 mesi, da Maggio a Ottobre.*
5. **Voti.** Da `voti_classe.csv` calcolate la media di ogni materia e i nomi degli studenti con almeno un voto sotto 6.
   *Prova: matematica 6.96, fisica 6.88, chimica 7.17; 5 studenti (Bruno, Davide, Fabio, Luca, Nicola).*
6. **Riepilogo su file.** Scrivete `riepilogo_voti.csv` con due colonne, studente e media dei tre voti (2 decimali).
   *Prova: 12 righe di dati; Alice → 7.17.*
7. **Bonus – Gruppi.** Costruite un dizionario che associa a ogni gruppo della tavola periodica la lista dei simboli.
   *Prova: gruppo 18 → `['He', 'Ne', 'Ar', 'Kr']`.*
8. **Bonus – Voto valido.** Scrivete `leggi_voto()`, che chiede un voto e ripete la domanda finché non è un numero tra 0 e 10.
   *Prova: «abc» → nuova domanda; 11 → nuova domanda; 7,5 → 7.5.*

## Per approfondire
- Nei programmi di questa lezione trovate `try` ed `except`: servono a gestire gli errori senza far fermare il programma.
  Una spiegazione con esempi è in [`../avanzato/gestione_errori.py`](../avanzato/gestione_errori.py).
- I grafici con `matplotlib` sono l'argomento della lezione 4; esempi più impegnativi in [`../avanzato/`](../avanzato/README.md).
- Documentazione ufficiale (in italiano): [dizionari](https://docs.python.org/it/3/tutorial/datastructures.html#dictionaries),
  [file](https://docs.python.org/it/3/tutorial/inputoutput.html#reading-and-writing-files), [modulo `csv`](https://docs.python.org/it/3/library/csv.html).
