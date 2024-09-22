from visualizers.rubik_visualizer import visualize_cube_3D
from RubikMoves import RubikMoves
from ErrorManager import *
from parser import check_notation
import random
import time


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
		self.formatedSolution = []

		# self.cube = [[3] * 3]
		self.cube_up: list[list[str]] = [(['W' for _ in range(3)]) for _x in range(3)]
		self.cube_down: list[list[str]] = [(['Y' for _ in range(3)]) for _x in range(3)]
		self.cube_front: list[list[str]] = [(['G' for _ in range(3)]) for _x in range(3)]
		self.cube_back: list[list[str]] = [(['B' for _ in range(3)]) for _x in range(3)]
		self.cube_left: list[list[str]] = [(['O' for _ in range(3)]) for _x in range(3)]
		self.cube_right: list[list[str]] = [(['R' for _ in range(3)]) for _x in range(3)]

# 		self.cube_up: list[list[str]] = [
# 			['6', '6', '2'],
# 			['6', '1', '3'],
# 			['1', '3', '2'],
# 		]
# 		self.cube_down: list[list[str]] = [
# 			['2', '5', '3'],
# 			['2', '2', '3'],
# 			['5', '5', '6'],
# 		]
# 		self.cube_front: list[list[str]] = [
# 			['6', '5', '4'],
# 			['1', '4', '6'],
# 			['3', '1', '4'],
# 		]
# 		self.cube_back: list[list[str]] = [
# 			['4', '4', '4'],
# 			['4', '3', '1'],
# 			['3', '2', '5'],
# 		]
# 		self.cube_left: list[list[str]] = [
# 			['1', '2', '3'],
# 			['3', '6', '4'],
# 			['1', '2', '2'],
# 		]
# 		self.cube_right: list[list[str]] = [
# 			['6', '6', '5'],
# 			['1', '5', '5'],
# 			['1', '4', '5'],
# 		]

		# self.cube_up: list[list[str]] = [(['1' for _ in range(3)]) for _x in range(3)]
		# self.cube_front: list[list[str]] = [(['3' for _ in range(3)]) for _x in range(3)]
		# self.cube_right: list[list[str]] = [(['6' for _ in range(3)]) for _x in range(3)]
		# self.cube_left: list[list[str]] = [(['5' for _ in range(3)]) for _x in range(3)]
		# self.cube_back: list[list[str]] = [(['4' for _ in range(3)]) for _x in range(3)]

		# self.cube_down: list[list[str]] = [(['2' for _ in range(3)]) for _x in range(3)]


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

	def getEdges(self) -> list[tuple[str, str]]:
		cube_up,cube_down,cube_front,cube_back,cube_left,cube_right = self.get_cube()
		return [
			(cube_up[2][1], cube_front[0][1]),
			(cube_up[1][2], cube_right[0][1]),
			(cube_up[0][1], cube_back[0][1]),
			(cube_up[1][0], cube_left[0][1]),
			(cube_down[2][1], cube_front[2][1]),
			(cube_down[1][0], cube_right[2][1]),
			(cube_down[0][1], cube_back[2][1]),
			(cube_down[1][2], cube_left[2][1]),
			(cube_front[1][2], cube_right[1][0]),
			(cube_back[1][0], cube_right[1][2]),
			(cube_back[1][2], cube_left[1][0]),
			(cube_front[1][0], cube_left[1][2]),
		]

	def getCorners(self) -> list[tuple[str, str, str]]:
		cube_up,cube_down,cube_front,cube_back,cube_left,cube_right = self.get_cube()
		return [
			(cube_up[2][2], cube_right[0][0], cube_front[0][2]),
			(cube_up[0][2], cube_right[0][2], cube_back[0][0]),
			(cube_down[2][2], cube_left[2][2], cube_front[2][0]),
			(cube_down[2][0], cube_right[2][0], cube_front[2][2]),
			(cube_up[0][0], cube_left[0][0], cube_back[0][2]),
			(cube_up[2][0], cube_left[0][2], cube_front[0][0]),
			(cube_down[0][0], cube_right[2][2], cube_back[2][0]),
			(cube_down[0][2], cube_left[2][0], cube_back[2][2])
		]

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

		# print(move)
		# print(result)
