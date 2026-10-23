"""Solveurs numériques d'équations différentielles ordinaires (EDO).

Les méthodes d'Euler et de Runge-Kutta d'ordre 4 sont codées à la main,
sans scipy, afin de pouvoir les comparer ensuite à scipy.integrate.
"""
import numpy as np


def euler_pas(f, t, y, h):
    """Effectue un pas de la méthode d'Euler explicite pour y' = f(t, y).

    Précondition : h != 0 ; f(t, y) renvoie un tableau numpy de même forme que y
    Exemple(s) :
    $$$ euler_pas(lambda t, y: np.array([2.0]), 0.0, np.array([1.0]), 0.5)
    array([2.])
    """
    return y + h * f(t, y)


def rk4_pas(f, t, y, h):
    """Effectue un pas de la méthode de Runge-Kutta d'ordre 4 pour y' = f(t, y).

    Précondition : h != 0 ; f(t, y) renvoie un tableau numpy de même forme que y
    Exemple(s) :
    $$$ rk4_pas(lambda t, y: np.array([2.0]), 0.0, np.array([1.0]), 0.5)
    array([2.])
    """
    k1 = f(t, y)
    k2 = f(t + h / 2, y + h / 2 * k1)
    k3 = f(t + h / 2, y + h / 2 * k2)
    k4 = f(t + h, y + h * k3)
    return y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6


def integrer(f, y0, t0, t1, h, pas=rk4_pas):
    """Intègre y' = f(t, y) de t0 à t1 avec le pas h et renvoie (temps, valeurs).

    Précondition : t1 > t0, h > 0, (t1 - t0) / h entier, y0 tableau numpy
    Exemple(s) :
    $$$ len(integrer(lambda t, y: np.array([0.0]), np.array([1.0]), 0.0, 1.0, 0.25)[0])
    5
    $$$ integrer(lambda t, y: np.array([0.0]), np.array([1.0]), 0.0, 1.0, 0.25)[1][-1]
    array([1.])
    """
    n = int(round((t1 - t0) / h))
    temps = t0 + h * np.arange(n + 1)
    valeurs = np.empty((n + 1, len(y0)))
    valeurs[0] = y0
    for i in range(n):
        valeurs[i + 1] = pas(f, temps[i], valeurs[i], h)
    return temps, valeurs
