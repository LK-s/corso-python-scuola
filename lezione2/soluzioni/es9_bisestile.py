# Esercizio 9 (bonus) - Anno bisestile


def e_bisestile(anno):
    """Vero se l'anno è bisestile: divisibile per 4, ma non per 100, a meno che lo sia per 400."""
    return (anno % 4 == 0 and anno % 100 != 0) or anno % 400 == 0


for anno in [1900, 2000, 2024, 2100]:
    print(anno, e_bisestile(anno))
