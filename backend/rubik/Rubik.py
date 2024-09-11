from visualizers.rubik_visualizer import visualize_cube_3D
from RubikMoves import RubikMoves
from ErrorManager import *
from parser import check_notation
from PruningTable import PruningTable

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
			'1': 'white',  # face 1 (up)
			'2': 'yellow', # face 2 (bottom)
			'3': 'blue',   # face 3 (back)
			'4': 'green',  # face 4 (front)
			'5': 'red',	# face 5 (right)
			'6': 'orange', # face 6 (left)
		}


		# self.cube = [[3] * 3]
		self.cube_up: list[list[str]] = [(['W' for _ in range(3)]) for _x in range(3)]
		self.cube_down: list[list[str]] = [(['Y' for _ in range(3)]) for _x in range(3)]
		self.cube_front: list[list[str]] = [(['G' for _ in range(3)]) for _x in range(3)]
		self.cube_back: list[list[str]] = [(['B' for _ in range(3)]) for _x in range(3)]
		self.cube_left: list[list[str]] = [(['O' for _ in range(3)]) for _x in range(3)]
		self.cube_right: list[list[str]] = [(['R' for _ in range(3)]) for _x in range(3)]

		self.corners = []
		self.edges = []


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

	def getEdgeOrientation(self) -> list[int]:
		"""
		This method calculates the orientation of the edges of the Rubik's Cube.
		An edge is considered oriented if one of its colors is white ('W') or yellow ('Y').
		Otherwise, the edge is considered misoriented.

		The cube's current state is retrieved and the relevant edges are evaluated.
		Each edge is represented by two stickers, and the function checks 
		whether one of these stickers is 'W' or 'Y'.

		Returns:
		list[int]: A list of integers where 0 indicates an oriented edge 
				   (one of the stickers is 'W' or 'Y') and 1 indicates a misoriented edge.
		"""
		cube_up,cube_down,cube_front,cube_back,cube_left,cube_right = self.get_cube()
		edges = [
			(cube_up[0][1], cube_back[0][1]),	
			(cube_up[1][2], cube_right[0][1]),
			(cube_up[2][1], cube_front[0][1]),
			(cube_up[1][0], cube_left[0][1]),	
			(cube_down[0][1], cube_front[2][1]),
			(cube_down[1][2], cube_right[2][1]),
			(cube_down[2][1], cube_back[2][1]),
			(cube_down[1][0], cube_left[2][1]),
			(cube_front[1][0], cube_left[1][2]),
			(cube_front[1][2], cube_right[1][0]),
			(cube_back[1][0], cube_left[1][0]),
			(cube_back[1][2], cube_right[1][2])
		]
		# print(edges)
		orientation = []
		for edge in edges:
			if edge[0] in ['W', 'Y'] or edge[1] in ['W', 'Y']:
				orientation.append(0)
			else:
				orientation.append(1)
		return orientation
	
	def getCornerOrientation(self) -> list[int]:
		cube_up,cube_down,cube_front,cube_back,cube_left,cube_right = self.get_cube()
		corners = [
			(cube_up[0][0], cube_left[0][2], cube_back[0][0]),
			(cube_up[0][2], cube_right[0][2], cube_back[0][2]),
			(cube_up[2][2], cube_right[0][0], cube_front[0][2]),
			(cube_up[2][0], cube_left[0][0], cube_front[0][0]),
			(cube_down[0][0], cube_left[2][2], cube_front[2][0]),
			(cube_down[0][2], cube_right[2][2], cube_front[2][2]),
			(cube_down[2][2], cube_right[2][0], cube_back[2][2]),
			(cube_down[2][0], cube_left[2][0], cube_back[2][0])
		]
		# print(corners)
		orientation = []
		for corner in corners:
			if corner[0] in ['W', 'Y']:
				orientation.append(0)
			elif corner[1] in ['W', 'Y']:
				orientation.append(1)
			else:
				orientation.append(2)
		return orientation
	
	def getEdgeOrientationState(self) -> int:
		edgeOrientation = self.getEdgeOrientation()
		state = 0
		for i in range(12):
			state = (state << 1) | edgeOrientation[i]
		return state
	
	def getCornerOrientationState(self) -> int:
		cornerOrientation = self.getCornerOrientation()
		state = 0
		for i in range(8):
			state = state * 3 + cornerOrientation[i]
		return state


	def setEdgeOrientationState(self, state) -> None:
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

	def setCornerOrientationState(self, state):
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

	def solve(self) -> None:
		"""Solve the self.cube
		"""
		pass

	def isOrientationSolved(self) -> bool:
		edges = self.getEdgeOrientation()
		for edge in edges:
			if edge == 1:
				return False
		corners = self.getCornerOrientation()
		for corner in corners:
			if corner == 1 or corner == 2:
				return False
		return True

	def isPermutationSolved(self) -> bool:
		pass

	def shuffle(self):
		# U D R2 L2 F2 B2
		self.apply_move("U")
		self.apply_move("D")
		self.apply_move("R")
		self.apply_move("R")
		self.apply_move("L")
		self.apply_move("L")
		self.apply_move("F")
		self.apply_move("F")
		self.apply_move("B")
		self.apply_move("B")

