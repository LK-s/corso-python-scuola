# Guida rapida a Thonny

Thonny è l'editor che usiamo nel corso. Questa guida raccoglie in un posto solo ciò che serve per lavorare con più sicurezza.
I nomi dei menu sono in italiano, con l'originale inglese tra parentesi; le scorciatoie sono per Windows.
(Verificato su Thonny 5.0.0: in altre versioni qualche voce può avere un nome leggermente diverso.)

## La finestra

| Parte | Cosa fa |
| --- | --- |
| **Editor** (in alto) | Qui si scrive il programma, che si salva in un file `.py` |
| **Shell** (in basso) | Qui compaiono i risultati e si risponde a `input()`. Si possono anche provare istruzioni singole |
| **Variabili** (a destra, se attivo) | Mostra nomi e valori delle variabili del programma. Si attiva da *Visualizza → Variabili* (*View → Variables*) |

Gli altri pannelli (*File*, *Assistente*, …) si mostrano o nascondono dal menu *Visualizza* (*View*): conviene tenere aperti solo
Editor, Shell e Variabili.

## Il giro di lavoro

1. **Nuovo** programma: **Ctrl+N**. **Salva**: **Ctrl+S** (la prima volta chiede nome e cartella; il nome termina con `.py`, senza spazi né accenti).
2. Scrivere il codice.
3. **Esegui**: pulsante verde ▶ oppure **F5** (*Esegui → Esegui lo script corrente*, *Run → Run current script*).
4. Leggere il risultato nella Shell. Se il programma chiede un valore (`input()`), scriverlo **nella Shell** e premere Invio.
5. In caso di errore, leggere l'**ultima riga** del messaggio: dice che errore è e a quale riga del programma.

Altri comandi utili: **Ctrl+O** apre un file, **Ctrl+Z** annulla (menu *Modifica → Annulla*), **Ctrl+3** trasforma le righe selezionate in commento e viceversa (*Modifica → Attiva commenti*).

## Fermare un programma

| Situazione | Cosa fare |
| --- | --- |
| Il programma sembra fermo: sta aspettando un valore | Guardare la Shell e rispondere a `input()` |
| Ciclo infinito o programma troppo lento | Pulsante rosso **Ferma** (*Stop*), oppure **Ctrl+F2** (*Esegui → Ferma/Riavvia il backend*) |
| Interrompere senza riavviare la Shell | **Ctrl+C** con il cursore nella Shell (*Esegui → Interrompi l'esecuzione*) |

## Farsi aiutare mentre si scrive

| Cosa si vuole | Come |
| --- | --- |
| Vedere cosa si può scrivere (per esempio dopo `math.`) | **Ctrl+Spazio** (*Modifica → Auto-completamento*). Nella Shell basta **Tab** |
| Vedere i parametri di una funzione | Dopo la parentesi aperta, **Ctrl+Maiusc+Spazio** (*Modifica → Mostra info sui parametri*) |
| Leggere la spiegazione di un comando | Nella Shell: `help(round)`, `help(math.sqrt)`, `dir(str)` |
| Vedere il codice di una funzione | **Ctrl+clic** sul nome nell'editor (utile per le funzioni scritte in Python; per quelle scritte in C il codice Python non esiste) |

**Conviene attivare i suggerimenti automatici:** *Strumenti → Opzioni → Editor* (*Tools → Options → Editor*), poi spuntare
*Proponi automaticamente suggerimenti durante la digitazione* e
*Mostra automaticamente le info del parametro dopo aver digitato '('*.
Da questa scheda si può anche attivare *Mostra i numeri di riga*: utile perché i messaggi di errore indicano la riga.

## Vedere cosa fa il programma, passo per passo (debug)

Il debug esegue il programma **una riga alla volta**, così si vede dove i valori cominciano a essere diversi da quelli attesi.

1. Aprire il pannello *Variabili* (*Visualizza → Variabili*).
2. Premere il pulsante con l'insetto (**Debug**, **Ctrl+F5**).
3. Avanzare con **F6** (*Passo sopra*, *Step over*: esegue la riga) oppure **F7** (*Passo dentro*, *Step into*: entra nella funzione chiamata);
   **F8** esce dalla funzione (*Passo fuori*, *Step out*).
4. Guardare come cambiano i valori nel pannello delle variabili. Per uscire dal debug basta il pulsante **Ferma**.

È il modo migliore per capire cicli e funzioni: lo useremo nella lezione 2.

## Leggibilità

- **Caratteri più grandi:** *Visualizza → Aumenta la dimensione del carattere* (*View → Increase font size*), oppure **Ctrl++** e **Ctrl+−**.
  Da *Strumenti → Opzioni → Temi & Font* (*Tools → Options → Theme & Font*) si scelgono anche carattere e tema.
- **Lingua dell'interfaccia:** *Strumenti → Opzioni → Generale* (*General*), voce *Lingua* (*Language*); poi riavviare Thonny.

## Scegliere la versione di Python

Thonny ha una propria copia di Python, che può essere precedente alla 3.15. Per usare quella installata con il Python install manager:
*Strumenti → Opzioni → Interprete* (*Tools → Options → Interpreter*), poi *Interprete alternativo Python 3 o ambiente virtuale*
e indicare il percorso ottenuto con `py -c "import sys; print(sys.executable)"` (dettagli nella [guida pre-corso](../pre-corso/guida_pre_corso.md)).
Per installare librerie: *Strumenti → Gestisci pacchetti* (*Tools → Manage packages*); se una libreria non è ancora compatibile con
la 3.15, vedere [strumenti e librerie](strumenti_e_librerie.md).

## Se qualcosa non va

| Sintomo | Cosa fare |
| --- | --- |
| Il programma non parte o si comporta in modo strano dopo molte prove | **Ctrl+F2** (*Ferma/Riavvia il backend*): riavvia la Shell |
| Compare `IndentationError` | Controllare i rientri: tutte le righe dello stesso blocco devono avere lo stesso numero di spazi |
| Il codice incollato dal web dà errori strani | Meglio riscriverlo a mano; i caratteri copiati possono contenere virgolette «ricurve» al posto di `"` |
| Non si trova più un file salvato | *File → Salva come…* mostra la cartella corrente; usare sempre una cartella dedicata (per esempio `C:\Corso_Python`) |
