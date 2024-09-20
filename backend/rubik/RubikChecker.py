from Rubik import Rubik

class RubikChecker:
	def __init__(self) -> None:
		self.stickers = {'W': 0, 'Y': 0, 'B': 0, 'R': 0, 'G': 0, 'O': 0}

	def verifyStickers(self, cube: list[list[list[str]]]) -> bool:
		for face in cube:
			for row in face:
				for color in row:
					self.stickers[color] += 1
		return all([self.stickers[i] == 9 for i in self.stickers])
	


if __name__ == "__main__":
	cube = Rubik()
	cube.generateRandomCube(10)
	checker = RubikChecker()
	checker.verifyStickers(cube.get_cube())