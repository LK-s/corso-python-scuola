# Esercizio 4 - Quoziente e resto
dividendo = int(input("Dividendo: "))
divisore = int(input("Divisore: "))

quoziente = dividendo // divisore
resto = dividendo % divisore

print(f"{dividendo} = {divisore} * {quoziente} + {resto}")
