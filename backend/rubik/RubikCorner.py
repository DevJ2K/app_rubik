# Will be a class who takes a corner has arguments and final position and returns movements to apply and distances.
from Rubik import Rubik
import itertools


# neighboring_corner = [
# 	{
# 		'1': [1, 3, 5],  # Corners à 1 mouvement du coin URF (0)
# 	},
# 	{
# 		'1': [0, 4, 6],  # Corners à 1 mouvement du coin UBR (1)
# 	},
# 	{
# 		'1': [3, 5, 7],  # Corners à 1 mouvement du coin DLF (2)
# 	},
# 	{
# 		'1': [0, 2, 6],  # Corners à 1 mouvement du coin DFR (3)
# 	},
# 	{
# 		'1': [1, 5, 7],  # Corners à 1 mouvement du coin ULB (4)
# 	},
# 	{
# 		'1': [0, 2, 4],  # Corners à 1 mouvement du coin UFL (5)
# 	},
# 	{
# 		'1': [1, 3, 7],  # Corners à 1 mouvement du coin DRB (6)
# 	},
# 	{
# 		'1': [2, 4, 6],  # Corners à 1 mouvement du coin DBL (7)
# 	}
# ]

	# 0: Up Right Front
	# 1: Up Back Right
	# 2: Down Left Front
	# 3: Down Front Right
	# 4: Up Left Back
	# 5: Up Front Left
	# 6: Down Right Back
	# 7: Down Back Left

neighboring_corner = {
	'0': {
		'1': ["U'", "R"],
		'3': ["R'", "F"],
		'5': ["F'","U"]
	},
	'1': {
		'0': ["R'", "U"],
		'4': ["U'", "B"],
		'6': ["R", "B'"],
	},
	'2': {
		'3': ["F'", "D"],
		'5': ["F", "L'"],
		'7': ["D'", "L"]
	},
	'3': {
		'0': ["R", "F'"],
		'2': ["F", "D'"],
		'6': ["D", "R'"]
	},
	'4': {
		'1': ["U", "B'"],
		'5': ["L", "U'"],
		'7': ["B", "L'"]
	},
	'5': {
		'0': ["U'", "F"],
		'2': ["F'", "L"],
		'4': ["U", "L'"]
	},
	'6': {
		'1': ["R'", "B"],
		'3': ["D'", "R"],
		'7': ["D", "B'"]
	},
	'7': {
		'2': ["D", "L'"],
		'4': ["B'", "L"],
		'6': ["B", "D'"]
	}
}

tab_pos_corners = [
	{
		'1': [1, 3, 5],  # Corners à 1 mouvement du coin URF (0)
		'2': [2, 4, 6],  # Corners à 2 mouvements du coin URF (0)
		'3': [7]         # Corner à 3 mouvements du coin URF (0)
	},
	{
		'1': [0, 4, 6],  # Corners à 1 mouvement du coin UBR (1)
		'2': [2, 3, 7],  # Corners à 2 mouvements du coin UBR (1)
		'3': [5]         # Corner à 3 mouvements du coin UBR (1)
	},
	{
		'1': [3, 5, 7],  # Corners à 1 mouvement du coin DLF (2)
		'2': [0, 1, 6],  # Corners à 2 mouvements du coin DLF (2)
		'3': [4]         # Corner à 3 mouvements du coin DLF (2)
	},
	{
		'1': [0, 2, 6],  # Corners à 1 mouvement du coin DFR (3)
		'2': [1, 5, 7],  # Corners à 2 mouvements du coin DFR (3)
		'3': [4]         # Corner à 3 mouvements du coin DFR (3)
	},
	{
		'1': [1, 5, 7],  # Corners à 1 mouvement du coin ULB (4)
		'2': [0, 2, 6],  # Corners à 2 mouvements du coin ULB (4)
		'3': [3]         # Corner à 3 mouvements du coin ULB (4)
	},
	{
		'1': [0, 2, 4],  # Corners à 1 mouvement du coin UFL (5)
		'2': [1, 3, 7],  # Corners à 2 mouvements du coin UFL (5)
		'3': [6]         # Corner à 3 mouvements du coin UFL (5)
	},
	{
		'1': [1, 3, 7],  # Corners à 1 mouvement du coin DRB (6)
		'2': [0, 2, 4],  # Corners à 2 mouvements du coin DRB (6)
		'3': [5]         # Corner à 3 mouvements du coin DRB (6)
	},
	{
		'1': [2, 4, 6],  # Corners à 1 mouvement du coin DBL (7)
		'2': [0, 1, 5],  # Corners à 2 mouvements du coin DBL (7)
		'3': [3]         # Corner à 3 mouvements du coin DBL (7)
	}
]

# Ex. 0 -> 4:
#	0 -> 1 -> 4
#	0 -> 5 -> 4


