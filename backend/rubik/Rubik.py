class Rubik:
	"""The class to solve an rubik cube"""
	def __init__(self, cube: list[list[str]] = None, sequences: str = None) -> None:
		if cube is None:
			self.cube = [
				[
					['1', '1', '1']
					['1', '1', '1']
					['1', '1', '1']
				],
				[
					['2', '2', '2']
					['2', '2', '2']
					['2', '2', '2']
				],
				[
					['3', '3', '3']
					['3', '3', '3']
					['3', '3', '3']
				],
				[
					['4', '4', '4']
					['4', '4', '4']
					['4', '4', '4']
				],
				[
					['5', '5', '5']
					['5', '5', '5']
					['5', '5', '5']
				],
				[
					['6', '6', '6']
					['6', '6', '6']
					['6', '6', '6']
				],
			]
		else:
			self.cube = cube
		pass


	def check_valid_cube(self) -> bool:
		pass

	def apply_sequences(self, sequences: str) -> None:
		"""Apply sequences to the rubik cube.

		Args:
			sequences (str): Sequences to apply to the rubik cube.
		"""
		pass

	def visualize_cube(self) -> None:
		"""Visualize cube with mathplotlib.
		"""
		pass

	def solve(self) -> None:
		"""Solve the self.cube
		"""
		pass

if __name__ == "__main__":
	rubik = Rubik()
	rubik.apply_sequences("R2 D' B' D F2 R F2 R2 U L' F2 U' B' L2 R D B' R' B2 L2 F2 L2 R2 U2 D2")
