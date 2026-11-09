# Lezione 2 - Numeri primi: tutto insieme (funzioni, cicli, condizioni, liste)

def e_primo(n):
    if n < 2:
        return False
    divisore = 2
    while divisore * divisore <= n:
        if n % divisore == 0:
            return False
        divisore += 1
    return True


primi = []
for numero in range(1, 101):
    if e_primo(numero):
        primi.append(numero)

print("Primi fino a 100:", primi)
print("Quanti sono:", len(primi))

# Primi gemelli: coppie di primi che differiscono di 2
for p in primi:
    if e_primo(p + 2):
        print(f"({p}, {p + 2})", end=" ")

print()

# La stessa ricerca con le comprehension: ogni lista si costruisce in una riga
primi2 = [n for n in range(1, 101) if e_primo(n)]
gemelli = [(p, p + 2) for p in primi2 if e_primo(p + 2)]
print("Primi gemelli:", gemelli)
print("Quante coppie:", len(gemelli))
print("Stesso elenco di primi di prima:", primi2 == primi)
