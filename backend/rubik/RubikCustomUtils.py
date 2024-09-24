from Rubik import Rubik

def same_cube(cube1: tuple, cube2: tuple):
	return sorted(cube1) == sorted(cube2)


def update_corners_pos(rubikSolved: Rubik, rubik: Rubik):
	new_corners_pos = rubik.cornerPos

	rubikSolvedCorners = rubikSolved.getCorners()
	rubikCorners = rubik.getCorners()
	for i in range(len(rubikSolvedCorners)):
		for j in range(len(rubikCorners)):
			# print(rubikSolvedCorners[i])
			# print(cube)
			# print(same_cube(rubikSolvedCorners[i], cube))
			if (same_cube(rubikSolvedCorners[i], rubikCorners[j])):
				new_corners_pos[j] = i
	return new_corners_pos

def update_edges_pos(rubikSolved: Rubik, rubik: Rubik):
	new_edges_pos = rubik.edgePos

	rubikSolvedEdges = rubikSolved.getEdges()
	rubikEdges = rubik.getEdges()
	for i in range(len(rubikSolvedEdges)):
		for j in range(len(rubikEdges)):
			if (same_cube(rubikSolvedEdges[i], rubikEdges[j])):
				new_edges_pos[j] = i
	return new_edges_pos


def update_edges_orientation(rubikSolved: Rubik, rubik: Rubik):
	new_edges_ort = rubik.edgeOrt

	rubikSolvedEdges = rubikSolved.getEdges()
	rubikEdges = rubik.getEdges()
	for i in range(len(rubikSolvedEdges)):
		for j in range(len(rubikEdges)):
			if (same_cube(rubikSolvedEdges[i], rubikEdges[j])):
				new_edges_ort[j] = int(rubikSolvedEdges[i] != rubikEdges[j])
	return new_edges_ort


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

tab_movements_distance = [
    {
        '1': ["F'", "R", "R'"],  # Mouvements en 1 étape depuis URF qui permet d'atteindre UFL, UBR, DFR
        '2': ["F' U", "R R", "F F"],  # Mouvements en 2 étapes qui permet d'atteindre UBL, DFL, DBR
        '3': ["F' L' B"]  # Mouvements en 3 étapes (modifié) DBL
    },
    {
        '1': ["U", "R", "R'"],  # UBR qui permet d'atteindre URF, UFL, DFR
        '2': ["U R", "R U'", "U F"],  # Mouvements en 2 étapes qui permet d'atteindre UBL, DBR, DFL
        '3': ["U R' F"]  # Mouvements en 3 étapes (modifié) DFL
    },
    {
        '1': ["D'", "F", "D"],  # DLF qui permet d'atteindre DFR, DBR, UFL
        '2': ["D' F'", "L D", "F L'"],  # Mouvements en 2 étapes qui permet d'atteindre DFL, DBL, ULB
        '3': ["D' F L"]  # Mouvements en 3 étapes (modifié) DBL
    },
    {
        '1': ["D", "R'", "F'"],  # DFR qui permet d'atteindre URF, UBR, DLF
        '2': ["D R'", "F' D", "R' F"],  # Mouvements en 2 étapes qui permet d'atteindre DFL, DBR, UFL
        '3': ["D F' R"]  # Mouvements en 3 étapes (modifié) DBR
    },
    {
        '1': ["L", "U", "B"],  # ULB qui permet d'atteindre UFL, DBL, DLF
        '2': ["L U", "B U'", "L' B"],  # Mouvements en 2 étapes qui permet d'atteindre UBL, DFR, DFL
        '3': ["L U B"]  # Mouvements en 3 étapes (modifié) DFR
    },
    {
        '1': ["F", "L", "U'"],  # UFL qui permet d'atteindre URF, ULB, DFR
        '2': ["F U'", "L U'", "F' L"],  # Mouvements en 2 étapes qui permet d'atteindre UBR, DBR, DLF
        '3': ["F L U"]  # Mouvements en 3 étapes (modifié) DBR
    },
    {
        '1': ["D'", "R", "B"],  # DRB qui permet d'atteindre DFR, DBL, URF
        '2': ["D' R", "B D'", "R B'"],  # Mouvements en 2 étapes qui permet d'atteindre DFL, UBR, ULB
        '3': ["D' R B"]  # Mouvements en 3 étapes (modifié) DFL
    },
    {
        '1': ["D", "B'", "L"],  # DBL qui permet d'atteindre DLF, DRB, ULB
        '2': ["D B'", "L D'", "B' L"],  # Mouvements en 2 étapes qui permet d'atteindre UBL, DFR, UFL
        '3': ["D B' L"]  # Mouvements en 3 étapes (modifié) UFR
    }
]