def find_paths_of_length_x_to_goal(graph, start, goal, distance, path=None, all_paths=None, allowed_back: bool=False):
	if path is None:
		path = []
	if all_paths is None:
		all_paths = []

	path.append(str(start))


	if len(path) - 1 == distance:
		if str(start) == str(goal):
			all_paths.append(path.copy())
	else:
		for neighbor in graph[f'{start}']:
			if neighbor not in path or allowed_back:
				# print(graph[f'{start}'][f'{neighbor}'])
				find_paths_of_length_x_to_goal(graph, neighbor, goal, distance, path, all_paths, allowed_back)

	# Backtrack: retirer le nœud courant du chemin
	path.pop()

	return all_paths


def convert_path_to_sequences_lst(path: list):
	lists = []
	for i in range(len(path) - 1):
		lists.append(neighboring_corner[path[i]][path[i + 1]])

	# print(lists)
	lists_sequences = []


	for combination in itertools.product(*lists):
		# print(" ".join(combination))
		lists_sequences.append(" ".join(combination))
	return lists_sequences


# print(convert_path_to_sequences_lst(['0', '1', '4']))
# U' U'
# U' B
# R U'
# R B




# # Chercher tous les chemins de longueur 2 depuis le nœud 0 pour atteindre le nœud 4
# all_paths_distance_2_to_4 = find_paths_of_length_x_to_goal(neighboring_corner, '0', '4', 2)

# # Afficher les chemins trouvés
# for path in all_paths_distance_2_to_4:
#     print(f"Chemin: {path}")


def find_distances_corner(distances_map: dict, pos: int):
	for i in range(1, 4):
		if (pos in distances_map[f"{i}"]):
			return i
	return -1

class RubikCorner:
	# 0: Up Right Front
	# 1: Up Back Right
	# 2: Down Left Front
	# 3: Down Front Right
	# 4: Up Left Back
	# 5: Up Front Left
	# 6: Down Right Back
	# 7: Down Back Left

	# 0: urf, 1: ubr, 2: dlf, 3: dfr, 4: ulb, 5: ufl, 6: drb, 7: dbl
	def __init__(self, rubik: Rubik, default_position: int, target_position: int, expect_tuple: tuple) -> None:
		self.default_position = default_position
		self.target_position = target_position
		self.expect_tuple = expect_tuple
		self.target_rotation = 42
		self.distance = self.get_distance()
		self.all_paths = []
		self.rubik = rubik
		# print(self.distance)
		# if rubik.getCorners()[target_position] == expect_tuple:
		# 	print("UUUU")

		if (self.distance == -1):
			return
		if (default_position == target_position):
			# print("HERE1")
			self.all_paths = find_paths_of_length_x_to_goal(neighboring_corner, default_position, target_position, 2, None, None, True)
			# print(self.all_paths)
		else:
			for i in range(1, 4):
				self.all_paths.extend(find_paths_of_length_x_to_goal(neighboring_corner, default_position, target_position, 4 - i, None, None))
				# self.all_paths = find_paths_of_length_x_to_goal(neighboring_corner, default_position, target_position, i, None, None)

		if self.all_paths == []:
			return

		self.sequences = self.get_all_combinaisons()

		self.find_perfect_rotation()

		# print(f"DISTANCE BETWEEN {self.default_position} -> {self.target_position} : {self.distance}")
		# print(f"ROTATION -> {self.target_rotation}")
		# print(self.sequences)



	def get_distance(self) -> int:
		if (self.default_position == self.target_position):
			return 0
		return find_distances_corner(tab_pos_corners[self.default_position], self.target_position)
		# print(distance_to_default)

	def get_all_combinaisons(self) -> list[str]:
		all_sequences = []
		for path in self.all_paths:
			path_sequences = convert_path_to_sequences_lst(path)
			for sequence in path_sequences:
				all_sequences.append(sequence)
		return all_sequences

	def find_perfect_rotation(self):
		import copy
		rubikSolved = copy.deepcopy(Rubik())
		for sequence in self.sequences:
			rubikSolved.restore()
			rubikSolved.apply_sequences(sequences=sequence)
			if rubikSolved.getCorners()[self.target_position] == self.expect_tuple:
				# print(f"FIND - {rubikSolved.cornerOrt[self.target_position]}")
				# print(f"{rubikSolved.getCorners()[self.target_position]} -- {self.expect_tuple}")
				# if rubikSolved.cornerOrt[self.target_position] < self.target_rotation:
				self.target_rotation = rubikSolved.cornerOrt[self.target_position]
				# if self.distance == 1:
				# 	self.target_rotation = 0
		# 		if self.target_rotation == 0:
		# 			return
		# if self.target_rotation == 42:
		# 	self.target_rotation = 0

if __name__ == "__main__":
	# 0: Up Right Front
	# 1: Up Back Right
	# 2: Down Left Front
	# 3: Down Front Right
	# 4: Up Left Back
	# 5: Up Front Left
	# 6: Down Right Back
	# 7: Down Back Left
	# RubikCorner(0, 4, ())
	# RubikCorner(0, 7, ())
	# RubikCorner(0, 0, ())
	# RubikCorner(0, 7, ('W', 'B', 'O'))
	# RubikCorner(1, 6, ('W', 'G', 'O'))
	# RubikCorner(2, 3, ('Y', 'B', 'R'))
	# RubikCorner(0, 0, ('B', 'W', 'O'))
	# RubikCorner(0, 0, ('W', 'O', 'B'))
	pass

