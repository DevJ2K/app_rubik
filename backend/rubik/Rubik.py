from visualizers.rubik_visualizer import visualize_cube_3D
from RubikMoves import RubikMoves
from ErrorManager import *
from parser import check_notation
from PruningTable import PruningTable
import copy
import random


from apply_rubik_moves import move_up, move_down, move_back, move_front, move_left, move_right

# SOLVE RUBIK
[
	# self.cube_up: list[list[str]] = [
	# 	['1', '1', '1'],
	# 	['1', '1', '1'],
	# 	['1', '1', '1'],
	# ]
	# self.cube_down: list[list[str]] = [
	# 	['2', '2', '2'],
	# 	['2', '2', '2'],
	# 	['2', '2', '2'],
	# ]
	# self.cube_front: list[list[str]] = [
	# 	['3', '3', '3'],
	# 	['3', '3', '3'],
	# 	['3', '3', '3'],
	# ]
	# self.cube_back: list[list[str]] = [
	# 	['4', '4', '4'],
	# 	['4', '4', '4'],
	# 	['4', '4', '4'],
	# ]
	# self.cube_left: list[list[str]] = [
	# 	['5', '5', '5'],
	# 	['5', '5', '5'],
	# 	['5', '5', '5'],
	# ]
	# self.cube_right: list[list[str]] = [
	# 	['6', '6', '6'],
	# 	['6', '6', '6'],
	# 	['6', '6', '6'],
	# ]
]


