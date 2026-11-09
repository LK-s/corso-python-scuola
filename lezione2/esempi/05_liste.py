# Lezione 2 - Le liste: tante informazioni in una variabile

temperature = [18.5, 21.0, 19.8, 23.4, 22.1]

print(temperature)
print(len(temperature))        # quanti elementi
print(temperature[0])          # il primo (gli indici partono da 0)
print(temperature[-1])         # l'ultimo
print(temperature[1:4])        # elementi di indice 1, 2, 3

# Modificare una lista
temperature.append(20.7)       # aggiunge in fondo
temperature[0] = 18.0          # sostituisce il primo
print(temperature)

# Funzioni utili
print("Minimo:", min(temperature))
print("Massimo:", max(temperature))
print("Somma:", sum(temperature))
print("Media:", sum(temperature) / len(temperature))
print("Ordinata:", sorted(temperature))

# Scorrere una lista con for
for t in temperature:
    if t > 21:
        print(f"{t} °C: giornata calda")

# Costruire una lista con un ciclo
quadrati = []
for n in range(1, 11):
    quadrati.append(n ** 2)
print(quadrati)

# La stessa cosa, in modo compatto (list comprehension: la vedremo meglio più avanti)
quadrati2 = [n ** 2 for n in range(1, 11)]
print(quadrati == quadrati2)

# La stessa cosa, usando funzioni lambda e map
quadrati3 = list(map(lambda n: n ** 2, range(1, 11)))
print(quadrati == quadrati2 == quadrati3)
