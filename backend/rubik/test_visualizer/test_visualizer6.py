import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

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
	CONSTANTE = 0
	for y in range(len(face1)):
		for x in range(len(face1[y])):
			vertices = [
				[x, CONSTANTE, 3 - y],
				[x + 1, CONSTANTE, 3 - y],
				[x + 1, CONSTANTE, 3 - y - 1],
				[x, CONSTANTE, 3 - y - 1],
			]

			face = Poly3DCollection([vertices], color=colors[face1[y][x]], alpha=1)
			ax.add_collection3d(face)

			# ax.plot_trisurf(
			# 	[x, x + 1, x + 1, x],
			# 	[y, y, y + 1, y + 1],
			# 	[1, 1, 1, 1],
			# 	color=colors[face1[y][x]]
			# 	)


			print(f"x: {x} | y: {y} | {face1[y][x]}")

draw_face_1()

# Définir les limites des axes
ax.set_xlim(0, 3)
ax.set_ylim(0, 3)
ax.set_zlim(0, 3)

# Étiquettes des axes
ax.set_xlabel('Axe X')
ax.set_ylabel('Axe Y')
ax.set_zlabel('Axe Z')

# Affichage
plt.show()
