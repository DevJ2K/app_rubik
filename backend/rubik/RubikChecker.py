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

		cornerIndex = {}
		for i, piece in enumerate(cornersSolved):
			normalized = self.normalizePiece(piece)
			cornerIndex.setdefault(normalized, []).append(i)
		edgeIndex = {}
		for i, piece in enumerate(edgesSolved):
			normalized = self.normalizePiece(piece)
			edgeIndex.setdefault(normalized, []).append(i)

		cornerPermutation = []
		usedCorners = set()
		for piece in self.corners:
			normalized = self.normalizePiece(piece)
			possibleIndices = cornerIndex.get(normalized, None)
			mappedIndex = None
			for i in possibleIndices:
				if i not in usedCorners:
					mappedIndex = i
					usedCorners.add(i)
					break
			if mappedIndex is None:
				return False
			cornerPermutation.append(mappedIndex)
		
		edgePermutation = []
		usedEdges = set()
		for piece in self.edges:
			normalized = self.normalizePiece(piece)
			possibleIndices = edgeIndex.get(normalized, None)
			mappedIndex = None
			for i in possibleIndices:
				if i not in usedEdges:
					mappedIndex = i
					usedEdges.add(i)
					break
			if mappedIndex is None:
				return False
			edgePermutation.append(mappedIndex)
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
	checker = RubikChecker(cube)
	print(f"Cube solvable ? : {checker.isSolvable()}")