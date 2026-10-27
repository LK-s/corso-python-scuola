# Pre-corso

La guida completa (installazione di Python 3.15 e Thonny su Windows, differenze per chi ha già programmato,
storia di Python, perché usarlo e perché no, curiosità e suggerimenti) è nel file
[`guida_pre_corso.md`](guida_pre_corso.md).
I file `.md` si leggono meglio sulla pagina GitHub del repository (già formattati) oppure, facoltativo,
con Visual Studio Code (`Ctrl+Maiusc+V`); nel Blocco note appaiono come testo semplice.
Dettagli nel [`README.md` principale](../README.md).

**Riassunto in cinque passi:**

1. Installare il **Python install manager** da <https://www.python.org/downloads/latest/pymanager/>:
   premere il pulsante *Microsoft Store* (scelta consigliata) e poi **Ottieni** (o **Installa**) nell'app Store.
   Se il Store è bloccato (può succedere sui computer della scuola), usare *download Installer (MSIX)*
   della stessa pagina (si apre con doppio clic) oppure, dal Prompt dei comandi, `winget install 9NQ7512CXL7T`.
   Se sul computer c'è il vecchio «Python Launcher», disinstallarlo prima da Impostazioni → App.
2. Aprire il Prompt dei comandi (Start, `cmd`) e digitare `py install 3.15`.
3. Verificare con `py --version`: deve mostrare `Python 3.15.0`.
4. Installare Thonny da <https://thonny.org>. Poi, in Thonny:
   **Strumenti → Opzioni → Interprete → Interprete alternativo Python 3** e indicare il
   percorso ottenuto con `py -c "import sys; print(sys.executable)"` dal Prompt dei comandi.
5. Creare `C:\Corso_Python` (o una cartella a piacere nel proprio PC), scrivere `primo.py` con `print("Ciao, Python!")` ed eseguirlo con F5.

Per provare l'ambiente è disponibile anche il file [`verifica_installazione.py`](verifica_installazione.py).
Per eseguirlo lanciare da Prompt dei comandi `py verifica_installazione.py`

L'elenco di strumenti e librerie utili, divisi per argomento, è in
[`../risorse/strumenti_e_librerie.md`](../risorse/strumenti_e_librerie.md).