def applyMoveToSolve(state, move):
	pass

def applyOrientationMove(state, move):
	pass

def applyPermutationMove(state, move):
	pass

def phase1Search(cube: Rubik, maxDepth: int, edgePruningTable: PruningTable, cornerPruningTable: PruningTable) -> list[str]:
	def dfs(cubeState: Rubik, depth: int, maxDepth: int, path: list[str]) -> list[str]:
		if cubeState.isOrientationSolved():
			return path
		if depth >= maxDepth:
			return None
		if edgePruningTable.getPruning(cubeState.getEdgeOrientationState()) > maxDepth - depth:
			return None
		if cornerPruningTable.getPruning(cubeState.getCornerOrientationState()) > maxDepth - depth:
			return None
		
		moves = ["U", "U'", "D", "D'", "F", "F'", "B", "B'", "R", "R'", "L", "L'"]

		for move in moves:
			cubeState.apply_move(move)
			result = dfs(cubeState, depth + 1, maxDepth, path + [move])
			if "'" in move:
				cubeState.apply_move(move)
			else:
				cubeState.apply_move(move + "'")
			if result is not None:
				return result
		return None
	
	for depth in range(1, maxDepth + 1):
		result = dfs(cube, 0, depth, [])
		if result is not None:
			return result
	return None

def phase2Search(cube: Rubik, maxDepth: int, edgePermutationTable: PruningTable, cornerPermutationTable: PruningTable) -> list[str]:
	def dfs(cubeState: Rubik, depth: int, maxDepth: int, path: list[str]) -> list[str]:
		if cubeState.isPermutationSolved():
			return path
		if depth >= maxDepth:
			return None
		if edgePermutationTable.getPruning(cubeState.getEdgeOrientationState()) > maxDepth - depth:
			return None
		if cornerPermutationTable.getPruning(cubeState.getCornerOrientationState()) > maxDepth - depth:
			return None
		
		moves = ["U", "U'", "D", "D'", "F", "F'", "B", "B'", "R", "R'", "L", "L'"]

		for move in moves:
			newCube = cubeState.copy()
			# apply permutation movement
			result = dfs(newCube, depth + 1, maxDepth, path + [move])
			if result is not None:
				return result
		return None
	
	for depth in range(1, maxDepth + 1):
		result = dfs(cube, 0, depth, [])
		if result is not None:
			return result
	return None

if __name__ == "__main__":
	rubik = Rubik()
	# phase1EdgePruningTable = generateEdgePruningTable()
	# phase1CornerPruningTable = generateCornerPruningTable()
	# print(phase1EdgePruningTable)
	rubik.shuffle()
	# rubik.visualize_cube()
	# print(rubik.get_cube())
	rubik.getCornerOrientation()
	# rubik.apply_move("B")
	# rubik.apply_move("B'")
	# rubik.apply_move("U'")
	# rubik.apply_move("u")
	# rubik.apply_move("u'")
	# rubik.visualize_cube()
	# rubik.apply_move("U'")
	# rubik.visualize_cube()
	# rubik.apply_sequences("R2 D' B' (RU4R'U')4 D F2 R F2 R2 U L' F2 U' B' L2 R D B' R' B2 L2 	F2 L2 R2 U2 	D2")
