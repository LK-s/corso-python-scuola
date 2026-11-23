# Un modulo scritto da noi: raccoglie funzioni da riusare in altri programmi.
# Si usa con: import miei_strumenti   (il file deve stare nella stessa cartella)


def media(valori):
    return sum(valori) / len(valori)


def e_primo(n):
    if n < 2:
        return False
    divisore = 2
    while divisore * divisore <= n:
        if n % divisore == 0:
            return False
        divisore += 1
    return True


def leggi_numero(messaggio):
    """Chiede un numero all'utente e ripete la domanda finché la risposta non è valida."""
    while True:
        testo = input(messaggio)
        try:
            return float(testo.replace(",", "."))
        except ValueError:
            print("Non è un numero, riprova.")
