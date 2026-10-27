# Python per la scuola – Guida pre-corso

Prima del corso servono circa 30 minuti: installare Python 3.15 e Thonny su Windows (sezione «Installazione») e provare il primo programma. Il resto della guida è lettura facoltativa: storia, curiosità e qualche consiglio, per arrivare alla prima lezione con un'idea di cosa stiamo per usare. Chi ha già programmato in altri linguaggi (Fortran, Pascal, C…) trova una sezione dedicata alle differenze; chi parte da zero può saltarla senza problemi.

## Installazione su Windows

Servono due programmi: **Python** (l'interprete, cioè il programma che esegue il codice) e **Thonny** (l'editor in cui scriveremo ed eseguiremo i programmi). Sono gratuiti e funzionano su Windows 10 e 11. Python si installa con il Python install manager, lo strumento ufficiale di python.org per Windows, che permette anche di aggiungere o aggiornare versioni in seguito.

### Passo 1 – Installare Python 3.15

1. Aprire [python.org/downloads/latest/pymanager](https://www.python.org/downloads/latest/pymanager/) e premere il pulsante **Microsoft Store**, la scelta consigliata dalla pagina. Nell'app Store premere **Ottieni** (o **Installa**).
2. Aprire il menu Start, scrivere `cmd` e premere Invio. Nella finestra nera digitare `py install 3.15` e premere Invio. Se compare una richiesta di conferma o di verifica della configurazione, rispondere sì e attendere la fine del download.

Se sul computer c'è già il vecchio «Python Launcher» (installato con il programma di installazione tradizionale), disinstallarlo prima da Impostazioni → App: usa lo stesso comando `py` dell'install manager. Se il Microsoft Store è bloccato (può succedere sui computer della scuola), dalla stessa pagina si scarica il pacchetto **MSIX**, che si apre con doppio clic, oppure in `cmd` si digita `winget install 9NQ7512CXL7T`. L'install manager si aggiorna da solo. Le schermate possono differire leggermente dalla descrizione.

Verifica: nella finestra nera digitare:

```
py --version
```

Deve comparire `Python 3.15.0`. Se compare un errore, vedere la sezione «Se qualcosa non funziona».

### Passo 2 – Installare Thonny

1. Aprire [thonny.org](https://thonny.org) e scaricare la versione per Windows.
2. Eseguire l'installer lasciando le opzioni predefinite.

Thonny contiene una propria copia di Python (una versione precedente alla 3.15). Per usare la 3.15 appena installata serve il passo successivo.

### Passo 3 – Dire a Thonny di usare Python 3.15

1. Nella finestra nera (`cmd`) digitare e copiare il percorso che compare:

```
py -c "import sys; print(sys.executable)"
```

Con l'install manager è simile a `C:\Users\NOME\AppData\Local\Python\pythoncore-3.15-64\python.exe`. Copiarlo, poi in Thonny:

1. Aprire il menu **Strumenti → Opzioni** (in inglese *Tools → Options*) e la scheda **Interprete**.
2. Scegliere **Interprete alternativo Python 3 o ambiente virtuale** (*Alternative Python 3 interpreter or virtual environment*).
3. Incollare il percorso nel campo sotto (o usare il pulsante per cercare il file) e premere **OK**.
4. Chiudere e riaprire Thonny.

Per cambiare la lingua dell'interfaccia: scheda **Generale** delle stesse Opzioni, poi riavviare.

### Passo 4 – Il primo programma

Nella parte bassa di Thonny c'è la **Shell**. Digitare:

```
>>> 2 + 3
>>> print("Ciao, Python!")
>>> import sys; print(sys.version)
```

La terza riga deve mostrare una versione che inizia con `3.15`. Per provare un vero programma, nell'editor in alto scrivere:

```python
nome = input("Come ti chiami? ")
print("Ciao,", nome)
```

Salvarlo (**File → Salva come…**) in una cartella creata apposta, per esempio `C:\Corso_Python`, con nome `primo.py`, e premere il pulsante verde ▶ (oppure **F5**). Se il programma chiede il nome e vi saluta, tutto è pronto.

## Se qualcosa non funziona

Nessun problema: il primo quarto d'ora della prima lezione è riservato a sistemare le installazioni. Questi sono i casi più comuni.

| Sintomo | Causa probabile | Cosa fare |
| --- | --- | --- |
| `python` non è riconosciuto come comando | Il comando non è ancora configurato | Usare `py` al posto di `python` (per esempio `py --version`). Se anche `py` non funziona, eseguire `py install --configure` e riaprire la finestra nera |
| Scrivendo `python` si apre il Microsoft Store | Un collegamento di Windows intercetta il comando | Usare `py`, oppure eseguire `py install --configure`. In alternativa: Impostazioni → App → Impostazioni app avanzate → *Alias di esecuzione app* e disattivare le voci `python.exe` e `python3.exe` del «Programma di installazione app» |
| Thonny mostra una versione di Python precedente alla 3.15 | Sta usando la sua copia interna | Ripetere il Passo 3 e riavviare Thonny |
| Il file si chiama `primo.py.txt` | Windows nasconde le estensioni | In Esplora file: Visualizza → Mostra → *Estensioni nomi file*, poi rinominare il file |
| L'installer chiede la password di amministratore | Computer gestito dalla scuola | Di norma Python si installa solo per il proprio utente; se la richiesta compare comunque, portare il portatile alla lezione 1 |
| L'antivirus blocca il file scaricato | Falso allarme su file nuovo | Scaricare solo da python.org e thonny.org, poi sbloccare il file dall'antivirus |
| Il Microsoft Store non si apre o è bloccato | Restrizioni del computer della scuola | Scaricare il pacchetto MSIX dalla pagina dell'install manager, oppure portare il portatile alla lezione 1 |

## Cos'è Python

Python è un linguaggio di programmazione **generalista**: serve per fare calcoli, analizzare dati, disegnare grafici, automatizzare compiti ripetitivi, costruire siti web e molto altro. È **interpretato**: il computer legge il programma riga per riga e lo esegue subito, senza una fase di compilazione separata. Questo permette di provare un'istruzione e vederne l'effetto immediatamente, ottimo per imparare.

La sua caratteristica più riconoscibile è la leggibilità: il codice somiglia a un testo ordinato e la struttura è data dall'**indentazione** (i rientri), non da parentesi graffe. Per esempio, i quadrati dei numeri da 1 a 5:

```python
for n in range(1, 6):
    print(n, n**2)
```

Non serve capire tutto ora: alla seconda lezione scriverete cicli come questo da soli.

## Se avete già programmato

Chi ha usato Fortran, Pascal, C o C++ ritroverà molte idee (variabili, cicli, funzioni), ma alcune abitudini vanno aggiornate. Chi non ha mai programmato può saltare questa sezione: il corso parte comunque dalle basi.

| Argomento | In Fortran, Pascal, C/C++ | In Python |
| --- | --- | --- |
| Esecuzione | Si scrive, si compila, si lancia l'eseguibile | Si esegue direttamente; nella Shell anche una riga alla volta |
| Blocchi di codice | `begin`/`end`, graffe, `DO`…`END DO` | Due punti e **rientro**: il rientro è parte della sintassi |
| Fine istruzione | Punto e virgola (Pascal, C) | A capo; niente punto e virgola |
| Tipi delle variabili | Dichiarati (`INTEGER`, `int`, `var x: real`) | Non si dichiarano: la variabile prende il tipo del valore e può cambiarlo |
| Interi | Dimensione fissa, con rischio di overflow | Nessun limite di grandezza |
| Divisione | Tra interi dà un intero (C, Fortran) | `/` dà sempre un decimale; `//` è la divisione intera |
| Potenza | `**` in Fortran, `pow` in C, nessun operatore in Pascal | `**` |
| Assegnazione e confronto | `:=` e `=` in Pascal; `=` e `==` in C | `=` assegna, `==` confronta |
| Cicli `for` | `DO i = 1, n`: estremi compresi | `range(1, n + 1)`: l'estremo finale è **escluso** |
| Vettori | Dimensione dichiarata, stesso tipo, indici spesso da 1 | Liste che crescono, anche di tipi misti; indici da **0** |
| Lettura da tastiera | `READ`, `scanf`, `cin` con il tipo dichiarato | `input()` restituisce sempre **testo**: va convertito con `int()` o `float()` |
| Calcolo numerico pesante | Veloce di per sé | Python da solo è più lento; si usano NumPy e SciPy, scritti in C e Fortran |

In pratica i due inciampi più frequenti sono il rientro dimenticato e `input()` che restituisce testo. Alla seconda lezione scriverete cicli ed equazioni come in uno qualsiasi di questi linguaggi, con meno cerimonie.

## Storia e autore

Python nasce dal lavoro di **Guido van Rossum**, programmatore olandese, che nel dicembre 1989 iniziò a svilupparlo al CWI (il centro nazionale di matematica e informatica dei Paesi Bassi, ad Amsterdam) come successore di un linguaggio didattico chiamato ABC. Il nome non viene dal serpente ma dalla serie televisiva britannica *Monty Python's Flying Circus*, di cui Guido era appassionato: per questo la documentazione è piena di battute e di esempi con `spam` e `eggs`.

Per quasi trent'anni Guido è stato il «Benevolent Dictator For Life» (BDFL), cioè l'ultima voce sulle decisioni di progetto. Nel luglio 2018 ha lasciato quel ruolo; dal 2019 il linguaggio è guidato da uno *Steering Council* di cinque persone elette dagli sviluppatori. Il linguaggio appartiene a una comunità, tutelata dalla Python Software Foundation (nata nel 2001), non a una singola azienda.

| Data | Evento |
| --- | --- |
| Dicembre 1989 | Guido van Rossum inizia a sviluppare Python al CWI |
| Febbraio 1991 | Prima versione pubblica (0.9) |
| Gennaio 1994 | Python 1.0 |
| Ottobre 2000 | Python 2.0 |
| Dicembre 2008 | Python 3.0: nuova versione non compatibile con la 2, per correggere difetti di progetto |
| 1 gennaio 2020 | Fine del supporto a Python 2 |
| Ottobre 2020 | Python 3.9: da qui in poi una nuova versione ogni anno, a ottobre |
| 9 ottobre 2026 | Python 3.15.0, la versione del corso |

Questo spiega perché in rete si trovano ancora esempi vecchi che usano `print "ciao"` senza parentesi: sono codice per Python 2, che non funziona più. Noi usiamo solo Python 3.

## Le implementazioni

«Python» indica due cose: il **linguaggio** (le regole, descritte nella documentazione ufficiale) e i programmi che lo eseguono, detti **implementazioni**. Quella che installiamo, e che la maggior parte delle persone usa, si chiama **CPython** (la C è il linguaggio in cui è scritta) ed è l'implementazione di riferimento.

| Implementazione | A cosa serve |
| --- | --- |
| CPython | L'implementazione ufficiale e più diffusa; quella del corso. Dalla 3.13 include anche funzioni sperimentali (compilatore JIT, esecuzione senza il blocco globale GIL) |
| PyPy | Alternativa con compilazione JIT, spesso più veloce su programmi che girano a lungo, ma meno compatibile con alcune librerie scientifiche |
| MicroPython e CircuitPython | Versioni ridotte per microcontrollori (Raspberry Pi Pico, micro:bit e simili): ottimi per la didattica con l'elettronica |
| Jython e IronPython | Python integrato nell'ecosistema Java e in quello .NET; oggi poco usati |
| Pyodide | CPython compilato per il browser: permette di eseguire Python in una pagina web senza installare nulla |

Per chi insegna è utile saperlo: lo stesso codice di base funziona, con piccole differenze, dal portatile alla scheda elettronica.

## Perché Python si è diffuso così tanto

Nessuna di queste ragioni basta da sola; insieme hanno fatto la differenza.

- **Leggibilità.** Il codice è vicino al linguaggio naturale e la formattazione è parte della sintassi: programmi scritti da persone diverse si somigliano e si leggono bene.
- **Facile da cominciare.** Non servono dichiarazioni di tipi, file di progetto o compilazione: si scrive e si esegue. Per questo è diventato il linguaggio di molti corsi introduttivi, universitari e non.
- **«Batterie incluse».** La libreria standard copre molti compiti (file, date, matematica, statistica, reti) senza installare nulla.
- **Ecosistema enorme.** PyPI, l'archivio pubblico dei pacchetti, ne contiene centinaia di migliaia, installabili con un comando (`pip install`).
- **Colla tra mondi.** Le parti pesanti dei calcoli sono scritte in C o Fortran (NumPy, SciPy) e usate da Python in modo semplice: si ottiene facilità d'uso con buone prestazioni sui calcoli numerici.
- **Scienza e dati.** Strumenti come Jupyter, pandas, matplotlib e SymPy hanno portato Python nei laboratori e nelle aule di fisica, chimica, matematica e biologia; poi l'apprendimento automatico (PyTorch, scikit-learn) ha fatto il resto.
- **Gratuito, aperto, multipiattaforma.** Funziona su Windows, macOS e Linux, e non ci sono licenze da pagare per scuola o ricerca.
- **Comunità.** Tantissima documentazione, tutorial e risposte a ogni domanda in rete, anche in italiano.

## Lo Zen di Python

Nel 2004 Tim Peters, uno degli sviluppatori storici, ha riassunto in 19 aforismi (il ventesimo è volutamente lasciato vuoto) la filosofia del linguaggio. Il testo originale in inglese è la proposta [PEP 20](https://peps.python.org/pep-0020/) e si legge direttamente in Python: aprite la Shell di Thonny e scrivete

```
import this
```

Alcuni dei principi, in una traduzione libera:

- Bello è meglio di brutto.
- Esplicito è meglio di implicito.
- Semplice è meglio di complesso.
- La leggibilità conta.
- Gli errori non dovrebbero mai passare in silenzio.
- Davanti a un'ambiguità, resistere alla tentazione di indovinare.

Non sono regole tecniche, ma un invito a scrivere codice che un'altra persona (o voi stessi tra sei mesi) possa capire. È un buon criterio anche per scrivere una verifica o una dispensa.

## Perché usare Python e perché no

Python è una scelta eccellente per imparare e per il calcolo scientifico, ma non è lo strumento giusto per tutto. Vale la pena saperlo, anche per spiegarlo agli studenti.

| Ambito | Giudizio | Motivo |
| --- | --- | --- |
| Imparare a programmare | Ottimo | Sintassi pulita, feedback immediato nella Shell |
| Calcoli, dati e grafici | Ottimo | NumPy, pandas, matplotlib, SciPy, SymPy |
| Automatizzare compiti (file, tabelle, documenti) | Ottimo | Script brevi con la libreria standard |
| Siti web e servizi | Buono | Framework maturi (Django, Flask, FastAPI) |
| Velocità pura nei cicli | Limitato | Essendo interpretato è spesso molto più lento di C o Rust; si rimedia con NumPy e simili |
| App per smartphone e videogiochi pesanti | Poco adatto | Gli strumenti principali usano altri linguaggi (Kotlin, Swift, C++, C#) |
| Programmi grandi con molte persone | Richiede disciplina | I tipi sono controllati solo durante l'esecuzione: servono test e annotazioni di tipo |
| Dare un programma a chi non ha Python | Scomodo | Serve impacchettare il programma o installare Python sul computer di chi lo usa |
| Gestione di librerie e ambienti | Può confondere | Esistono più strumenti (pip, venv, conda, Poetry, uv) e più versioni sullo stesso computer |

Per i nostri obiettivi (calcolare, simulare, visualizzare, preparare materiale didattico) i primi tre punti contano molto più degli ultimi.

## Altri modi di usare Python

Nel corso useremo Thonny perché è pensato per chi inizia. Chi lo desidera può provare altri ambienti, che usano lo stesso linguaggio.

| Strumento | Quando conviene | Note |
| --- | --- | --- |
| IDLE | Il minimo indispensabile | Installato insieme a Python, essenziale ma senza strumenti per il debug |
| Visual Studio Code | Programmi più grandi, uso professionale | Richiede l'estensione Python di Microsoft e un po' di configurazione iniziale |
| Jupyter / JupyterLab | Lezioni e relazioni con testo, formule, codice e grafici insieme | Si installa con `pip install jupyterlab`; lo accenneremo nell'ultima lezione |
| Google Colab | Provare Python senza installare nulla | Gira nel browser, richiede un account Google; i file restano nel proprio Drive |
| Anaconda / Miniconda | Distribuzione con molte librerie scientifiche già pronte | Molto diffusa in ambito scientifico, ma pesante e con un proprio sistema di installazione |
| Riga di comando | Provare piccole istruzioni | Digitando `py` si apre l'interprete interattivo (si esce con `exit()`) |

Un elenco più ampio di strumenti e librerie, diviso per argomento (matematica, dati, grafici, chimica e altro), è nel file [`../risorse/strumenti_e_librerie.md`](../risorse/strumenti_e_librerie.md).

## Curiosità

Da provare nella Shell di Thonny:

- `import this` stampa lo Zen di Python.
- `import antigravity` apre nel browser un famoso fumetto di xkcd su Python.
- `from __future__ import braces` risponde con un errore dal messaggio «not a chance»: in Python le graffe non delimitano i blocchi e non cambierà.
- `0.1 + 0.2` dà `0.30000000000000004`, non 0.3. Non è un errore di Python: è il modo in cui tutti i computer rappresentano i decimali. Ne parleremo, è un ottimo spunto per la classe.
- `2 ** 1000` calcola senza problemi un numero con oltre 300 cifre: in Python gli interi non hanno un limite fisso di grandezza.
- Con Python 3.15 la codifica predefinita dei file di testo è UTF-8: meno problemi con lettere accentate e simboli (gradi, µ, pedici), un vantaggio su Windows.

## Suggerimenti per affrontare il corso

- **Scrivere a mano il codice**, invece di copiare e incollare: le dita imparano e si notano i dettagli (maiuscole, due punti, rientri).
- **Usare i suggerimenti di Thonny**: premendo Ctrl+Spazio mentre si scrive compare l'elenco di ciò che si può digitare, con la spiegazione accanto; nella Shell, `help(nome)` descrive un comando. Dettagli nella [guida a Thonny](../risorse/guida_thonny.md), insieme a una [scheda riassuntiva](../risorse/scheda_riassuntiva.md) e a un [glossario](../risorse/glossario.md).
- **Gli errori sono normali**, anche per chi programma da anni. Python scrive il problema nell'ultima riga del messaggio: leggerla con calma, di solito indica anche il numero della riga.
- **Sperimentare nella Shell** di Thonny: provare cose, anche sbagliate, non rompe nulla.
- **Una cartella dedicata** (per esempio `C:\Corso_Python`), con nomi di file senza spazi né accenti: `lezione1_esercizio2.py`.
- **Un problema alla volta**: se un programma non funziona, ridurlo al pezzo più piccolo che si rompe.
- **Portare il portatile carico** e il caricabatterie; per i computer della scuola verificare prima di poter installare programmi.
- Non serve esperienza pregressa: chi ha già programmato ritroverà idee note, chi parte da zero seguirà un percorso che riparte dalle basi. Bastano curiosità e un po' di pazienza.

### Lista di controllo prima della lezione 1

- [ ] Python 3.15 installato (`py --version` mostra 3.15.0)
- [ ] Thonny installato e configurato con Python 3.15
- [ ] Cartella del corso creata e `primo.py` eseguito con successo
- [ ] Estensioni dei file visibili in Esplora file
- [ ] (Facoltativo) letta questa guida e provato `import this` nella Shell

Il materiale del corso (slide, esercizi e codice di esempio) sarà nel repository GitHub pubblico [github.com/LK-s/corso-python-scuola](https://github.com/LK-s/corso-python-scuola): si scarica senza account con il pulsante *Code → Download ZIP*. Il link sarà confermato per email prima della lezione 1.

Le dispense sono file Markdown (`.md`): il modo più comodo per leggerle è aprirle sulla pagina GitHub del repository, dove compaiono già formattate. Aperte offline con un doppio clic (Blocco note) si leggono, ma come testo semplice. Facoltativo: Visual Studio Code le mostra formattate con `Ctrl+Maiusc+V`. Dettagli nel `README.md` principale.

## Fonti

- [Python install manager – python.org](https://www.python.org/downloads/latest/pymanager/) (versione 26.4 del 9 ottobre 2026: Microsoft Store, MSIX, MSI)
- [Python 3.15.0 – python.org](https://python.org/downloads/release/python-3150/) (rilasciato il 9 ottobre 2026)
- [Thonny – note di rilascio](https://github.com/thonny/thonny/releases) (la versione 5 supporta Python da 3.11 a 3.15)
- [Storia di Python – Wikipedia](https://en.wikipedia.org/wiki/History_of_Python)
- [PEP 20 – The Zen of Python](https://peps.python.org/pep-0020/)
