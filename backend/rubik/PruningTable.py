from collections import deque
# from Rubik import Rubik

class PruningTable:
	def __init__(self, nbStates) -> None:
		self.table = [-1] * nbStates
		
	def getPruning(self, state):
		return self.table[state]
	
	def generateTable(self, initialState, getNeighbors):
		self.table[initialState] = 0
		queue = deque([initialState])

		while queue:
			# print('len queue: ', len(queue))
			currentState = queue.popleft()
			currentDistance = self.table[currentState]

			neighbors = getNeighbors(currentState)
			# print('neighbors: ', neighbors)
			for neighbor in neighbors:
				if self.table[neighbor] == -1:
					# print(neighbor)
					self.table[neighbor] = currentDistance + 1
					queue.append(neighbor)
			
	def getDistance(self, state):
		return self.table[state]
	
def generateEdgePruningTablePermutation(initialState, getNeighbors):
	pruningTable = PruningTable(12*11*10*9*8*7*6*5*4*3*2)
	pruningTable.table[initialState] = 0
	queue = deque([initialState])

	while queue:
		currentState = queue.popleft()
		currentDistance = pruningTable.table[currentState]

		neighbors = getNeighbors(currentState)

		for neighbor in neighbors:
			if pruningTable.table[neighbor] == -1:
				# print(neighbor)
				pruningTable.table[neighbor] = currentDistance + 1
				queue.append(neighbor)
	return pruningTable

def generateCornerPruningTablePermutation(initialState, getNeighbors):
	pruningTable = PruningTable(8*7*6*5*4*3*2)
	pruningTable.table[initialState] = 0
	queue = deque([initialState])

	while queue:
		currentState = queue.popleft()
		currentDistance = pruningTable.table[currentState]

		neighbors = getNeighbors(currentState)

		for neighbor in neighbors:
			if pruningTable.table[neighbor] == -1:
				pruningTable.table[neighbor] = currentDistance + 1
				queue.append(neighbor)
	return pruningTable

def getNeighborsEdgeOrientation(state) -> list[int]:
	from Rubik import Rubik
	neighbors = []
	cube = Rubik()
	print(state)
	cube.setEdgeOrientationState(state)
	
	moves = ["U", "U'", "D", "D'", "F", "F'", "B", "B'", "R", "R'", "L", "L'"]

	for move in moves:
		cube.apply_move(move)
		neighbors.append(cube.getEdgeOrientationState())
		if "'" in move:
			cube.apply_move(move)
		else:
			cube.apply_move(move + "'")
	return neighbors

def getNeighborsCornerOrientation(state) -> list[int]:
	from Rubik import Rubik
	neighbors = []
	cube = Rubik()
	cube.setCornerOrientationState(state)
	
	moves = ["U", "U'", "D", "D'", "F", "F'", "B", "B'", "R", "R'", "L", "L'"]

	for move in moves:
		cube.apply_move(move)
		neighbors.append(cube.getCornerOrientationState())
		if "'" in move:
			cube.apply_move(move)
		else:
			cube.apply_move(move + "'")

	return neighbors

def generateEdgePruningTable():
	nbStates = 2**12
	pruningTable = PruningTable(nbStates)
	initialState = 0
	pruningTable.generateTable(initialState, getNeighborsEdgeOrientation)
	return pruningTable

def generateCornerPruningTable():
	nbStates = 3**8
	pruningTable = PruningTable(nbStates)
	initialState = 0
	pruningTable.generateTable(initialState, getNeighborsCornerOrientation)
	return pruningTable

if __name__ == "__main__":
	from Rubik import Rubik, phase1Search
	cube = Rubik()
	cube.shuffle()

	phase1EdgePruningTable = generateEdgePruningTable()
	# for i in range(2**12):
	# 	distance = phase1EdgePruningTable.getPruning(i)
	# 	if distance != -1: print(distance)
	
	phase1CornerPruningTable = generateCornerPruningTable()
	# for i in range(3**8):
	# 	distance = phase1CornerPruningTable.getPruning(i)
	# 	if distance != -1: print(distance)
	G1State = phase1Search(cube, 12, phase1EdgePruningTable, phase1CornerPruningTable)
	# print(G1State)
	# print(phase1EdgePruningTable)
