# Lezione 2 - Le funzioni: blocchi di codice con un nome, riutilizzabili
import math


def area_cerchio(raggio):
    return math.pi * raggio ** 2


def discriminante(a, b, c):
    return b ** 2 - 4 * a * c


def media(valori):
    return sum(valori) / len(valori)


def saluta(nome: str, entusiasta: bool=False):
    # Un parametro può avere un valore predefinito
    if entusiasta:
        return f"Ciao {nome}!!!"
    return f"Ciao {nome}"


print(area_cerchio(3))                  # 28.274333882308138 (tutte le cifre)
print(f"{area_cerchio(3):.2f}")          # 28.27 (due cifre decimali)
print(discriminante(1, -5, 6))          # 1
print(media([6, 7.5, 8, 5.5]))
print(saluta("Maria"))
print(saluta("Maria", entusiasta=True))


# Una funzione può restituire più valori
def quoziente_e_resto(a, b):
    return a // b, a % b


q, r = quoziente_e_resto(47, 5)
print(q, r)        # 9 2

# Le variabili create dentro una funzione esistono solo lì dentro (variabili locali)

# --- Annotazioni di tipo (type hints) ---
# Dopo ogni parametro si scrive il tipo atteso (: float) e dopo la parentesi il tipo del risultato (-> float).
# ATTENZIONE: Python NON le controlla quando esegue il programma, quindi non cambiano il risultato.
# Servono a chi legge il codice e a strumenti come mypy che controllano il file PRIMA di eseguirlo
# (installazione: py -m pip install mypy; uso nella Shell di Thonny: !mypy 07_funzioni.py).
def area_rettangolo(base: float, altezza: float) -> float:
    return base * altezza


def classifica_ph(ph: float) -> str:
    if ph < 7:
        return "acida"
    elif ph > 7:
        return "basica"
    return "neutra"


print(area_rettangolo(4, 2.5))     # 10.0
print(classifica_ph(6.2))          # acida

# Gli errori che le annotazioni permettono di scoprire. Togliete il # alle righe, una prova alla volta:
#
# 1) Un testo al posto di un numero (succede con input() dimenticando float(...)).
#    Senza annotazioni Python NON dà errore e stampa un risultato sbagliato:
# lato = "ab"
# print(area_rettangolo(lato, 3))    # stampa ababab (il testo viene ripetuto 3 volte)
#    mypy segnala: Argument 1 to "area_rettangolo" has incompatible type "str"; expected "float"
#
# 2) Qui Python se ne accorge, ma solo quando la riga viene eseguita (e il programma si ferma lì):
# print(classifica_ph("7"))          # TypeError: '<' not supported between instances of 'str' and 'int'
#    mypy lo segnala prima di eseguire, con lo stesso messaggio del caso 1.
#
# 3) Un caso dimenticato: se manca la riga finale  return "neutra"  la funzione per ph = 7
#    restituisce None senza errore, e il guaio si vede molto più avanti nel programma.
#    mypy segnala: Missing return statement
