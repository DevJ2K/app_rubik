import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Création de la figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Définir les coordonnées de la face
x = [1, 2, 2, 1]
y = [1, 1, 2, 2]
z = [1, 1, 1, 1]  # Les z sont constants pour une face plane

# Tracer la face
ax.plot_trisurf(x, y, z, color='#ff00ff', alpha=0.7)

# Étiquettes des axes
ax.set_xlabel('Axe X')
ax.set_ylabel('Axe Y')
ax.set_zlabel('Axe Z')

# Affichage
plt.show()
