# Lezione 4 - Il primo grafico con matplotlib
import matplotlib.pyplot as plt

# Due liste della stessa lunghezza: i valori di x e i valori di y corrispondenti
x = [0, 1, 2, 3, 4, 5]
y = [n ** 2 for n in x]          # i quadrati: [0, 1, 4, 9, 16, 25]

plt.plot(x, y)                   # disegna la linea che passa per i punti
plt.title("I quadrati dei primi numeri")
plt.xlabel("numero")
plt.ylabel("quadrato")
plt.grid(True)                   # griglia di riferimento
plt.show()                       # apre la finestra con il grafico (chiuderla per continuare)

# Stessi dati con uno stile diverso: marcatore su ogni punto, linea tratteggiata, colore
plt.plot(x, y, marker="o", linestyle="--", color="tab:red")
plt.title("Gli stessi dati, con uno stile diverso")
plt.xlabel("numero")
plt.ylabel("quadrato")
plt.grid(True)
plt.show()

# Solo i punti, senza linea: grafico di dispersione (scatter)
plt.scatter(x, y)
plt.title("Solo i punti")
plt.show()
