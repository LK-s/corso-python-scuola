"""Stima di pi greco con il metodo Monte Carlo (solo libreria standard).

Idea: si lanciano punti a caso nel quadrato [0,1] x [0,1]. La frazione di
punti che cade nel quarto di cerchio di raggio 1 è circa pi/4.
"""
import random

random.seed(42)          # numeri casuali riproducibili; togliere per risultati diversi ogni volta

for lanci in (100, 10_000, 1_000_000):
    dentro = 0
    for _ in range(lanci):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            dentro += 1
    stima = 4 * dentro / lanci
    print(f"{lanci:>9} lanci -> pi ≈ {stima:.5f}")
