# Esercizio 8 (bonus) - Leggere un voto valido (da 0 a 10)


def leggi_voto():
    """Chiede un voto e ripete la domanda finché non è un numero tra 0 e 10."""
    while True:
        testo = input("Voto (0-10): ")
        try:
            voto = float(testo.replace(",", "."))
        except ValueError:
            print("Scrivete un numero, per esempio 7.5")
            continue
        if 0 <= voto <= 10:
            return voto
        print("Il voto deve essere tra 0 e 10")


voto = leggi_voto()
print(f"Voto registrato: {voto}")
