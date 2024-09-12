class PruningTable:
	def __init__(self, nbStates) -> None:
		self.table = [-1] * nbStates
	
	def setPruning(self, state, depth):
		self.table[state] = depth

	def getPruning(self, state):
		return self.table[state]
	
	def generateTable(self, getNeighbors: function) -> None:
		"""
		Remplit la table de réduction en utilisant une recherche en largeur (BFS).

		Initialise la table avec les distances minimales à l'état initial (0) et explore les états voisins en utilisant
		la fonction `getNeighbors` fournie. Met à jour la table avec les distances minimales pour chaque état voisin découvert.

		Paramètres:
		- getNeighbors (function): Fonction qui retourne une liste des voisins d'un état donné.
		
		Retourne:
		- None: La méthode modifie directement la table de réduction sans retourner de valeur.
		"""
		queue = [0]
		self.setPruning(0, 0)

		while queue:
			currentState = queue.pop(0)
			currentDistance = self.getPruning(currentState)

			neighbors = getNeighbors(currentState)
			# print('neighbors: ', neighbors)
			for neighbor in neighbors:
				if self.table[neighbor] == -1:
					self.table[neighbor] = currentDistance + 1
					queue.append(neighbor)


def generateEdgePruningTablePermutation() -> PruningTable:
	"""
    Génère une table de réduction pour les permutations des arêtes du Rubik's Cube.

    Crée une table de réduction (`PruningTable`) pour toutes les permutations possibles des arêtes en utilisant
    une approche de recherche en largeur (BFS). Remplit la table avec les distances minimales à l'état initial (0).

    Retourne:
    - PruningTable: La table de réduction générée pour les permutations des arêtes.
    """
	total_states = 479001600 # <=> 12!
	pruningTable = PruningTable(total_states)

	queue = [0]
	pruningTable.setPruning(0, 0)

	while queue:
		currentState = queue.pop(0)
		currentDistance = pruningTable.getPruning(currentState)

		neighbors = getNeighborsEdgeOrientation(currentState)

		for neighbor in neighbors:
			if pruningTable.table[neighbor] == -1:
				# print(neighbor)
				pruningTable.setPruning(neighbor, currentDistance + 1)
				queue.append(neighbor)
	return pruningTable

def generateCornerPruningTablePermutation() -> PruningTable:
	"""
    Génère une table de réduction pour les permutations des coins du Rubik's Cube.

    Crée une table de réduction (`PruningTable`) pour toutes les permutations possibles des coins en utilisant
    une approche de recherche en largeur (BFS). Remplit la table avec les distances minimales à l'état initial (0).

    Retourne:
    - PruningTable: La table de réduction générée pour les permutations des coins.
    """
	total_states = 40320 # <=> 8!
	pruningTable = PruningTable(total_states)

	queue = [0]
	pruningTable.setPruning(0, 0)

	while queue:
		currentState = queue.pop(0)
		currentDistance = pruningTable.getPruning(currentState)

		neighbors = getNeighborsCornerOrientation(currentState)

		for neighbor in neighbors:
			if pruningTable.table[neighbor] == -1:
				pruningTable.setPruning(neighbor, currentDistance + 1)
				queue.append(neighbor)
	return pruningTable

def getNeighborsEdgeOrientation(state: int) -> list[int]:
	"""
    Obtient les voisins d'un état d'orientation des arêtes du Rubik's Cube.

    Génère une liste d'états voisins en appliquant chaque mouvement possible au cube avec l'état d'orientation des arêtes
    donné. Chaque voisin est un nouvel état d'orientation des arêtes après un mouvement.

    Paramètres:
    - state (int): L'état d'orientation des arêtes du cube à partir duquel les voisins sont générés.

    Retourne:
    - list[int]: Une liste d'entiers représentant les états voisins des orientations des arêtes.
    """
	from Rubik import Rubik
	neighbors = []
	cube = Rubik()
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

def getNeighborsCornerOrientation(state: int) -> list[int]:
	"""
    Obtient les voisins d'un état d'orientation des coins du Rubik's Cube.

    Génère une liste d'états voisins en appliquant chaque mouvement possible au cube avec l'état d'orientation des coins
    donné. Chaque voisin est un nouvel état d'orientation des coins après un mouvement.

    Paramètres:
    - state (int): L'état d'orientation des coins du cube à partir duquel les voisins sont générés.

    Retourne:
    - list[int]: Une liste d'entiers représentant les états voisins des orientations des coins.
    """
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

def generateEdgePruningTable() -> PruningTable:
	"""
    Génère une table de réduction pour les orientations des arêtes du Rubik's Cube.

    Crée une table de réduction (`PruningTable`) basée sur toutes les orientations possibles des arêtes, puis la
    remplit en utilisant l'état initial et une fonction pour obtenir les voisins des orientations des arêtes.

    Retourne:
    - PruningTable: La table de réduction générée pour les orientations des arêtes.
    """
	nbStates = 2**12
	pruningTable = PruningTable(nbStates)
	pruningTable.generateTable(getNeighborsEdgeOrientation)
	return pruningTable

def generateCornerPruningTable() -> PruningTable:
	"""
    Génère une table de réduction pour les orientations des coins du Rubik's Cube.

    Crée une table de réduction (`PruningTable`) basée sur toutes les orientations possibles des coins, puis la
    remplit en utilisant l'état initial et une fonction pour obtenir les voisins des orientations des coins.

    Retourne:
    - PruningTable: La table de réduction générée pour les orientations des coins.
    """
	nbStates = 3**8
	pruningTable = PruningTable(nbStates)
	pruningTable.generateTable(getNeighborsCornerOrientation)
	return pruningTable

# if __name__ == "__main__":
# 	from Rubik import Rubik, phase1Search, phase2Search
# 	cube = Rubik()
# 	cube.generateRandomCube(7, mode='easy') # easy <=> no inverse moves, hard <=> all moves
# 	# cube.shuffle()
# 	# cube.visualize_cube()

# 	phase1EdgePruningTable = generateEdgePruningTable()
# 	# # for i in range(2**12):
# 	# # 	distance = phase1EdgePruningTable.getPruning(i)
# 	# # 	if distance != -1: print(distance)
	
# 	phase1CornerPruningTable = generateCornerPruningTable()
# 	G1State = phase1Search(cube, 12, phase1EdgePruningTable, phase1CornerPruningTable)
# 	print(G1State)
# 	cube.visualize_cube()
# 	for move in G1State:
# 		cube.apply_move(move)
# 	if cube.isSolved():
# 		print("Solved! Sequences: ", G1State)
# 	cube.visualize_cube()

# 	# phase2EdgePruningTable = generateEdgePruningTablePermutation()
# 	# phase2CornerPruningTable = generateCornerPruningTablePermutation()
# 	# print('fin phase 2 pruningTable')
# 	# print(cube.get_cube())
# 	# result = phase2Search(cube, 20, phase2EdgePruningTable, phase2CornerPruningTable)
# 	# print(result)
# 	# print(phase1EdgePruningTable)