class Rubik:
	"""The class to solve an rubik cube"""
	def __init__(self, cube: list[list[list[str]]] = None, sequences: str = None) -> None:
		self.COLORS = {
			'W': 'white',  # face 1 (up)
			'Y': 'yellow', # face 2 (bottom)
			'B': 'blue',   # face 3 (back)
			'G': 'green',  # face 4 (front)
			'R': 'red',	# face 5 (right)
			'O': 'orange', # face 6 (left)
		}
		self.edgePos = [i for i in range(12)]
		self.cornerPos = [i for i in range(8)]
		self.edgeOrt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		self.cornerOrt = [0, 0, 0, 0, 0, 0, 0, 0]
		self.movesList = ""

		# self.cube = [[3] * 3]
		self.cube_up: list[list[str]] = [(['W' for _ in range(3)]) for _x in range(3)]
		self.cube_down: list[list[str]] = [(['Y' for _ in range(3)]) for _x in range(3)]
		self.cube_front: list[list[str]] = [(['G' for _ in range(3)]) for _x in range(3)]
		self.cube_back: list[list[str]] = [(['B' for _ in range(3)]) for _x in range(3)]
		self.cube_left: list[list[str]] = [(['O' for _ in range(3)]) for _x in range(3)]
		self.cube_right: list[list[str]] = [(['R' for _ in range(3)]) for _x in range(3)]


	def get_cube(self) -> list[list[list[str]]]:
		return [
			self.cube_up,
			self.cube_down,
			self.cube_front,
			self.cube_back,
			self.cube_left,
			self.cube_right
		]

	def check_valid_cube(self) -> bool:
		pass

	def apply_move(self, move: str) -> None:
		"""
		This method applies a specified move to the Rubik's cube,
		updating its state based on the move type.
		Depending on the letter in the move string ('U', 'D', 'F', 'B', 'L', 'R'),
		it performs the corresponding face rotation.

		Parameters:
		move (str): A string representing the move to apply.
					Valid values include 'U', 'D', 
					'F', 'B', 'L' and 'R'. If the move contains a prime symbol ('), 
					the rotation is counterclockwise.

		Returns:
		None: The cube's state is updated in place.
		If the move is invalid, an error message is printed.
		"""
		result = self.get_cube()
		if 'U' in move:
			result = move_up(self.get_cube(), move)
		elif 'D' in move:
			result = move_down(self.get_cube(), move)
		elif 'F' in move:
			result = move_front(self.get_cube(), move)
		elif 'B' in move:
			result = move_back(self.get_cube(), move)
		elif 'L' in move:
			result = move_left(self.get_cube(), move)
		elif 'R' in move:
			result = move_right(self.get_cube(), move)
		else:
			print("Undefined") #Raise

		self.cube_up,self.cube_down,self.cube_front,self.cube_back,self.cube_left,self.cube_right = result
		# self.visualize_cube(window_title=f"MOVE : {move}")

	def applyMultipleMoves(self, move: str, amount: int):
		result = self.get_cube()
		for _ in range(amount):
			if 'U' in move:
				result = move_up(self.get_cube(), move)
				self.cornerOrt[0], self.cornerOrt[1], self.cornerOrt[4], self.cornerOrt[5] = \
				self.cornerOrt[1], self.cornerOrt[4], self.cornerOrt[5], self.cornerOrt[0]
				self.edgeOrt[2], self.edgeOrt[3], self.edgeOrt[0], self.edgeOrt[1] = \
				self.edgeOrt[3], self.edgeOrt[0], self.edgeOrt[1], self.edgeOrt[2]

				self.cornerPos[0], self.cornerPos[1], self.cornerPos[4], self.cornerPos[5] = \
				self.cornerPos[1], self.cornerPos[4], self.cornerPos[5], self.cornerPos[0]
				self.edgePos[2], self.edgePos[3], self.edgePos[0], self.edgePos[1] = \
				self.edgePos[3], self.edgePos[0], self.edgePos[1], self.edgePos[2]
			elif 'D' in move:
				result = move_down(self.get_cube(), move)
				self.cornerOrt[3], self.cornerOrt[2], self.cornerOrt[7], self.cornerOrt[6] = \
				self.cornerOrt[2], self.cornerOrt[7], self.cornerOrt[6], self.cornerOrt[3]
				self.edgeOrt[4], self.edgeOrt[7], self.edgeOrt[6], self.edgeOrt[5] = \
				self.edgeOrt[7], self.edgeOrt[6], self.edgeOrt[5], self.edgeOrt[4]

				self.cornerPos[3], self.cornerPos[2], self.cornerPos[7], self.cornerPos[6] = \
				self.cornerPos[2], self.cornerPos[7], self.cornerPos[6], self.cornerPos[3]
				self.edgePos[4], self.edgePos[7], self.edgePos[6], self.edgePos[5] = \
				self.edgePos[7], self.edgePos[6], self.edgePos[5], self.edgePos[4]
			elif 'F' in move:
				result = move_front(self.get_cube(), move)
				self.cornerOrt[0], self.cornerOrt[5], self.cornerOrt[2], self.cornerOrt[3] = \
				(2 + self.cornerOrt[5]) % 3, (1 + self.cornerOrt[2]) % 3, (2 + self.cornerOrt[3]) % 3, (1 + self.cornerOrt[0]) % 3
				self.edgeOrt[0], self.edgeOrt[11], self.edgeOrt[4], self.edgeOrt[8] = \
				1 - self.edgeOrt[11], 1 - self.edgeOrt[4], 1 - self.edgeOrt[8], 1 - self.edgeOrt[0]

				self.cornerPos[0], self.cornerPos[5], self.cornerPos[2], self.cornerPos[3] = \
				self.cornerPos[5],self.cornerPos[2],self.cornerPos[3],self.cornerPos[0]
				self.edgePos[0], self.edgePos[11], self.edgePos[4], self.edgePos[8] = \
				self.edgePos[11], self.edgePos[4], self.edgePos[8], self.edgePos[0]
			elif 'B' in move:
				result = move_back(self.get_cube(), move)
				self.cornerOrt[4], self.cornerOrt[1], self.cornerOrt[6], self.cornerOrt[7] = \
				(2 + self.cornerOrt[1]) % 3, (1 + self.cornerOrt[6]) % 3, (2 + self.cornerOrt[7]) % 3, (1 + self.cornerOrt[4]) % 3
				self.edgeOrt[9], self.edgeOrt[6], self.edgeOrt[10], self.edgeOrt[2] = \
				1 - self.edgeOrt[6], 1 - self.edgeOrt[10], 1 - self.edgeOrt[2], 1 - self.edgeOrt[9]

				self.cornerPos[4], self.cornerPos[1], self.cornerPos[6], self.cornerPos[7] = \
				self.cornerPos[1], self.cornerPos[6], self.cornerPos[7], self.cornerPos[4]
				self.edgePos[9], self.edgePos[6], self.edgePos[10], self.edgePos[2] = \
				self.edgePos[6], self.edgePos[10], self.edgePos[2], self.edgePos[9]
			elif 'L' in move:
				result = move_left(self.get_cube(), move)
				self.cornerOrt[2], self.cornerOrt[5], self.cornerOrt[4], self.cornerOrt[7] = \
				(1 + self.cornerOrt[5]) % 3, (2 + self.cornerOrt[4]) % 3, (1 + self.cornerOrt[7]) % 3, (2 + self.cornerOrt[2]) % 3
				self.edgeOrt[10], self.edgeOrt[7], self.edgeOrt[11], self.edgeOrt[3] = \
				self.edgeOrt[7], self.edgeOrt[11], self.edgeOrt[3], self.edgeOrt[10]

				self.cornerPos[2], self.cornerPos[5], self.cornerPos[4], self.cornerPos[7] = \
				self.cornerPos[5], self.cornerPos[4], self.cornerPos[7], self.cornerPos[2]
				self.edgePos[10], self.edgePos[7], self.edgePos[11], self.edgePos[3] = \
				self.edgePos[7], self.edgePos[11], self.edgePos[3], self.edgePos[10]
			elif 'R' in move:
				result = move_right(self.get_cube(), move)
				self.cornerOrt[0], self.cornerOrt[3], self.cornerOrt[6], self.cornerOrt[1] = \
				(1 + self.cornerOrt[3]) % 3, (2 + self.cornerOrt[6]) % 3, (1 + self.cornerOrt[1]) % 3, (2 + self.cornerOrt[0]) % 3
				self.edgeOrt[8], self.edgeOrt[5], self.edgeOrt[9], self.edgeOrt[1] = \
				self.edgeOrt[5], self.edgeOrt[9], self.edgeOrt[1], self.edgeOrt[8]

				self.cornerPos[0], self.cornerPos[3], self.cornerPos[6], self.cornerPos[1] = \
				self.cornerPos[3], self.cornerPos[6], self.cornerPos[1], self.cornerPos[0]
				self.edgePos[8], self.edgePos[5], self.edgePos[9], self.edgePos[1] = \
				self.edgePos[5], self.edgePos[9], self.edgePos[1], self.edgePos[8]
			else:
				print("Undefined") #Raise
			self.cube_up,self.cube_down,self.cube_front,self.cube_back,self.cube_left,self.cube_right = result


	def apply_sequences(self, sequences: str) -> None:
		"""Apply sequences to the rubik cube.

		Args:
			sequences (str): Sequences to apply to the rubik cube.
		"""
		sequences_list_str = sequences.split()
		for sequence_str in sequences_list_str:
			if check_notation(sequence_str) == False:
				raise NotationError(f"{sequence_str} is not a valid notation.")

		sequences_list_not_join = [RubikMoves(notation).sequences for notation in sequences_list_str]
		sequences_list = []
		for expend_sequences in sequences_list_not_join:
			sequences_list += expend_sequences
		print(sequences_list)
		for move in sequences_list:
			self.apply_move(move)
		pass

	def visualize_cube(self, window_title: str = "Rubik Visualizer", spacing: float = 0.04) -> None:
		"""Visualize cube with mathplotlib.
		"""
		visualize_cube_3D(
			self.cube_up,
			self.cube_down,
			self.cube_front,
			self.cube_back,
			self.cube_left,
			self.cube_right,
			window_title,
			self.COLORS,
			spacing
		)
		pass

	def setedgeOrt(self) -> list[int]:
		"""
		Obtient les orientations des arêtes du Rubik's Cube.

		Calcule les orientations des arêtes en examinant les couleurs des stickers adjacents. Chaque orientation est
		déterminée par la couleur des stickers voisins.

		Retourne:
		- list[int]: Liste de 12 entiers pour les orientations des arêtes (0 ou 1).

		Notes:
		- Utilise `self.get_cube()` pour accéder aux couleurs des stickers.
		"""
		cube_up,cube_down,cube_front,cube_back,cube_left,cube_right = self.get_cube()
		edges = [
			(cube_up[2][1], cube_front[0][1]),
			(cube_up[1][2], cube_right[0][1]),
			(cube_up[0][1], cube_back[0][1]),
			(cube_up[1][0], cube_left[0][1]),
			(cube_down[0][1], cube_front[2][1]),
			(cube_down[1][2], cube_right[2][1]),
			(cube_down[2][1], cube_back[2][1]),
			(cube_down[1][0], cube_left[2][1]),
			(cube_front[1][2], cube_right[1][0]),
			(cube_back[1][2], cube_right[1][2]),
			(cube_back[1][0], cube_left[1][0]),
			(cube_front[1][0], cube_left[1][2]),
		]
		self.edgeOrt = []
		for edge in edges:
			if edge[0] in ['W', 'Y'] or edge[1] in ['W', 'Y']:
				self.edgeOrt.append(0)
			else:
				self.edgeOrt.append(1)
		return self.edgeOrt
	
	def setcornerOrt(self) -> list[int]:
		"""
		Obtient les orientations des coins du Rubik's Cube.

		Calcule les orientations des coins en examinant les couleurs des stickers adjacents. Chaque orientation est
		déterminée par la couleur des stickers voisins.

		Retourne:
		- list[int]: Liste de 8 entiers pour les orientations des coins (0, 1 ou 2).

		Notes:
		- Utilise `self.get_cube()` pour accéder aux couleurs des stickers.
		"""
		cube_up,cube_down,cube_front,cube_back,cube_left,cube_right = self.get_cube()
		corners = [
			(cube_up[2][2], cube_right[0][0], cube_front[0][2]),
			(cube_up[0][2], cube_right[0][2], cube_back[0][2]),
			(cube_down[0][0], cube_left[2][2], cube_front[2][0]),
			(cube_down[0][2], cube_right[2][2], cube_front[2][2]),
			(cube_up[0][0], cube_left[0][2], cube_back[0][0]),
			(cube_up[2][0], cube_left[0][0], cube_front[0][0]),
			(cube_down[2][2], cube_right[2][0], cube_back[2][2]),
			(cube_down[2][0], cube_left[2][0], cube_back[2][0])
		]
		self.cornerOrt = []
		for corner in corners:
			if corner[0] in ['W', 'Y']:
				self.cornerOrt.append(0)
			elif corner[1] in ['W', 'Y']:
				self.cornerOrt.append(1)
			else:
				self.cornerOrt.append(2)
		return self.cornerOrt
	
	def getedgeOrtState(self) -> int:
		"""
		Obtient l'état d'orientation des arêtes du Rubik's Cube.

		Calcule l'état d'orientation des arêtes en convertissant les orientations en une valeur entière codée en binaire.

		Retourne:
		- int: Entier représentant l'état d'orientation des arêtes, avec chaque bit indiquant l'orientation (0 ou 1).

		Notes:
		- Utilise `self.getedgeOrt()` pour obtenir les orientations des arêtes.
		"""
		edgeOrt = self.getedgeOrt()
		state = 0
		for i in range(11):
			state = (state << 1) | edgeOrt[i]
		return state
	
	def getcornerOrtState(self) -> int:
		"""
		Obtient l'état d'orientation des coins du Rubik's Cube.

		Calcule l'état d'orientation des coins en convertissant les orientations en une valeur entière codée en base 3.
		
		Retourne:
		- int: Entier représentant l'état d'orientation des coins, avec chaque orientation codée comme 0 (aucune rotation),
		1 (120°), ou 2 (240°).

		Notes:
		- Utilise `self.getcornerOrt()` pour obtenir les orientations des coins.
		"""
		cornerOrt = self.getcornerOrt()
		state = 0
		for i in range(7):
			state = state * 3 + cornerOrt[i]
		return state


	def setedgeOrtState(self, state) -> None:
		"""
		Définit l'état d'orientation des arêtes du Rubik's Cube.

		Ajuste l'orientation des arêtes en fonction d'un entier d'état codé en binaire, où chaque bit représente
		l'orientation d'une arête (0 pour non-orienté, 1 pour orienté).

		Paramètres:
		- state (int): Entier représentant l'état d'orientation des arêtes.

		Retourne:
		- None: Modifie directement l'état interne du cube sans retourner de valeur.
		"""
		cube = self.get_cube()
		edges = [
			(0, 0, 1, 3, 0, 1), # 0: up, 1: down, 2: front, 3: back, 4: left, 5: right 
			(0, 1, 2, 5, 0, 1),
			(0, 2, 1, 2, 0, 1),
			(0, 1, 0, 4, 0, 1),
			(1, 0, 1, 2, 2, 1),
			(1, 1, 2, 5, 2, 1),
			(1, 2, 1, 3, 2, 1),
			(1, 1, 0, 4, 2, 1),
			(2, 1, 0, 4, 1, 2),
			(2, 1, 2, 5, 1, 0),
			(3, 1, 0, 4, 1, 0),
			(3, 1, 2, 5, 1, 2)
		]

		for i, edge in enumerate(edges):
			face1, x1, y1, face2, x2, y2 = edge

			orientation = (state >> (11 - i)) & 1
			if orientation == 1:
				cube[face1][x1][y1], cube[face2][x2][y2] = cube[face2][x2][y2], cube[face1][x1][y1]

	def setcornerOrtState(self, state):
		"""
		Définit l'état d'orientation des coins du Rubik's Cube.

		La méthode ajuste l'orientation des coins en fonction d'un entier d'état, codé en base 3. Chaque orientation
		possible pour un coin est représentée par 0 (aucun changement), 1 (rotation de 120°), ou 2 (rotation de 240°).

		Paramètres:
		- state (int): Entier représentant l'état d'orientation des coins.

		Retourne:
		- None: Modifie directement l'état interne du cube sans retourner de valeur.
		"""
		cube = self.get_cube()
		corners = [
			(0, 0, 0, 4, 0, 2, 3, 0, 0), # 0: up, 1: down, 2: front, 3: back, 4: left, 5: right 
			(0, 0, 2, 5, 0, 0, 3, 0, 2),
			(0, 2, 0, 4, 0, 0, 2, 0, 0),
			(0, 2, 2, 5, 0, 2, 2, 0, 2),
			(1, 0, 0, 4, 2, 0, 2, 2, 0),
			(1, 0, 2, 5, 2, 2, 2, 2, 2),
			(1, 2, 0, 4, 2, 2, 3, 2, 0),
			(1, 2, 2, 5, 2, 0, 3, 2, 2) 
		]

		for _, corner in enumerate(corners[:-1]):
			face1, x1, y1, face2, x2, y2, face3, x3, y3 = corner

			orientation = state % 3
			state //= 3

			if orientation == 1:
				(
					cube[face1][x1][y1], cube[face2][x2][y2], cube[face3][x3][y3]
				) = (
					cube[face3][x3][y3], cube[face1][x1][y1], cube[face2][x2][y2]
				)
			elif orientation == 2:
				(
					cube[face1][x1][y1], cube[face2][x2][y2], cube[face3][x3][y3]
				) = (
					cube[face2][x2][y2], cube[face3][x3][y3], cube[face1][x1][y1]
				)


	def isOrientationSolved(self) -> bool:
		"""
		Vérifie si l'orientation du Rubik's Cube est résolue.

		La méthode vérifie si toutes les faces du cube ont une couleur uniforme en comparant chaque case au centre 
		de chaque face. Si toutes les cases d'une face ont la même couleur que le centre, la face est considérée comme 
		résolue.

		Retourne:
		- bool: True si toutes les faces sont uniformes, sinon False.

		Notes:
		- `self.get_cube()` doit retourner une représentation du cube en tant que liste 3D.
		"""
		# cube = self.get_cube()
		# for face in cube:
		# 	center_color = face[1][1]
		# 	for row in face:
		# 		for color in row:
		# 			if color != center_color:
		# 				return False
		# return True
		solvededgeOrt = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
		solvedcornerOrt = [0] * 8

		edgeOrt = self.getedgeOrt()
		cornerOrt = self.getcornerOrt()
		if edgeOrt != solvededgeOrt:
			return False
		if cornerOrt != solvedcornerOrt:
			return False
		return True

	def isSolved(self) -> bool:
		cube = self.get_cube()
		for face in cube:
			center_color = face[1][1]
			for row in face:
				for color in row:
					if color != center_color:
						return False
		return True

	def shuffle(self):
		# U D R2 L2 F2 B2
		# U D L R R B F
		self.applyMultipleMoves("U", 1)
		self.applyMultipleMoves("D", 1)
		self.applyMultipleMoves("L", 1)
		self.applyMultipleMoves("R", 1)
		self.applyMultipleMoves("R", 1)
		self.applyMultipleMoves("B", 1)
		self.applyMultipleMoves("F", 1)

	def generateRandomCube(self, numMoves: int, mode: str) -> None:
		"""
		Génère un cube de Rubik mélangé en appliquant une séquence aléatoire de mouvements.

		La méthode génère une séquence de mouvements pour mélanger le cube, avec des mouvements basiques ou incluant
		des inverses selon le mode spécifié.

		Paramètres:
		- numMoves (int): Nombre de mouvements à appliquer pour mélanger le cube.
		- mode (str): 'hard' pour inclure les inverses, autre chose pour des mouvements sans inverses.

		Retourne:
		- None: Modifie l'état du cube en appliquant les mouvements générés sans retourner de valeur.

		Notes:
		- Utilise `generateRandomMoves` pour créer la séquence de mouvements.
		"""
		def generateRandomMoves(numMoves: int, mode: str) -> list[str]:
			"""
			Génère une liste de mouvements aléatoires basée sur le mode spécifié.

			Paramètres:
			- numMoves (int): Nombre de mouvements à générer.
			- mode (str): 'hard' pour inclure des inverses, autre chose pour des mouvements sans inverses.

			Retourne:
			- list[str]: Liste de mouvements aléatoires sous forme de chaînes de caractères.
			"""
			if mode == 'hard':
				moves = ["U", "U'", "D", "D'", "F", "F'", "B", "B'", "L", "L'", "R", "R'"]
			else:	
				moves = ["U", "D", "F", "B", "L", "R"]
			move_sequences = []
			for _ in range(numMoves):
				move = random.choice(moves)
				move_sequences.append(move)
			return move_sequences
		moves = generateRandomMoves(numMoves, mode)
		print('Moves: ', moves)
		for move in moves:
			self.apply_move(move)

	def solve(self) -> None:
		"""
		Résout le Rubik's Cube en deux phases.

		1. Phase 1: Utilise les tables de réduction d'orientation des arêtes et des coins pour trouver une solution
		intermédiaire (G1State) qui simplifie le cube en une configuration plus facile pour la phase 2.
		2. Phase 2: Utilise les tables de réduction de permutation des arêtes et des coins pour trouver la solution finale
		du cube.

		Les étapes incluent l'application des mouvements de Phase 1, la vérification si le cube est résolu, et l'application
		des mouvements de Phase 2. Affiche les séquences de mouvements et les états du cube à chaque étape.

		Retourne:
		- None: La méthode modifie directement l'état du cube et affiche les résultats sans retourner de valeur.
		"""
		from PruningTable import generateCornerPruningTable, generateEdgePruningTable, \
		generateEdgePruningTablePermutation, generateCornerPruningTablePermutation

		phase1EdgePruningTable = generateEdgePruningTable()
		# for i in range(2**11):
		# 	distance = phase1EdgePruningTable.getPruning(i)
		# 	# if distance != -1: print(distance)
		# 	print(distance)
		# print(len(phase1EdgePruningTable.table))
		phase1CornerPruningTable = generateCornerPruningTable()
		G1State = phase1Search(self, 12, phase1EdgePruningTable, phase1CornerPruningTable)
		print(G1State)
		self.visualize_cube()
		for move in G1State:
			self.apply_move(move)
		if self.isSolved():
			print("Solved before Phase 2, Sequences: ", G1State)
		self.visualize_cube()

		phase2EdgePruningTable = generateEdgePruningTablePermutation()
		phase2CornerPruningTable = generateCornerPruningTablePermutation()
		print('fin phase 2 pruningTable')
		# print(self.get_cube())
		result = phase2Search(self, 12, phase2EdgePruningTable, phase2CornerPruningTable)
		print(result)
		self.visualize_cube()

	def newSolver(self):
		output = []
		from Solver import Solver
		solver = Solver(self)
		print('Table loading done!')
		for phase in range(1, 4):
			print(f'Phase {phase}   {solver.phaseGoal[phase]}')
			while solver.getPhaseId(self, phase) != solver.phaseGoal[phase]:
				print(f'Phase {phase} {solver.phaseGoal[phase]}')
				path = solver.phaseTable[phase - 1][solver.getPhaseId(self, phase)]
				print(solver.getPhaseId(self, phase))
				print(path)
				if path == "":
					print(f'No solution')
					return 1
				pathList = [path[i:i+2] for i in range(0, len(path), 2)]
				if path != 'E':
					output.append(path)
					for move in pathList:
						face = move[0]
						try:
							nb = int(move[1])
						except ValueError:
							print(f'Format error')
							return 1
						self.applyMultipleMoves(face, nb)
		return output


