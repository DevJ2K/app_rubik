from Rubik import Rubik

class Solver:
	def __init__(self, cube: Rubik) -> None:
		self.cube = cube.get_cube()
	
	def getEdgeOrientation(self):
		cube_up,cube_down,cube_front,cube_back,cube_left,cube_right = self.cube
		edges = [
			(cube_up[0][1], cube_back[0][1]),	
			(cube_up[1][2], cube_right[0][1]),
			(cube_up[2][1], cube_front[0][1]),
			(cube_up[1][0], cube_left[0][1]),	
			(cube_down[0][1], cube_front[2][1]),
			(cube_down[1][2], cube_right[2][1]),
			(cube_down[2][1], cube_back[2][1]),
			(cube_down[1][0], cube_left[2][1]),
			(cube_front[1][0], cube_left[1][2]),
			(cube_front[1][2], cube_right[1][0]),
			(cube_back[1][0], cube_left[1][0]),
			(cube_back[1][2], cube_right[1][2])
		]
		print(edges)
		orientation = []
		for edge in edges:
			if edge[0] in ['1', '2'] or edge[1] in ['1', '2']:
				orientation.append(0)
			else:
				orientation.append(1)
		return orientation
	
	def getCornerOrientation(self):
		cube_up,cube_down,cube_front,cube_back,cube_left,cube_right = self.cube
		corners = [
			(cube_up[0][0], cube_left[0][2], cube_back[0][0]),
			(cube_up[0][2], cube_right[0][2], cube_back[0][2]),
			(cube_up[2][2], cube_right[0][0], cube_front[0][2]),
			(cube_up[2][0], cube_left[0][0], cube_front[0][0]),
			(cube_down[0][0], cube_left[2][2], cube_front[2][0]),
			(cube_down[0][2], cube_right[2][2], cube_front[2][2]),
			(cube_down[2][2], cube_right[2][0], cube_back[2][2]),
			(cube_down[2][0], cube_left[2][0], cube_back[2][0])
		]

		orientation = []
		for corner in corners:
			if corner[0] in ['1', '2']:
				orientation.append(0)
			elif corner[1] in ['1', '2']:
				orientation.append(1)
			else:
				orientation.append(2)
		return orientation


if __name__ == "__main__":
	cube = Rubik()
	solver = Solver(cube)
	solver.getEdgeOrientation()
	
