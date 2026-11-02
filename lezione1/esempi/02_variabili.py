# Lezione 1 - Variabili: nomi che si riferiscono a valori

base = 12
altezza = 5
area = base * altezza / 2
print("Area del triangolo:", area)

# Una variabile può cambiare valore
altezza = 8
area = base * altezza / 2
print("Nuova area:", area)

# Ogni valore ha un tipo
print(type(base))      # int   (numero intero)
print(type(area))      # float (numero decimale)
print(type("ciao"))    # str   (testo)
print(type(True))      # bool  (vero/falso)

# Aggiornare una variabile a partire dal suo stesso valore
contatore = 0
contatore = contatore + 1
contatore += 1         # forma abbreviata di contatore = contatore + 1
print("Contatore:", contatore)

# Scambiare due valori
a, b = 3, 10
a, b = b, a
print(a, b)            # 10 3
