# Strumenti e librerie utili

Elenco di strumenti e librerie Python, diviso per uso. La colonna «Nel corso» indica cosa tocchiamo a lezione; tutto il resto è per l'approfondimento.

## Come installare una libreria

I moduli della libreria standard (`math`, `random`, `csv`…) sono già inclusi in Python. Le altre librerie si installano da PyPI in due modi:

1. In Thonny: **Strumenti → Gestisci pacchetti** (in inglese *Tools → Manage packages*), cercare il nome e premere **Installa**.
2. Dal prompt dei comandi: `py -m pip install nome_libreria`.

Python 3.15 è uscito il 9 ottobre 2026: le librerie più diffuse (NumPy, pandas, SciPy, matplotlib) di solito sono pronte subito, mentre quelle specialistiche possono arrivare dopo settimane. Se pip risponde «No matching distribution found», la libreria non è ancora disponibile per la 3.15: conviene provare l'installazione prima di usarla in classe.

### Se una libreria non è ancora compatibile con Python 3.15

Alcune librerie, soprattutto quelle specialistiche (chimica, calcolo scientifico avanzato), possono non essere ancora aggiornate per la 3.15. In questo caso si usa una versione precedente di Python, per esempio la 3.14, che l'install manager può affiancare alla 3.15 senza rimuoverla:

1. Dal Prompt dei comandi: `py install 3.14`.
2. Installare la libreria in quella versione: `py -3.14 -m pip install nome_libreria`.
3. Eseguire i programmi con `py -3.14 nomefile.py`. In Thonny si cambia interprete da **Strumenti → Opzioni → Interprete**, come per la 3.15 (vedi la guida pre-corso).

Il codice del corso funziona anche con la 3.14.

**Prova di installazione con Python 3.15.0 su Windows (26 ottobre 2026):** la situazione cambia in fretta, quindi conviene ripetere la prova prima di usare una libreria in classe.

- **Installate e provate con un esempio funzionante:** NumPy, SciPy, pandas, matplotlib, SymPy, molmass, chemlib, periodictable, PubChemPy.
- **pip trova una versione installabile (uso non provato):** mpmath, RDKit, seaborn, Plotly, Manim, NetworkX, openpyxl, Pillow, Pint, uncertainties, lmfit, py3Dmol, ASE.
- **Problemi:** *mendeleev* non si installa (richiede versioni vecchie di NumPy e SQLAlchemy da compilare); *Cantera* ha solo il codice sorgente per la 3.15 e richiede un compilatore; *ChemPy* si installa, ma porta con sé molti pacchetti (anche Jupyter), alcuni compilati sul posto. Per queste tre conviene usare Python 3.14 oppure lasciarle per l'approfondimento personale.

Colonna **Nel corso**: *Sì* = si usa a lezione; *Citato* = nominato nella guida pre-corso o a lezione; *Forse* = possibile nelle lezioni 3-4, ancora da confermare; *—* = solo approfondimento.

## Ambienti ed editor

