import matplotlib.pyplot as plt
import numpy as np

# Données
data = np.random.randn(1000)

# Création de la figure et de l'axe
fig, ax = plt.subplots()

# Tracer l'histogramme
ax.hist(data, bins=30)

# Ajouter des labels et un titre
ax.set(xlabel='value', ylabel='frequency', title='Histogram')

# Afficher le graphique
plt.show()
