# Lezione 3 - Un dizionario per contare: quante volte compare ogni parola

testo = "la matematica è la scienza dei numeri e la chimica è la scienza della materia"

frequenze = {}
for parola in testo.split():                 # split() divide il testo negli spazi
    frequenze[parola] = frequenze.get(parola, 0) + 1

for parola, quante in frequenze.items():
    print(f"{parola:12} {quante}")

# La parola più frequente
piu_frequente = max(frequenze, key=frequenze.get)
print("La più frequente:", piu_frequente, frequenze[piu_frequente])
