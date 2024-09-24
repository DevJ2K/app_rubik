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
