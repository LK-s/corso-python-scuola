# Esercizio 3 - Media di tre voti
voto1 = float(input("Primo voto: "))
voto2 = float(input("Secondo voto: "))
voto3 = float(input("Terzo voto: "))

media = (voto1 + voto2 + voto3) / 3
print(f"Media: {media:.2f}")
print("Media arrotondata:", round(media))
