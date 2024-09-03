import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Création de la figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

colors = {
	'1': 'white',  # face 1
	'2': 'yellow', # face 2
	'3': 'blue',   # face 3
	'4': 'green',  # face 4
	'5': 'red',    # face 5
	'6': 'orange', # face 6
}

face1 = [
		['1', '2', '3'],
		['4', '1', '5'],
		['6', '2', '6'],
	]
# Définir les coordonnées de la face
x = [1, 2, 2, 1]
y = [1, 1, 2, 2]
z = [1, 1, 1, 1]  # Les z sont constants pour une face plane

print(face1)

def draw_face_1():
	for y in range(len(face1)):
		for x in range(len(face1[y])):
			ax.plot_trisurf(
				[x, x + 1, x + 1, x],
				[y, y, y + 1, y + 1],
				[1, 1, 1, 1],
				color=colors[face1[y][x]]
				)


			print(f"x: {x} | y: {y} | {face1[y][x]}")

# draw_face_1()

x = [1, 2, 2, 1]
y = [1, 1, 1, 1]  # y est constant pour une face verticale
z = [1, 1, 2, 2]

# Tracer la face
ax.plot_trisurf(x, y, z, color='red', alpha=0.7)

# Étiquettes des axes
ax.set_xlabel('Axe X')
ax.set_ylabel('Axe Y')
ax.set_zlabel('Axe Z')

# Affichage
plt.show()
