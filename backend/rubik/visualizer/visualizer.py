import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Création de la figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

SPACING = 0.03

colors = {
	'1': 'white',  # face 1
	'2': 'yellow', # face 2
	'3': 'blue',   # face 3
	'4': 'green',  # face 4
	'5': 'red',    # face 5
	'6': 'orange', # face 6
}

face_up = [
	['1', '1', '1'],
	['1', '1', '1'],
	['1', '1', '1']
]
face_down = [
	['2', '2', '2'],
	['2', '2', '2'],
	['2', '2', '2']
]
face_front = [
	['3', '3', '3'],
	['3', '3', '3'],
	['3', '3', '3']
]
face_back = [
	['4', '4', '4'],
	['4', '4', '4'],
	['4', '4', '4']
]
face_left = [
	['5', '5', '5'],
	['5', '5', '5'],
	['5', '5', '5']
]
face_right = [
	['6', '6', '6'],
	['6', '6', '6'],
	['6', '6', '6']
]




# Définir les coordonnées de la face
x = [1, 2, 2, 1]
y = [1, 1, 2, 2]
z = [1, 1, 1, 1]  # Les z sont constants pour une face plane

print(face_front)

def draw_face_front():
	CONSTANTE = 0
	for y in range(len(face_front)):
		for x in range(len(face_front[y])):
			vertices = [
				[x + SPACING, CONSTANTE, 3 - y - SPACING],
				[x + 1, CONSTANTE, 3 - y - SPACING],
				[x + 1, CONSTANTE, 3 - y - 1],
				[x + SPACING, CONSTANTE, 3 - y - 1],
			]
			face = Poly3DCollection([vertices], color=colors[face_front[y][x]], alpha=1)
			ax.add_collection3d(face)
			print(f"x: {x} | y: {y} | {face_front[y][x]}")

def draw_face_back():
	CONSTANTE = 3 + SPACING
	for y in range(len(face_back)):
		for x in range(len(face_back[y])):
			vertices = [
				[x + SPACING, CONSTANTE, 3 - y - SPACING],
				[x + 1, CONSTANTE, 3 - y - SPACING],
				[x + 1, CONSTANTE, 3 - y - 1],
				[x + SPACING, CONSTANTE, 3 - y - 1],
			]
			face = Poly3DCollection([vertices], color=colors[face_back[y][x]], alpha=1)
			ax.add_collection3d(face)
			print(f"x: {x} | y: {y} | {face_back[y][x]}")

def draw_face_up():
	CONSTANTE = 3 + SPACING
	for y in range(len(face_up)):
		for x in range(len(face_up[y])):
			vertices = [
				[x + SPACING, 3 - y - SPACING, CONSTANTE],
				[x + 1, 3 - y - SPACING, CONSTANTE],
				[x + 1, 3 - y - 1, CONSTANTE],
				[x + SPACING, 3 - y - 1, CONSTANTE],
			]
			face = Poly3DCollection([vertices], color=colors[face_up[y][x]], alpha=1)
			ax.add_collection3d(face)
			print(f"x: {x} | y: {y} | {face_up[y][x]}")

def draw_face_down():
	CONSTANTE = 0 - SPACING
	for y in range(len(face_down)):
		for x in range(len(face_down[y])):
			vertices = [
				[x + SPACING, 3 - y - SPACING, CONSTANTE],
				[x + 1, 3 - y - SPACING, CONSTANTE],
				[x + 1, 3 - y - 1, CONSTANTE],
				[x + SPACING, 3 - y - 1, CONSTANTE],
			]
			face = Poly3DCollection([vertices], color=colors[face_down[y][x]], alpha=1)
			ax.add_collection3d(face)
			print(f"x: {x} | y: {y} | {face_down[y][x]}")


def draw_face_left():
	CONSTANTE = 0 - SPACING
	for y in range(len(face_left)):
		for x in range(len(face_left[y])):
			vertices = [
				[CONSTANTE, x + SPACING, 3 - y - SPACING],
				[CONSTANTE, x + 1, 3 - y - SPACING],
				[CONSTANTE, x + 1, 3 - y - 1],
				[CONSTANTE, x + SPACING, 3 - y - 1],
			]
			face = Poly3DCollection([vertices], color=colors[face_left[y][x]], alpha=1)
			ax.add_collection3d(face)
			print(f"x: {x} | y: {y} | {face_left[y][x]}")

def draw_face_right():
	CONSTANTE = 3 + SPACING
	for y in range(len(face_right)):
		for x in range(len(face_right[y])):
			vertices = [
				[CONSTANTE, x + SPACING, 3 - y - SPACING],
				[CONSTANTE, x + 1, 3 - y - SPACING],
				[CONSTANTE, x + 1, 3 - y - 1],
				[CONSTANTE, x + SPACING, 3 - y - 1],
			]
			face = Poly3DCollection([vertices], color=colors[face_right[y][x]], alpha=1)
			ax.add_collection3d(face)
			print(f"x: {x} | y: {y} | {face_right[y][x]}")

draw_face_front()
draw_face_back()

draw_face_up()
draw_face_down()

draw_face_left()
draw_face_right()

# Définir les limites des axes
ax.set_xlim(0, 3.1)
ax.set_ylim(0, 3.1)
ax.set_zlim(0, 3.1)

# Étiquettes des axes
ax.set_xlabel('Axe X')
ax.set_ylabel('Axe Y')
ax.set_zlabel('Axe Z')

fig.canvas.manager.set_window_title("Rubik Visualizer")
fig.set_facecolor('black')
ax.set_facecolor('black')

ax.grid(False)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# Affichage
plt.show()
