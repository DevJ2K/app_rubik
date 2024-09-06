from visualizers.rubik_visualizer import visualize_cube_3D
from RubikMoves import RubikMoves
from ErrorManager import *
from parser import check_notation

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
			'1': 'white',  # face 1
			'2': 'yellow', # face 2
			'3': 'blue',   # face 3
			'4': 'green',  # face 4
			'5': 'red',    # face 5
			'6': 'orange', # face 6
		}


		# self.cube = [[3] * 3]
		self.cube_up: list[list[str]] = [(['1' for _ in range(3)]) for _x in range(3)]
		self.cube_down: list[list[str]] = [(['2' for _ in range(3)]) for _x in range(3)]
		self.cube_front: list[list[str]] = [(['3' for _ in range(3)]) for _x in range(3)]
		self.cube_back: list[list[str]] = [(['4' for _ in range(3)]) for _x in range(3)]
		self.cube_left: list[list[str]] = [(['5' for _ in range(3)]) for _x in range(3)]
		self.cube_right: list[list[str]] = [(['6' for _ in range(3)]) for _x in range(3)]


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
		self.visualize_cube(window_title=f"MOVE : {move}")

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

	def solve(self) -> None:
		"""Solve the self.cube
		"""
		pass

if __name__ == "__main__":
	rubik = Rubik()
	rubik.visualize_cube()
	rubik.apply_move("B")
	rubik.apply_move("B'")
	# rubik.apply_move("U'")
	# rubik.apply_move("u")
	# rubik.apply_move("u'")
	# rubik.visualize_cube()
	# rubik.apply_move("U'")
	# rubik.visualize_cube()
	# rubik.apply_sequences("R2 D' B' (RU4R'U')4 D F2 R F2 R2 U L' F2 U' B' L2 R D B' R' B2 L2 	F2 L2 R2 U2 	D2")