def phase1Search(cube: Rubik, maxDepth: int, edgePruningTable: PruningTable, cornerPruningTable: PruningTable) -> list[str]:
	"""
	Recherche une solution pour la phase 1 du Rubik's Cube avec une recherche en profondeur (DFS). 
	Explore les mouvements jusqu'à une profondeur maximale pour résoudre l'orientation des arêtes.

	Paramètres:
	- cube (Rubik): État actuel du Rubik's Cube.
	- maxDepth (int): Profondeur maximale pour explorer les mouvements.
	- edgePruningTable (PruningTable): Table de réduction pour l'orientation des arêtes.
	- cornerPruningTable (PruningTable): Table de réduction pour l'orientation des coins.

	Retourne:
	- list[str]: Séquence de mouvements qui résout la phase 1, ou None si aucune solution n'est trouvée.
	"""
	def dfs(cubeState: Rubik, depth: int, path: list[str]) -> list[str]:
		"""
		Recherche en profondeur pour trouver une séquence de mouvements résolvant l'orientation des arêtes.

		Paramètres:
		- cubeState (Rubik): État actuel du Rubik's Cube.
		- depth (int): Profondeur actuelle.
		- maxDepth (int): Profondeur maximale.
		- path (list[str]): Séquence actuelle de mouvements.

		Retourne:
		- list[str]: Mouvements résolvant l'orientation, ou None si aucune solution n'est trouvée à cette profondeur.
		"""
		if cubeState.isOrientationSolved():
			print('here')
			return path
		if depth >= maxDepth:
			return None
		if edgePruningTable.getPruning(cubeState.getedgeOrtState()) > maxDepth - depth:
			return None
		if cornerPruningTable.getPruning(cubeState.getcornerOrtState()) > maxDepth - depth:
			return None
		
		moves = ["U", "U'", "D", "D'", "F", "F'", "B", "B'", "R", "R'", "L", "L'"]

		for move in moves:
			newCube: Rubik = copy.deepcopy(cubeState)
			newCube.apply_move(move)
			result = dfs(newCube, depth + 1, path + [move])
			if result is not None:
				return result
		return None
	
	# for depth in range(1, maxDepth + 1):
	# 	result = dfs(cube, 0, depth, [])
	# 	if result is not None:
	# 		return result
	# return None
	return dfs(cube, 0, [])

