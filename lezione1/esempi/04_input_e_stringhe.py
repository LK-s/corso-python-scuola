# Lezione 1 - Input dell'utente e stringhe

nome = input("Come ti chiami? ")
anno_nascita = int(input("In che anno sei nato/a? "))   # input() restituisce sempre testo: va convertito

anno_corrente = 2026
eta = anno_corrente - anno_nascita

print(f"Ciao {nome}, nel {anno_corrente} compi (o hai compiuto) {eta} anni.")
print("Il tuo nome ha", len(nome), "lettere")
print(nome.upper())
print("Prima lettera:", nome[0], "- ultima lettera:", nome[-1])
