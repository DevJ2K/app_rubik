import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def draw_face_front(ax, cube_face: list[list[str]], colors: dict, spacing: float = 0.5):
	CONSTANTE = 0
	for y in range(len(cube_face)):
		for x in range(len(cube_face[y])):
			vertices = [
				[x + spacing, CONSTANTE, 3 - y - spacing],
				[x + 1, CONSTANTE, 3 - y - spacing],
				[x + 1, CONSTANTE, 3 - y - 1],
				[x + spacing, CONSTANTE, 3 - y - 1],
			]
			face = Poly3DCollection([vertices], color=colors[cube_face[y][x]], alpha=1)
			ax.add_collection3d(face)

def draw_face_back(ax, cube_face: list[list[str]], colors: dict, spacing: float = 0.5):
	CONSTANTE = 3 + spacing
	for y in range(len(cube_face)):
		for x in range(len(cube_face[y])):
			vertices = [
				[x + spacing, CONSTANTE, 3 - y - spacing],
				[x + 1, CONSTANTE, 3 - y - spacing],
				[x + 1, CONSTANTE, 3 - y - 1],
				[x + spacing, CONSTANTE, 3 - y - 1],
			]
			face = Poly3DCollection([vertices], color=colors[cube_face[y][x]], alpha=1)
			ax.add_collection3d(face)

def draw_face_up(ax, cube_face: list[list[str]], colors: dict, spacing: float = 0.5):
	CONSTANTE = 3 + spacing
	for y in range(len(cube_face)):
		for x in range(len(cube_face[y])):
			vertices = [
				[x + spacing, 3 - y - spacing, CONSTANTE],
				[x + 1, 3 - y - spacing, CONSTANTE],
				[x + 1, 3 - y - 1, CONSTANTE],
				[x + spacing, 3 - y - 1, CONSTANTE],
			]
			face = Poly3DCollection([vertices], color=colors[cube_face[y][x]], alpha=1)
			ax.add_collection3d(face)

def draw_face_down(ax, cube_face: list[list[str]], colors: dict, spacing: float = 0.5):
	CONSTANTE = 0 - spacing
	for y in range(len(cube_face)):
		for x in range(len(cube_face[y])):
			vertices = [
				[x + spacing, 3 - y - spacing, CONSTANTE],
				[x + 1, 3 - y - spacing, CONSTANTE],
				[x + 1, 3 - y - 1, CONSTANTE],
				[x + spacing, 3 - y - 1, CONSTANTE],
			]
			face = Poly3DCollection([vertices], color=colors[cube_face[y][x]], alpha=1)
			ax.add_collection3d(face)


def draw_face_left(ax, cube_face: list[list[str]], colors: dict, spacing: float = 0.5):
	CONSTANTE = 0 - spacing
	for y in range(len(cube_face)):
		for x in range(len(cube_face[y])):
			vertices = [
				[CONSTANTE, x + spacing, 3 - y - spacing],
				[CONSTANTE, x + 1, 3 - y - spacing],
				[CONSTANTE, x + 1, 3 - y - 1],
				[CONSTANTE, x + spacing, 3 - y - 1],
			]
			face = Poly3DCollection([vertices], color=colors[cube_face[y][x]], alpha=1)
			ax.add_collection3d(face)

def draw_face_right(ax, cube_face: list[list[str]], colors: dict, spacing: float = 0.5):
	CONSTANTE = 3 + spacing
	for y in range(len(cube_face)):
		for x in range(len(cube_face[y])):
			vertices = [
				[CONSTANTE, x + spacing, 3 - y - spacing],
				[CONSTANTE, x + 1, 3 - y - spacing],
				[CONSTANTE, x + 1, 3 - y - 1],
				[CONSTANTE, x + spacing, 3 - y - 1],
			]
			face = Poly3DCollection([vertices], color=colors[cube_face[y][x]], alpha=1)
			ax.add_collection3d(face)




def visualize_cube_3D(
		face_up: list[list[str]],
		face_down: list[list[str]],
		face_front: list[list[str]],
		face_back: list[list[str]],
		face_left: list[list[str]],
		face_right: list[list[str]],
		window_title: str = "Rubik Visualizer",
		colors: dict = {
			'1': 'white',  # face 1
			'2': 'yellow', # face 2
			'3': 'blue',   # face 3
			'4': 'green',  # face 4
			'5': 'red',    # face 5
			'6': 'orange', # face 6
		},
		spacing: float = 0.05
):

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	draw_face_up(ax, face_up, colors, spacing);
	draw_face_down(ax, face_down, colors, spacing);
	draw_face_front(ax, face_front, colors, spacing);
	draw_face_back(ax, face_back, colors, spacing);
	draw_face_left(ax, face_left, colors, spacing);
	draw_face_right(ax, face_right, colors, spacing);

	# Définir les limites des axes
	ax.set_xlim(0, 3.1)
	ax.set_ylim(0, 3.1)
	ax.set_zlim(0, 3.1)

	# Étiquettes des axes
	ax.set_xlabel('Axe X')
	ax.set_ylabel('Axe Y')
	ax.set_zlabel('Axe Z')

	fig.canvas.manager.set_window_title(window_title)
	fig.set_facecolor('black')
	ax.set_facecolor('black')

	ax.grid(False)
	ax.xaxis.pane.fill = False
	ax.yaxis.pane.fill = False
	ax.zaxis.pane.fill = False


	plt.show()

