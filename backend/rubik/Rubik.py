from visualizers.rubik_visualizer import visualize_cube_3D
from RubikMoves import RubikMoves
from ErrorManager import *
from parser import check_notation

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

		self.cube_up: list[list[str]] = [
			['1', '1', '1'],
			['1', '1', '1'],
			['1', '1', '1'],
		]
		self.cube_down: list[list[str]] = [
			['2', '2', '2'],
			['2', '2', '2'],
			['2', '2', '2'],
		]
		self.cube_front: list[list[str]] = [
			['3', '3', '3'],
			['3', '3', '3'],
			['3', '3', '3'],
		]
		self.cube_back: list[list[str]] = [
			['4', '4', '4'],
			['4', '4', '4'],
			['4', '4', '4'],
		]
		self.cube_left: list[list[str]] = [
			['5', '5', '5'],
			['5', '5', '5'],
			['5', '5', '5'],
		]
		self.cube_right: list[list[str]] = [
			['6', '6', '6'],
			['6', '6', '6'],
			['6', '6', '6'],
		]

	def check_valid_cube(self) -> bool:
		pass

	def apply_move(self, move: RubikMoves) -> None:
		pass

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

	def visualize_cube(self) -> None:
		"""Visualize cube with mathplotlib.
		"""
		visualize_cube_3D(
			self.cube_up,
			self.cube_down,
			self.cube_front,
			self.cube_back,
			self.cube_left,
			self.cube_right,
			"Rubik Visualizer",
			self.COLORS
		)
		pass

	def solve(self) -> None:
		"""Solve the self.cube
		"""
		pass

if __name__ == "__main__":
	rubik = Rubik()
	# rubik.visualize_cube()
	rubik.apply_sequences("R2 D' B' (RU4R'U')4 D F2 R F2 R2 U L' F2 U' B' L2 R D B' R' B2 L2 	F2 L2 R2 U2 	D2")

