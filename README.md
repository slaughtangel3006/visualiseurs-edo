# Visualiseur d'équations différentielles

Solveurs d'EDO codés à la main (Euler, Runge-Kutta 4), appliqués à des systèmes
dynamiques classiques (Lotka-Volterra, pendule, Lorenz) et comparés à `scipy`.

## Contenu

- `src/solveurs.py` : `euler_pas`, `rk4_pas`, `integrer`
- `src/systemes.py` : `lotka_volterra`, `pendule`, `lorenz`
- `src/demo.py` : portrait de phase et courbe d'ordre de convergence

## Installation

```
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux / macOS
pip install -r requirements.txt
```

## Utilisation

```
python src/demo.py
```

## Feuille de route

- [x] Méthodes d'Euler et RK4
- [x] Systèmes : Lotka-Volterra, pendule, Lorenz
- [x] Étude de l'ordre de convergence
- [ ] Comparaison avec `scipy.integrate.solve_ivp` (erreur, coût)
- [ ] Interface interactive avec curseurs (Streamlit)
- [ ] GIF des simulations dans ce README

## Licence

MIT
