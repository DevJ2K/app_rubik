from Rubik import Rubik

class RubikChecker:
	def __init__(self, cube: Rubik) -> None:
		self.cube = cube.get_cube()
		self.stickers = {'W': 0, 'Y': 0, 'B': 0, 'R': 0, 'G': 0, 'O': 0}
		self.edges = cube.getEdges()
		self.corners = cube.getCorners()


	def checkStickers(self) -> bool:
		for face in self.cube:
			for row in face:
				for color in row:
					self.stickers[color] += 1
		return all([self.stickers[i] == 9 for i in self.stickers])


	def checkPermutation(self):
		solvedCube = Rubik()
		cornersSolved = solvedCube.getCorners()
		edgesSolved = solvedCube.getEdges()
		cornerIndex = {v: k for k, v in enumerate(cornersSolved)}
		edgeIndex = {v: k for k, v in enumerate(edgesSolved)}

		def findPieceIndex(currentPiece, solvedMap, isCorner=True):
			ori = [currentPiece]
			if isCorner:
				ori += [
					(currentPiece[1], currentPiece[2], currentPiece[0]),
					(currentPiece[2], currentPiece[0], currentPiece[1])
				]
			else:
				ori += [
					(currentPiece[1], currentPiece[0])
				]
			for i in ori:
				if i in solvedMap:
					return solvedMap[i]
			return None

		cornerPermutation = []
		for piece in self.corners:
			mapIndex = findPieceIndex(piece, cornerIndex, isCorner=True)
			if mapIndex is None:
				print('here')
				return False
			cornerPermutation.append(mapIndex)
		edgePermutation = []
		for piece in self.edges:
			mapIndex = findPieceIndex(piece, edgeIndex, isCorner=False)
			if mapIndex is None:
				return False
			edgePermutation.append(mapIndex)
		
		def parity(permutation):
			inv = 0
			n = len(permutation)
			for i in range(n):
				for j in range(i + 1, n):
					if permutation[i] > permutation[j]:
						inv += 1
			return inv % 2
		
		cornerParity = parity(cornerPermutation)
		edgeParity = parity(edgePermutation)
		if cornerParity != edgeParity:
			return False
		return True

	def checkOrientation(self):
		solvedCube = Rubik()
		cornersSolved = solvedCube.getCorners()
		edgesSolved = solvedCube.getEdges()

		def cornerOrientation(current, solved):
			for i in range(3):
				if current[i] == solved[i]:
					return i % 3
			return 0

		cornerSum = 0
		for current, solved in zip(self.corners, cornersSolved):
			cornerSum += cornerOrientation(current, solved)
		if cornerSum % 3 != 0:
			return False
		edgeFlip = 0
		for current, solved in zip(self.edges, edgesSolved):
			if current != solved:
				edgeFlip += 1
		if edgeFlip % 2 != 0:
			return False
		return True

	def isSolvable(self):
		if not self.checkStickers() or \
			not self.checkPermutation() or \
			not self.checkOrientation():
			return False
		return True


if __name__ == "__main__":
	cube = Rubik()
	cube.generateRandomCube(10)
	# cube.cube_up = [
	# 		['W', 'W', 'W'],
	# 		['W', 'W', 'W'],
	# 		['W', 'W', 'W'],
	# 	]
	checker = RubikChecker(cube)
	print(f"Cube solvable ? : {checker.isSolvable()}")
