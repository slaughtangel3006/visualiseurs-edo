"""Systèmes dynamiques classiques, écrits sous la forme y' = f(t, y)."""
import numpy as np


def lotka_volterra(t, y, a=1.0, b=0.1, c=1.5, d=0.075):
    """Renvoie la dérivée du système proies-prédateurs de Lotka-Volterra.

    Précondition : y = [proies, prédateurs], paramètres a, b, c, d réels
    Exemple(s) :
    $$$ lotka_volterra(0.0, np.array([2.0, 1.0]), 1.0, 1.0, 1.0, 1.0)
    array([0., 1.])
    """
    x, z = y
    return np.array([a * x - b * x * z, d * x * z - c * z])


def pendule(t, y, g=9.81, l=1.0):
    """Renvoie la dérivée du pendule simple, avec y = [angle, vitesse angulaire].

    Précondition : l > 0
    Exemple(s) :
    $$$ pendule(0.0, np.array([np.pi / 2, 0.0]), 1.0, 1.0)
    array([ 0., -1.])
    """
    theta, omega = y
    return np.array([omega, -g / l * np.sin(theta)])


def lorenz(t, y, sigma=10.0, rho=28.0, beta=8.0 / 3.0):
    """Renvoie la dérivée du système de Lorenz, avec y = [x, y, z].

    Précondition : sigma, rho, beta réels
    Exemple(s) :
    $$$ lorenz(0.0, np.array([1.0, 1.0, 1.0]), 10.0, 28.0, 1.0)
    array([ 0., 26.,  0.])
    """
    x, z, w = y
    return np.array([sigma * (z - x), x * (rho - w) - z, x * z - beta * w])
