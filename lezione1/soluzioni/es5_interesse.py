# Esercizio 5 - Interesse composto: C * (1 + r) ** n
capitale = float(input("Capitale iniziale (€): "))
tasso_percentuale = float(input("Tasso annuo (%): "))
anni = int(input("Numero di anni: "))

tasso = tasso_percentuale / 100
montante = capitale * (1 + tasso) ** anni
interessi = montante - capitale

print(f"Dopo {anni} anni: {montante:.2f} €")
print(f"Interessi maturati: {interessi:.2f} €")
