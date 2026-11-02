# Lezione 1 - Preparare e diluire una soluzione di acido cloridrico
# Un problema in più passi: ogni passo usa il risultato del precedente.
# Valori di prova: massa 3.646 g, volume 0.5 L, prelievo 25 mL, diluizione a 250 mL
#   -> 0.200 mol/L, pH 0.70; dopo la diluizione 0.0200 mol/L, pH 1.70.
import math

MASSA_MOLARE_HCL = 36.46    # g/mol (costante: la scriviamo in maiuscolo)

# --- Passo 1: preparazione ---
massa = float(input("Massa di HCl sciolta (g): "))
volume = float(input("Volume della soluzione (L): "))

moli = massa / MASSA_MOLARE_HCL
concentrazione = moli / volume                  # mol/L
ph = -math.log10(concentrazione)                # acido forte: [H+] = concentrazione

print()
print("Soluzione madre")
print(f"  moli: {moli:.4f} mol")
print(f"  concentrazione: {concentrazione:.4f} mol/L")
print(f"  pH: {ph:.2f}")

# --- Passo 2: diluizione (C1 * V1 = C2 * V2) ---
prelievo_ml = float(input("Prelievo dalla soluzione madre (mL): "))
finale_ml = float(input("Volume finale dopo la diluizione (mL): "))

nuova_concentrazione = concentrazione * prelievo_ml / finale_ml
nuovo_ph = -math.log10(nuova_concentrazione)
fattore = finale_ml / prelievo_ml

print()
print(f"Soluzione diluita {fattore:.0f} volte")
print(f"  concentrazione: {nuova_concentrazione:.4f} mol/L")
print(f"  pH: {nuovo_ph:.2f}")
print(f"  il pH è aumentato di {nuovo_ph - ph:.2f}")