def phase2Search(cube: Rubik, maxDepth: int, edgePermutationTable: PruningTable, cornerPermutationTable: PruningTable) -> list[str]:
	"""
	Cette fonction recherche une solution pour la phase 2 de la résolution du Rubik's Cube en utilisant 
	une approche de recherche en profondeur (DFS). Elle explore les mouvements possibles jusqu'à une 
	profondeur maximale spécifiée pour trouver une séquence de mouvements qui résout la permutation des arêtes
	et des coins du Rubik's Cube.

	Paramètres:
	- cube (Rubik): L'état actuel du Rubik's Cube à résoudre.
	- maxDepth (int): La profondeur maximale jusqu'à laquelle explorer les mouvements.
	- edgePermutationTable (PruningTable): Table de réduction pour la permutation des arêtes. Permet d'éviter
	  l'exploration de certains états en fonction de la permutation des arêtes.
	- cornerPermutationTable (PruningTable): Table de réduction pour la permutation des coins. Permet d'éviter
	  l'exploration de certains états en fonction de la permutation des coins.

	Retourne:
	- list[str]: Une liste de mouvements sous forme de chaînes de caractères qui résout la phase 2, ou
	  None si aucune solution n'est trouvée dans la profondeur spécifiée.
	"""
	def dfs(cubeState: Rubik, depth: int, path: list[str]) -> list[str]:
		"""
		Fonction auxiliaire pour effectuer la recherche en profondeur (DFS) afin de trouver une séquence
		de mouvements qui résout la permutation des arêtes et des coins du Rubik's Cube.

		Paramètres:
		- cubeState (Rubik): L'état actuel du Rubik's Cube à explorer.
		- depth (int): La profondeur actuelle de la recherche.
		- maxDepth (int): La profondeur maximale jusqu'à laquelle explorer les mouvements.
		- path (list[str]): La séquence actuelle de mouvements explorée.

		Retourne:
		- list[str]: Une liste de mouvements qui résout la permutation des arêtes et des coins, ou None
		  si aucune solution n'est trouvée à cette profondeur.
		"""
		# print(path)
		if cubeState.isSolved():
			return path
		if depth > maxDepth:
			return None

		if edgePermutationTable.getPruning(cubeState.getedgeOrtState()) > maxDepth - depth:
			return None
		if cornerPermutationTable.getPruning(cubeState.getcornerOrtState()) > maxDepth - depth:
			return None
		
		moves = ["U", "U'", "D", "D'", "F", "F'", "B", "B'", "R", "R'", "L", "L'"]

		for move in moves:
			newCube: Rubik = copy.deepcopy(cubeState)
			newCube.apply_move(move)
			result = dfs(newCube, depth + 1, path + [move])
			if result is not None:
				return result
		return None
	
	# for depth in range(1, maxDepth + 1):
	# 	result = dfs(cube, 0, depth, [])
	# 	if result is not None:
	# 		return result
	# return None
	return dfs(cube, 0, [])

if __name__ == "__main__":
	rubik = Rubik()
	rubik.shuffle()
	# rubik.generateRandomCube(5, mode='easy') # easy <=> no inverse moves, hard <=> all moves
	print(rubik.newSolver())
	# rubik.apply_move("B")
	# rubik.apply_move("B'")
	# rubik.apply_move("U'")
	# rubik.apply_move("u")
	# rubik.apply_move("u'")
	# rubik.visualize_cube()
	# rubik.apply_move("U'")
	# rubik.visualize_cube()
	# rubik.apply_sequences("R2 D' B' (RU4R'U')4 D F2 R F2 R2 U L' F2 U' B' L2 R D B' R' B2 L2 	F2 L2 R2 U2 	D2")
