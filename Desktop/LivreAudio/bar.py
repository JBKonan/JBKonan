import matplotlib.pyplot as plt
import numpy as np

# Données
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 35, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # L'emplacement des labels
width = 0.35  # La largeur des barres

# Création de la figure et de l'axe
fig, ax = plt.subplots()

# Tracer les barres
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Ajouter des labels, un titre, et une légende
ax.set_xlabel('Groups')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Afficher le graphique
plt.show()
