# Gestione degli errori con try / except
#
# Un errore (eccezione) interrompe il programma. Con try / except si prevede il problema
# e si decide cosa fare, invece di lasciare che il programma si fermi.
# Per provare ogni parte, togliere il cancelletto alla chiamata in fondo al file.
from pathlib import Path


# 1. Lo schema di base --------------------------------------------------------------
def esempio_base():
    try:
        numero = int("tre")                  # qui Python segnala un ValueError
        print("Non arriviamo qui:", numero)
    except ValueError:
        print("Non è un numero intero")      # il programma prosegue
    print("Il programma continua")


# 2. Più tipi di errore, con il messaggio originale ---------------------------------
def dividi(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Divisione per zero")
    except TypeError as errore:              # "as errore" conserva il messaggio di Python
        print("Tipi non validi:", errore)


def esempio_divisioni():
    print(dividi(10, 4))
    print(dividi(10, 0))
    print(dividi(10, "a"))


# 3. else e finally -------------------------------------------------------------------
def leggi_righe(nome_file):
    try:
        f = open(nome_file, encoding="utf-8")
    except FileNotFoundError:
        print("File non trovato:", nome_file)
        return []
    else:                                    # eseguito solo se try è andato a buon fine
        with f:
            return f.read().splitlines()
    finally:                                 # eseguito sempre, anche dopo un return
        print("Tentativo di lettura terminato")


def esempio_file():
    print(leggi_righe(Path(__file__)))       # questo file esiste
    print(leggi_righe("non_esiste.txt"))     # questo no


# 4. Sollevare un errore con raise ----------------------------------------------------
def radice_quadrata(x):
    if x < 0:
        raise ValueError("serve un numero non negativo")
    return x ** 0.5


def esempio_raise():
    for valore in (16, -4):
        try:
            print(radice_quadrata(valore))
        except ValueError as errore:
            print("Errore:", errore)


# 5. Il modello più comune: ripetere la domanda finché la risposta è valida ------------
def leggi_intero(messaggio):
    while True:
        try:
            return int(input(messaggio))
        except ValueError:
            print("Scrivete un numero intero.")


# Regole pratiche
# - Catturare l'errore specifico (ValueError, FileNotFoundError...), non "except:" da solo,
#   altrimenti si nascondono anche errori di programmazione che invece vanno corretti.
# - Mettere nel try solo le righe che possono davvero fallire.
# - Un errore di sintassi o di nome (SyntaxError, NameError) non si "gestisce": si corregge.
# - Per un approfondimento: https://docs.python.org/it/3/tutorial/errors.html

# esempio_base()
# esempio_divisioni()
# esempio_file()
# esempio_raise()
# print(leggi_intero("Un numero intero: "))