def find_distances_corner(tuple3, distances_map: dict, pos: int):
	# print(tuple3)
	# print(distances_map)
	# print(pos)
	for i in range(1, 4):
		if (pos in distances_map[f"{i}"]):
			return i
	return -1

def find_perfect_rotation(rubikSolved_: Rubik, moves_to_try: list[str], initial_tuple: tuple, search_tuple: tuple, pos_search: int, nb_moves: int):
	import copy
	# print(f"==========={moves_to_try}=========")
	rubikSolved = copy.deepcopy(Rubik())
	for moves in moves_to_try:
		rubikSolved.restore()
		rubikSolved.apply_sequences(moves)

		rubikSolvedCorners = rubikSolved.getCorners()
		# print(f"{initial_tuple} - {rubikSolvedCorners[pos_search]} - {search_tuple}")
		# print(rubikSolvedCorners)
		if (same_cube(rubikSolvedCorners[pos_search], search_tuple)):
			ortTupleAfterMoves = rubikSolved.cornerOrt[pos_search]
			print(f"FIND AFTER MAKING : {moves} - {ortTupleAfterMoves}")
			if initial_tuple == search_tuple:
				return 0




			if ortTupleAfterMoves == search_tuple:
				return ortTupleAfterMoves
			# print(ortTupleAfterMoves)
			print("==")
			return 2 if ortTupleAfterMoves == 1 else 1
	return 42


def ultimate_backtracking(initial_pos: int, search_tuple: tuple, distance: int) -> int:
	rubik = Rubik()
	pass


def update_corners_orientation(rubikSolved: Rubik, rubik: Rubik):

	# UD | LR | BF

	# 0: urf, 1: ubr, 2: dlf, 3: dfr, 4: ulb, 5: ufl, 6: drb, 7: dbl
	# new_corners_ort = rubik.cornerOrt
	new_corners_ort = [-1 for _ in range(8)]

	rubikSolvedCorners = rubikSolved.getCorners()
	rubikCorners = rubik.getCorners()
	for i in range(len(rubikSolvedCorners)):
		for j in range(len(rubikCorners)):
			if (new_corners_ort[j] == -1 and same_cube(rubikSolvedCorners[i], rubikCorners[j])):
				# BIEN POSITIONNE
				if (i == j and rubikSolvedCorners[i] == rubikCorners[j]):
					new_corners_ort[j] = 0
				else:
					distance_to_default = find_distances_corner(rubikSolvedCorners[i], tab_pos_corners[i], j)

				# if (i == j):
				# 	if (rubikSolvedCorners[i] == rubikCorners[j]):
				# 		new_corners_ort[j] = 0
				# 	else:
				# 		new_corners_ort[j] = 3 % i if i != 0 else 2
				# else:
					# print(i)
					# distance_to_default = find_distances_corner(rubikSolvedCorners[i], tab_pos_corners[i], j)
					# print(f"{i} - {j} : DISTANCE = {distance_to_default}")
					# new_corners_ort[j] = find_perfect_rotation(rubikSolved, tab_movements_distance[i][f'{distance_to_default}'], rubikSolvedCorners[i], rubikCorners[j], j, distance_to_default)
					pass


			# else:
			# 	new_corners_ort[j] = -1
				# new_corners_ort[j] = int(rubikSolvedCorners[i] != rubikCorners[j])
	# return None
	return new_corners_ort
