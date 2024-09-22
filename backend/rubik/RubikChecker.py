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


	def normalizePiece(self, piece):
		return tuple(sorted(piece))


	def findPieceIndex(self, currentPiece, solvedMap):
		normalized = self.normalizePiece(currentPiece)
		return solvedMap.get(normalized, None)

	def checkPermutation(self):
		solvedCube = Rubik()
		cornersSolved = solvedCube.getCorners()
		edgesSolved = solvedCube.getEdges()

		if not cornersSolved or not edgesSolved or not self.corners or not self.edges:
			return False

		cornerIndex = {}
		for i, piece in enumerate(cornersSolved):
			normalized = self.normalizePiece(piece)
			cornerIndex[normalized] = i
		edgeIndex = {}
		for i, piece in enumerate(edgesSolved):
			normalized = self.normalizePiece(piece)
			edgeIndex[normalized] = i

		cornerPermutation = []
		for piece in self.corners:
			# print(piece, cornerIndex)
			mapIndex = self.findPieceIndex(piece, cornerIndex)
			if mapIndex is None:
				return False
			cornerPermutation.append(mapIndex)
		edgePermutation = []
		for piece in self.edges:
			mapIndex = self.findPieceIndex(piece, edgeIndex)
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

		solvedCornerOri = {}
		for i, piece in enumerate(cornersSolved):
			solvedCornerOri[i] = piece

		cornerOriSum = 0
		for current, solved in zip(self.corners, cornersSolved):
			normalized = self.normalizePiece(current)
			solvedIndex = self.findPieceIndex(current, {self.normalizePiece(p): i for i, p in enumerate(cornersSolved)})
			if solvedIndex is None:
				return False
			solved = cornersSolved[solvedIndex]
			try:
				ori = current.index(solved[0])
			except ValueError:
				ori = 0
			print(ori)
			cornerOriSum += ori
		print(cornerOriSum)
		if cornerOriSum % 3 != 0:
			print('here')
			return False
		
		edgeFlip = 0
		for current, solved in zip(self.edges, edgesSolved):
			if current != solved:
				if current[::-1] == solved:
					edgeFlip += 1
				else:
					print('here 2')
					return False
		if edgeFlip % 2 != 0:
			print('here 3')
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
	cube.generateRandomCube(5)
	print(cube.get_cube())
	print(cube.getEdges())
	print(cube.getCorners())
	# cube.visualize_cube()
	# cube.cube_up = [
	# 		['W', 'W', 'W'],
	# 		['W', 'W', 'W'],
	# 		['W', 'W', 'W'],
	# 	]
	checker = RubikChecker(cube)
	print(f"Cube solvable ? : {checker.isSolvable()}")
