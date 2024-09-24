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
		'1': [2, 3, 5],
		'2': [1, 4, 6, 7]
	}
]

def update_corners_orientation(rubikSolved: Rubik, rubik: Rubik):

	# 0: urf, 1: ubr, 2: dlf, 3: dfr, 4: ulb, 5: ufl, 6: drb, 7: dbl
	new_corners_ort = rubik.cornerOrt

	rubikSolvedCorners = rubikSolved.getCorners()
	rubikCorners = rubik.getCorners()
	for i in range(len(rubikSolvedCorners)):
		for j in range(len(rubikCorners)):
			if (same_cube(rubikSolvedCorners[i], rubikCorners[j])):
				if (rubikSolvedCorners[i] == rubikCorners[j]):
					new_corners_ort[j] = 0

				new_corners_ort[j] = int(rubikSolvedCorners[i] != rubikCorners[j])
	return None
	return new_corners_ort
