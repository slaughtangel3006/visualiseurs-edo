"""Démonstration : portrait de phase de Lotka-Volterra et ordre de convergence."""
import matplotlib.pyplot as plt
import numpy as np

from solveurs import euler_pas, rk4_pas, integrer
from systemes import lotka_volterra


def erreur_finale(pas, h):
    """Renvoie l'erreur en t = 1 de la méthode `pas` pour y' = y, y(0) = 1.

    Précondition : h > 0 et 1 / h entier
    Exemple(s) :
    $$$ erreur_finale(rk4_pas, 0.5) < 0.01
    True
    """
    _, valeurs = integrer(lambda t, y: y, np.array([1.0]), 0.0, 1.0, h, pas)
    return float(abs(valeurs[-1, 0] - np.e))


def main():
    """Trace le portrait de phase et la courbe d'erreur en fonction du pas.

    Précondition : matplotlib installé
    Exemple(s) :
    $$$
    """
    def f(t, y):
        return lotka_volterra(t, y, 1.0, 0.1, 1.5, 0.075)

    methodes = ((euler_pas, "Euler"), (rk4_pas, "RK4"))
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

    for pas, nom in methodes:
        _, valeurs = integrer(f, np.array([10.0, 5.0]), 0.0, 30.0, 0.05, pas)
        ax1.plot(valeurs[:, 0], valeurs[:, 1], label=nom)
    ax1.set(xlabel="proies", ylabel="prédateurs",
            title="Lotka-Volterra : portrait de phase")
    ax1.legend()

    pas_h = [1 / 2 ** k for k in range(1, 8)]
    for pas, nom in methodes:
        ax2.loglog(pas_h, [erreur_finale(pas, h) for h in pas_h], "o-", label=nom)
    ax2.set(xlabel="pas h", ylabel="erreur en t = 1",
            title="Ordre de convergence (y' = y)")
    ax2.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