# 		self.visualize_cube(window_title=f"MOVE : {move}")

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
		self.applyMultipleMoves("U'", 3)
		self.applyMultipleMoves("F", 1)
		self.applyMultipleMoves("D", 1)
		self.applyMultipleMoves("F", 1)
		self.applyMultipleMoves("B", 1)
		self.applyMultipleMoves("R", 1)
		self.applyMultipleMoves("F", 1)
		self.applyMultipleMoves("L", 1)
		self.applyMultipleMoves("F", 1)

	def generateRandomCube(self, numMoves: int) -> None:
		"""
		Génère un cube de Rubik mélangé en appliquant une séquence aléatoire de mouvements.

		La méthode génère une séquence de mouvements pour mélanger le cube

		Paramètres:
		- numMoves (int): Nombre de mouvements à appliquer pour mélanger le cube.

		Retourne:
		- None: Modifie l'état du cube en appliquant les mouvements générés sans retourner de valeur.

		Notes:
		- Utilise `generateRandomMoves` pour créer la séquence de mouvements.
		"""
		def generateRandomMoves(numMoves: int) -> list[str]:
			"""
			Génère une liste de mouvements aléatoires

			Paramètres:
			- numMoves (int): Nombre de mouvements à générer.

			Retourne:
			- list[str]: Liste de mouvements aléatoires sous forme de chaînes de caractères.
			"""
			moves = ["U", "U'", "D", "D'", "F", "F'", "B", "B'", "L", "L'", "R", "R'"]
			move_sequences = []
			for _ in range(numMoves):
				move = random.choice(moves)
				move_sequences.append(move)
			return move_sequences
		moves = generateRandomMoves(numMoves)
		for move in moves:
			if "'" in move:
				self.applyMultipleMoves(move[:1], 3)
			elif "2" in move:
				self.applyMultipleMoves(move[:1], 2)
			else:
				self.applyMultipleMoves(move, 1)


	def formatSolution(self, input: list) -> None:
		for string in input:
			for i in range(0, len(string), 2):
				if (string[i + 1]) == '3':
					self.formatedSolution.append(string[i:i+1] + "'")
				elif (string[i + 1]) == '1':
					self.formatedSolution.append(string[i:i+1])
				else:
					self.formatedSolution.append(string[i:i+2])


	def solver(self):
		output = []
		from Solver import Solver
		solver = Solver(self)
		print('Table loading done!')
		for phase in range(1, 5):
			while solver.getPhaseId(self, phase) != solver.phaseGoal[phase]:
				path = solver.phaseTable[phase - 1][solver.getPhaseId(self, phase)]
				if path == "":
					print(f'No solution')
					return 1
				pathList = [path[i:i+2] for i in range(0, len(path), 2)]
				if path != 'I':
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

if __name__ == "__main__":
	startTime = time.time()
	rubik = Rubik()
	rubik.generateRandomCube(25)
	# rubik.shuffle()
	rubik.formatSolution(rubik.solver())
	solution = " ".join(rubik.formatedSolution)
	print(f"\033[1m\033[36mSolution: \033[0m{solution}")
	print(f"\033[1m\033[35mNombre de coups: \033[0m{len(rubik.formatedSolution)}")
	print(f"\033[1m\033[32mTemps écoulé: \033[0m{time.time() - startTime:.3f} secondes")
	print(f"\033[1m\033[33mCube résolu ? : \033[0m{rubik.isSolved()}")
	# print(rubik.get_cube())
	# rubik.visualize_cube()

	# ✅ UP
	# rubik.apply_sequences("U U U U")
	# rubik.apply_sequences("U' U' U' U'")

	# ✅ DOWN
	# rubik.apply_sequences("D D D D")
	# rubik.apply_sequences("D' D' D' D'")

	# ✅ FRONT
	# rubik.apply_sequences("F F F F")
	# rubik.apply_sequences("F' F' F' F'")

	# ✅ BACK
	# rubik.apply_sequences("B B B B")
	# rubik.apply_sequences("B' B' B' B'")

	# ✅ LEFT
	# rubik.apply_sequences("L L L L")
	# rubik.apply_sequences("L' L' L' L'")

	# ✅ RIGHT
	# rubik.apply_sequences("R R R R")
	# rubik.apply_sequences("R' R' R' R'")


	# rubik.apply_move("U")
	# rubik.apply_move("U")
	# rubik.apply_move("L")
	# rubik.apply_sequences("L L'")
	# rubik.apply_move("U")
	# rubik.apply_move("R")
	# rubik.apply_move("L")
	# rubik.apply_move("U'")
	# rubik.apply_move("R'")
	# rubik.apply_move("L'")
	# rubik.apply_move("F'")
	# rubik.apply_move("B'")
	# rubik.apply_sequences("U R L U' R' L' F' B'")
	# rubik.visualize_cube()
	# rubik.apply_move("B")
	# rubik.apply_move("B'")
	# rubik.apply_move("U'")
	# rubik.apply_move("u")
	# rubik.apply_move("u'")
	# rubik.visualize_cube()
	# rubik.apply_move("U'")
	# rubik.visualize_cube()
	# rubik.apply_sequences("R2 D' B' (RU4R'U')4 D F2 R F2 R2 U L' F2 U' B' L2 R D B' R' B2 L2 	F2 L2 R2 U2 	D2")
