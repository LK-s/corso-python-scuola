# Lezione 1 - Operazioni sulle stringhe

parola = "matematica"

print(len(parola))            # numero di caratteri
print(parola.upper())         # MATEMATICA
print(parola.capitalize())    # Matematica
print(parola[0])              # primo carattere (si parte da 0)
print(parola[-1])             # ultimo carattere
print(parola[0:4])            # "mate": dal carattere 0 al 3 (il 4 è escluso)
print(parola.replace("a", "A"))
print(parola.count("a"))      # quante volte compare la lettera 'a'

# Concatenazione e ripetizione
print("mate" + "matica")
print("-" * 30)

# Tre modi di combinare testo e numeri
x = 3.14159
print("Il valore è", x)                  # print separa gli argomenti con uno spazio
print("Il valore è " + str(x))           # str() trasforma un numero in testo
print(f"Il valore è {x:.2f}")            # f-string, con 2 decimali
