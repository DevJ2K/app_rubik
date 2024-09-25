# Will be a class who takes a corner has arguments and final position and returns movements to apply and distances.
from Rubik import Rubik


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


# Exemple 0 -> 5 : U, F'
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
	def __init__(self, default_position: int, target_position: int, expect_tuple: tuple) -> None:
		self.default_position = default_position
		self.target_position = target_position
		self.except_tuple = expect_tuple
		self.rubikSolved = Rubik()
