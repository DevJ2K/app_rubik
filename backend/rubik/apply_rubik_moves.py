# self.cube_up: list[list[str]] = [
# 	['1', '1', '1'],
# 	['1', '1', '1'],
# 	['1', '1', '1'],
# ]
# self.cube_down: list[list[str]] = [
# 	['2', '2', '2'],
# 	['2', '2', '2'],
# 	['2', '2', '2'],
# ]
# self.cube_front: list[list[str]] = [
# 	['3', '3', '3'],
# 	['3', '3', '3'],
# 	['3', '3', '3'],
# ]
# self.cube_back: list[list[str]] = [
# 	['4', '4', '4'],
# 	['4', '4', '4'],
# 	['4', '4', '4'],
# ]
# self.cube_left: list[list[str]] = [
# 	['5', '5', '5'],
# 	['5', '5', '5'],
# 	['5', '5', '5'],
# ]
# self.cube_right: list[list[str]] = [
# 	['6', '6', '6'],
# 	['6', '6', '6'],
# 	['6', '6', '6'],
# ]

def rotate_face_only(face: list[list[str]], prime: bool = False) -> list[list[str]]:
	if prime:
		return [
			[face[0][2],face[1][2],face[2][2]],
			[face[0][1],face[1][1],face[2][1]],
			[face[0][0],face[1][0],face[2][0]],
		]
	else:
		return [
			[face[2][0],face[1][0],face[0][0]],
			[face[2][1],face[1][1],face[0][1]],
			[face[2][2],face[1][2],face[0][2]],
		]

def move_up(cube: list[list[list[str]]], move: str) -> list[list[list[str]]]:
	cube_up,cube_down,cube_front,cube_back,cube_left,cube_right = cube

	prime = "'" in move
	is_lower = move.islower()
	print(cube_up)
	# print(cube_down)
	# print(cube_front)
	# print(cube_back)
	# print(cube_left)
	# print(cube_right)
	if prime:
		cube_up = rotate_face_only(cube_up, prime)
		cube_front[0], cube_left[0], cube_back[0], cube_right[0] = cube_left[0], cube_back[0], cube_right[0], cube_front[0]
		if is_lower:
			cube_front[1], cube_left[1], cube_back[1], cube_right[1] = cube_left[1], cube_back[1], cube_right[1], cube_front[1]
	else:
		cube_up = rotate_face_only(cube_up, prime)
		cube_front[0], cube_left[0], cube_back[0], cube_right[0] = cube_right[0], cube_front[0], cube_left[0], cube_back[0]
		if is_lower:
			cube_front[1], cube_left[1], cube_back[1], cube_right[1] = cube_right[1], cube_front[1], cube_left[1], cube_back[1]

	print(cube_up)
	return [
		cube_up,
		cube_down,
		cube_front,
		cube_back,
		cube_left,
		cube_right
	]

# lst1 = [1, 2]
# lst2 = [3, 4]


# def new_list():
# 	return [
# 		[5, 6],
# 		[7, 8],
# 	]

# print(lst1, lst2)
# lst1, lst2 = new_list()
# print(lst1, lst2)

