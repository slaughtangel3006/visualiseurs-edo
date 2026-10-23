# Visualiseur d'équations différentielles

J’ai commencé ce projet pour mieux comprendre comment se comportent des méthodes numériques simples sur des systèmes dynamiques classiques. L’idée était simple : coder moi-même un intégrateur, tester quelques méthodes, et surtout voir ce que ça donne visuellement.

J’avais envie de comparer ce que fait une méthode très simple comme Euler avec une méthode plus précise comme Runge-Kutta d’ordre 4, sans utiliser de boîte noire tout de suite. Le but n’était pas de faire un outil ultra abouti, mais plutôt de comprendre le comportement des solutions, l’impact du pas de discrétisation, et la différence entre une méthode “basique” et une méthode plus robuste.

## Ce que contient le projet

- `src/solveurs.py` : implémentation des méthodes d’Euler et de Runge-Kutta 4, ainsi que la fonction d’intégration
- `src/systemes.py` : systèmes dynamiques classiques : Lotka-Volterra, pendule, Lorenz
- `src/demo.py` : script qui trace le portrait de phase et l’ordre de convergence

## Pourquoi ce projet ?

Quand on apprend les EDO, on a souvent l’impression que les méthodes numériques sont “juste” des formules. En les testant sur des exemples concrets, on voit vite que le choix de la méthode et du pas influence beaucoup la qualité du résultat.

Ce projet m’a aidé à visualiser cette idée :

- Euler est simple et facile à coder, mais souvent moins précis
- RK4 donne des résultats beaucoup plus stables sur les mêmes problèmes
- le pas de discrétisation a un effet énorme sur la précision
- la visualisation aide énormément à comprendre ce qui se passe

## Les systèmes étudiés

- Lotka-Volterra : modèle proies-prédateurs
- Pendule simple : oscillations non linéaires
- Système de Lorenz : exemple plus complexe, très sensible aux conditions initiales

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux / macOS
pip install -r requirements.txt
```

## Utilisation

```bash
python src/demo.py
```

Le script affiche une figure avec :

- un portrait de phase du système de Lotka-Volterra
- une courbe de convergence pour la méthode d’Euler et RK4

## Ce que j’ai appris

- Il faut être très prudent avec le choix du pas
- une méthode plus “forte” n’est pas toujours nécessaire pour un petit système simple, mais elle devient utile dès qu’on s’approche de dynamiques plus sensibles
- comparer plusieurs méthodes côte à côte donne une intuition toute différente de la lecture d’une formule isolée
- le fait de visualiser les trajectoires rend les notions de stabilité et d’erreur beaucoup plus concrètes

## Prochaines étapes

- [ ] comparer ces méthodes avec `scipy.integrate.solve_ivp`
- [ ] mesurer l’erreur et le coût de calcul
- [ ] ajouter une interface interactive
- [ ] générer des animations ou GIF des simulations

## Licence

MIT

## Journal rapide

J’ai commencé par coder la méthode d’Euler pour comprendre le principe de base. Ensuite j’ai ajouté RK4 pour voir l’effet de la précision supplémentaire. Le moment où les trajectoires ont commencé à se “comporter” correctement sur Lotka-Volterra a été le point clé : c’était la première fois que le code ne semblait plus abstrait, mais bien relié à un système physique réel.

C’est un projet simple, mais il m’a permis de comprendre concrètement ce que signifie résoudre numériquement une EDO. J'espère qu'il en sera de même pour vous aussi 😁.
