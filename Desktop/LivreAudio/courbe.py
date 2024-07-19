import matplotlib.pyplot as plt
import numpy as np
# Données
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Création de la figure et de l'axe
fig, ax = plt.subplots()

# Tracer les courbes avec des styles différents
ax.plot(x, y1, label='sin(x)', color='blue', linestyle='-', linewidth=2)
ax.plot(x, y2, label='cos(x)', color='red', linestyle='--', linewidth=2)

# Ajouter des labels, un titre, et une légende
ax.set(xlabel='x', ylabel='y', title='Sin and Cos functions')
ax.legend()

# Afficher le graphique
plt.show()
