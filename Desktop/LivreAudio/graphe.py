import matplotlib.pyplot as plt
import numpy as np

# Données
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Création de la figure et de l'axe
fig, ax = plt.subplots()

# Tracer la courbe
ax.plot(x, y)

# Ajouter des labels et un titre
ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')

# Ajouter une grille
ax.grid()

# Afficher le graphique
plt.show()
