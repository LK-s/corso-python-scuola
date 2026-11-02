# Lezione 1 - Gli errori più comuni (e come leggerli)
#
# Ogni riga qui sotto è un errore. Sono tutte commentate: togliete il
# cancelletto (#) a UNA riga per volta, eseguite il programma e leggete
# l'ULTIMA riga del messaggio. Poi rimettete il cancelletto.

# print("ciao)                 # SyntaxError: manca una virgoletta
# print(ciao)                  # NameError: 'ciao' non è una variabile
# x = 5 +                      # SyntaxError: l'espressione è incompleta
# print(10 / 0)                # ZeroDivisionError: divisione per zero
# print("Età: " + 15)          # TypeError: non si sommano testo e numero
# eta = int("quindici")        # ValueError: il testo non è un numero
# print(Print("ciao"))         # NameError: Python distingue maiuscole e minuscole
#     print("rientro strano")  # IndentationError: rientro non previsto
# import mat                   # ModuleNotFoundError: il modulo non esiste

print("Nessun errore: tutte le righe sopra sono commentate.")
