# Lezione 2 - Confronti e valori booleani (True / False)

a = 7
b = 10

print(a < b)        # True
print(a == b)       # False   ATTENZIONE: == confronta, = assegna
print(a != b)       # True    diverso
print(a >= 7)       # True

# Operatori logici: and, or, not
x = 5
print(0 < x and x < 10)     # True: x è compreso tra 0 e 10
print(0 < x < 10)           # lo stesso, in forma abbreviata (come in matematica)
print(x < 0 or x > 100)     # False
print(not x == 5)           # False

# Divisibilità con il resto
n = 18
print(n % 2 == 0)           # True: n è pari
print(n % 3 == 0 and n % 5 != 0)

# Confrontare numeri decimali: meglio usare una tolleranza
print(0.1 + 0.2 == 0.3)                 # False
print(abs((0.1 + 0.2) - 0.3) < 1e-9)    # True