| Nome | A cosa serve | Nel corso |
| --- | --- | --- |
| [Thonny](https://thonny.org) | Editor per chi inizia, con debugger passo-passo | Sì |
| [IDLE](https://docs.python.org/it/3/library/idle.html) | Editor minimale incluso con Python | Citato |
| [Visual Studio Code](https://code.visualstudio.com) | Editor generale: con l'estensione Python di Microsoft diventa un ambiente completo | Citato |
| [JupyterLab](https://jupyter.org) | Quaderni che mescolano testo, formule, codice e grafici | Citato |
| [Spyder](https://www.spyder-ide.org) | Ambiente per il calcolo scientifico, con esplora variabili e grafici integrati | — |
| [PyCharm](https://www.jetbrains.com/pycharm/) | Ambiente professionale per progetti grandi; esiste una versione gratuita | — |
| [Anaconda](https://www.anaconda.com) | Distribuzione con molte librerie scientifiche già pronte | Citato |

## Strumenti non Python da affiancare

Non sono librerie Python, ma molti insegnanti li usano già e si integrano bene con quello che si fa in Python.

| Nome | A cosa serve | Nel corso |
| --- | --- | --- |
| [GeoGebra](https://www.geogebra.org) | Geometria dinamica, grafici di funzioni e calcolo: ottimo per esplorare un problema prima di programmarlo | — |
| [Desmos](https://www.desmos.com/calculator) | Calcolatrice grafica online, immediata per tracciare funzioni e cursori | — |
| [SageMath](https://www.sagemath.org) | Sistema di calcolo simbolico basato su Python; su Windows l'installazione è impegnativa | — |

## Provare Python senza installare

| Nome | A cosa serve | Nel corso |
| --- | --- | --- |
| [Google Colab](https://colab.research.google.com) | Quaderni Jupyter nel browser; serve un account Google | Citato |
| [Python Tutor](https://pythontutor.com) | Mostra passo passo cosa accade in memoria mentre il codice gira: ottimo per spiegare variabili, cicli e funzioni | — |
| [JupyterLite](https://jupyterlite.readthedocs.io) | Jupyter che gira interamente nel browser, senza server | — |
| [Pyodide](https://pyodide.org) | Python compilato per il browser; è la base di JupyterLite | Citato |

## Pacchetti e ambienti virtuali

| Nome | A cosa serve | Nel corso |
| --- | --- | --- |
| [Python install manager](https://www.python.org/downloads/latest/pymanager/) | Installa e gestisce le versioni di Python su Windows (`py install`, `py list`) | Sì |
| [pip](https://pip.pypa.io) | Installa le librerie da PyPI: `py -m pip install nome` | Citato |
| [PyPI](https://pypi.org) | L'archivio pubblico dei pacchetti Python, con ricerca | Citato |
| [venv](https://docs.python.org/it/3/library/venv.html) | Ambienti separati per progetto, così librerie diverse non si disturbano | — |
| [uv](https://docs.astral.sh/uv/) | Installatore molto rapido, alternativa moderna a pip e venv | — |
| [conda](https://docs.conda.io) | Gestore di pacchetti e ambienti di Anaconda e Miniconda | Citato |

## Matematica e calcolo

I primi sette moduli fanno parte della libreria standard e non richiedono installazioni.

| Nome | A cosa serve | Nel corso |
| --- | --- | --- |
| [math](https://docs.python.org/it/3/library/math.html) | Radici, trigonometria, logaritmi, costanti | Sì (lezione 1) |
| [random](https://docs.python.org/it/3/library/random.html) | Numeri casuali per simulazioni e giochi | Sì (lezione 2, bonus) |
| [fractions](https://docs.python.org/it/3/library/fractions.html) | Frazioni esatte: `Fraction(1, 3) + Fraction(1, 6)` dà `1/2` | — |
| [decimal](https://docs.python.org/it/3/library/decimal.html) | Decimali a precisione scelta, senza gli errori di arrotondamento dei numeri in virgola mobile | — |
| [statistics](https://docs.python.org/it/3/library/statistics.html) | Media, mediana e deviazione standard di una lista di dati | — |
| [cmath](https://docs.python.org/it/3/library/cmath.html) | Funzioni per i numeri complessi | — |
| [itertools](https://docs.python.org/it/3/library/itertools.html) | Permutazioni, combinazioni, prodotto cartesiano: combinatoria e probabilità | — |
| [SymPy](https://www.sympy.org) | Calcolo simbolico: equazioni, derivate, integrali, limiti, semplificazioni, formule in LaTeX | Forse (lezione 4) |
| [NumPy](https://numpy.org) | Array e calcolo su vettori e matrici, molto veloce | Forse (lezione 4) |
| [SciPy](https://scipy.org) | Integrazione numerica, equazioni differenziali, ottimizzazione, interpolazione | — |
| [mpmath](https://mpmath.org) | Aritmetica a precisione arbitraria, per esempio migliaia di cifre di π | — |

## Dati e tabelle

| Nome | A cosa serve | Nel corso |
| --- | --- | --- |
| [csv](https://docs.python.org/it/3/library/csv.html) | Leggere e scrivere file CSV | Forse (lezione 3) |
| [json](https://docs.python.org/it/3/library/json.html) | File JSON, formato di scambio di molti servizi online | — |
| [pathlib](https://docs.python.org/it/3/library/pathlib.html) | Cartelle e percorsi dei file in modo indipendente dal sistema | — |
| [datetime](https://docs.python.org/it/3/library/datetime.html) | Date e orari: differenze tra date, giorni della settimana, formattazione | — |
| [collections](https://docs.python.org/it/3/library/collections.html) | Contenitori speciali, per esempio `Counter` per contare le frequenze in una lista di dati | — |
| [sqlite3](https://docs.python.org/it/3/library/sqlite3.html) | Piccoli database in un singolo file, senza installare nulla | — |
| [pandas](https://pandas.pydata.org) | Tabelle di dati: filtri, medie per gruppo, lettura di CSV ed Excel | Citato |
| [openpyxl](https://pypi.org/project/openpyxl/) | Leggere e scrivere file Excel `.xlsx`, anche con formule | — |

## Grafici e visualizzazione

| Nome | A cosa serve | Nel corso |
| --- | --- | --- |
| [matplotlib](https://matplotlib.org) | Grafici di funzioni, istogrammi, dispersione; base di molte altre librerie | Forse (lezione 3) |
| [seaborn](https://seaborn.pydata.org) | Grafici statistici più curati, costruiti su matplotlib | — |
| [Plotly](https://plotly.com/python/) | Grafici interattivi nel browser: zoom e valori al passaggio del mouse | — |
| [turtle](https://docs.python.org/it/3/library/turtle.html) | Disegno con la «tartaruga», utile per geometria e cicli; inclusa in Python | — |
| [tkinter](https://docs.python.org/it/3/library/tkinter.html) | Finestre con pulsanti, campi di testo e disegno: programmi con interfaccia grafica; inclusa in Python (Thonny stesso è scritto con tkinter) | — |
| [Manim](https://pypi.org/project/manim/) | Animazioni matematiche, nata per i video di 3Blue1Brown; installazione impegnativa | — |

## Chimica

Si installano con pip. Alcune sono pesanti e possono ritardare il supporto a una nuova versione di Python: provarle prima dell'uso in classe.

| Nome | A cosa serve | Nel corso |
| --- | --- | --- |
| [RDKit](https://www.rdkit.org) | Strutture molecolari: dalla notazione SMILES (la molecola scritta come testo) al disegno 2D, massa e proprietà; standard della chemioinformatica | — |
| [periodictable](https://pypi.org/project/periodictable/) | Dati sugli elementi, masse atomiche e isotopi: utile per le masse molari | — |
| [molmass](https://pypi.org/project/molmass/) | Massa molare e composizione percentuale a partire dalla formula scritta come testo, per esempio `H2SO4` | — |
| [chemlib](https://pypi.org/project/chemlib/) | Elementi, composti e calcoli di stechiometria, incluso il bilanciamento delle equazioni | — |
| [mendeleev](https://pypi.org/project/mendeleev/) | Banca dati degli elementi: raggi, elettronegatività, configurazioni elettroniche | — |
| [PubChemPy](https://pypi.org/project/PubChemPy/) | Interroga PubChem: dal nome di un composto a formula, massa e struttura (serve internet) | — |
| [ChemPy](https://pypi.org/project/chempy/) | Bilanciamento di equazioni, equilibri e cinetica | — |
| [Cantera](https://cantera.org) | Termodinamica e cinetica chimica, equilibri, fiamme | — |
| [py3Dmol](https://pypi.org/project/py3Dmol/) | Molecole in 3D ruotabili nei quaderni Jupyter | — |
| [ASE](https://pypi.org/project/ase/) | Strutture atomiche e cristalli, simulazioni; livello avanzato | — |

## Fisica, unità e misure

| Nome | A cosa serve | Nel corso |
| --- | --- | --- |
| [Pint](https://pypi.org/project/Pint/) | Unità di misura nei calcoli: converte e segnala operazioni incompatibili, come sommare metri e secondi | — |
| [uncertainties](https://pypi.org/project/uncertainties/) | Propagazione automatica delle incertezze di misura | — |
| [scipy.constants](https://docs.scipy.org/doc/scipy/reference/constants.html) | Costanti fisiche (CODATA) e conversioni, incluse in SciPy | — |
| [lmfit](https://pypi.org/project/lmfit/) | Adattamento di curve ai dati, con parametri e incertezze | — |

## Statistica e apprendimento automatico

Per la statistica elementare basta il modulo `statistics` (vedi «Matematica e calcolo»).

| Nome | A cosa serve | Nel corso |
| --- | --- | --- |
| [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html) | Distribuzioni di probabilità e test statistici | — |
| [statsmodels](https://www.statsmodels.org) | Regressione e modelli statistici con tabelle riassuntive | — |
| [scikit-learn](https://scikit-learn.org) | Apprendimento automatico: regressione, classificazione, raggruppamento | — |

## Materiali per la classe

| Nome | A cosa serve | Nel corso |
| --- | --- | --- |
| [ipywidgets](https://pypi.org/project/ipywidgets/) | Cursori e pulsanti nei quaderni Jupyter: variare un parametro e vedere il grafico cambiare | — |
| [Streamlit](https://streamlit.io) | Trasforma uno script in una pagina web interattiva | — |
| [Jinja2](https://pypi.org/project/Jinja2/) | Modelli di testo: generare verifiche con numeri diversi per ogni studente | — |
| [python-docx](https://pypi.org/project/python-docx/) | Creare e modificare documenti Word | — |
| [fpdf2](https://pypi.org/project/fpdf2/) | Creare PDF da Python (alternativa più completa: ReportLab) | — |
| [pypdf](https://pypi.org/project/pypdf/) | Unire, dividere e ruotare PDF | — |
| [Pillow](https://pypi.org/project/pillow/) | Elaborare immagini: ridimensionare, ritagliare, convertire | — |
| [nbgrader](https://pypi.org/project/nbgrader/) | Assegnare e correggere esercizi in Jupyter; livello avanzato | — |

## Elettronica e acquisizione dati

| Nome | A cosa serve | Nel corso |
| --- | --- | --- |
| [MicroPython](https://micropython.org) | Python per microcontrollori come Raspberry Pi Pico: sensori, LED, motori | Citato |
| [CircuitPython](https://circuitpython.org) | Variante di Adafruit pensata per la didattica | Citato |
| [pyserial](https://pypi.org/project/pyserial/) | Leggere dati da Arduino o da sensori collegati via USB | — |

## Qualità del codice

| Nome | A cosa serve | Nel corso |
| --- | --- | --- |
| Debugger di Thonny | Esecuzione passo passo, con i valori delle variabili in vista | Sì (lezione 2) |
| [doctest](https://docs.python.org/it/3/library/doctest.html) | Verifica una funzione con gli esempi scritti nella sua documentazione, senza installare nulla | — |
| [pdb](https://docs.python.org/it/3/library/pdb.html) | Debugger a riga di comando, incluso in Python | — |
| [pytest](https://docs.pytest.org) | Test automatici: verificare che una funzione dia i risultati attesi | — |
| [Ruff](https://docs.astral.sh/ruff/) | Segnala errori di scrittura e di stile e riformatta il codice | — |

## Dove continuare a imparare

| Risorsa | Contenuto | Nel corso |
| --- | --- | --- |
| [Tutorial ufficiale](https://docs.python.org/it/3/tutorial/) | In italiano, completo e ben scritto | Citato |
| [Libreria standard](https://docs.python.org/it/3/library/) | Riferimento di tutti i moduli inclusi in Python | — |
| [Project Euler](https://projecteuler.net) | Problemi di matematica da risolvere programmando, di difficoltà crescente (in inglese) | — |
| [Exercism – percorso Python](https://exercism.org/tracks/python) | Esercizi gratuiti con feedback | — |
| [Think Python, 3ª edizione](https://allendowney.github.io/ThinkPython/) | Libro gratuito di Allen Downey (in inglese): un'introduzione alla programmazione adatta a chi parte da zero | — |
| [Python for Everybody](https://www.py4e.com) | Corso e libro gratuiti di Charles Severance (in inglese), con esercizi e video; ci sono sottotitoli in diverse lingue | — |
| [Scientific Python Lectures](https://scipy-lectures.org) | Guida gratuita (in inglese) a NumPy, SciPy e matplotlib, da leggere dopo le basi | — |
| [Automate the Boring Stuff with Python](https://automatetheboringstuff.com) | Libro online gratuito (in inglese) sull'automazione di file, Excel e PDF | — |
