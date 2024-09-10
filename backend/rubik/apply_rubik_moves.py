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
	"""
    This function takes a rubiks face as input and
	rotate this one depending on direction

    Parameters:
    face (list[list[str]]): The face of the rubik's cube to rotate
    prime (bool): If True -> counterclockwise.

    Returns:
    list[list[str]]: The new rotated face.
    """
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
	"""
    This function performs a rotation of the top face of a Rubik's cube and swaps
    the corresponding rows of the adjacent faces depending on the direction
	of the move (clockwise or counterclockwise).

    Parameters:
    cube (list[list[list[str]]]): The Rubik's cube represented as a list of 6 faces,
                                  each face being a 2D matrix of strings.
    move (str): Specifies the move to be applied. If the string contains a "'",
                it indicates a counterclockwise rotation; otherwise, it's clockwise.

    Returns:
    list[list[list[str]]]: The updated cube after rotating the top face and swapping
                           the corresponding rows of adjacent faces.
	"""
	cube_up,cube_down,cube_front,cube_back,cube_left,cube_right = cube
	prime = "'" in move

	if prime:
		cube_up = rotate_face_only(cube_up, prime)
		cube_front[0], cube_left[0], cube_back[0], cube_right[0] = cube_left[0], cube_back[0], cube_right[0], cube_front[0]
	else:
		cube_up = rotate_face_only(cube_up, prime)
		cube_front[0], cube_left[0], cube_back[0], cube_right[0] = cube_right[0], cube_front[0], cube_left[0], cube_back[0]

	# print(cube_up)
	return [
		cube_up,
		cube_down,
		cube_front,
		cube_back,
		cube_left,
		cube_right
	]

def move_down(cube: list[list[list[str]]], move: str) -> list[list[list[str]]]:
	"""
    This function performs a rotation of the bottom face of a Rubik's cube and swaps
    the corresponding rows of the adjacent faces depending on the direction
	of the move (clockwise or counterclockwise).

    Parameters:
    cube (list[list[list[str]]]): The Rubik's cube represented as a list of 6 faces,
                                  each face being a 2D matrix of strings.
    move (str): Specifies the move to be applied. If the string contains a "'",
                it indicates a counterclockwise rotation; otherwise, it's clockwise.

    Returns:
    list[list[list[str]]]: The updated cube after rotating the top face and swapping
                           the corresponding rows of adjacent faces.
	"""
	cube_up,cube_down,cube_front,cube_back,cube_left,cube_right = cube
	prime = "'" in move

	if prime:
		cube_down = rotate_face_only(cube_down, prime)
		cube_front[2], cube_left[2], cube_back[2], cube_right[2] = cube_right[2], cube_front[2], cube_left[2], cube_back[2]
	else:
		cube_down = rotate_face_only(cube_down, prime)
		cube_front[2], cube_left[2], cube_back[2], cube_right[2] = cube_left[2], cube_back[2], cube_right[2], cube_front[2]

	# print(cube_down)
	return [
		cube_up,
		cube_down,
		cube_front,
		cube_back,
		cube_left,
		cube_right
	]

def move_right(cube: list[list[list[str]]], move: str) -> list[list[list[str]]]:
	"""
    This function performs a rotation of the right face of a Rubik's cube and swaps
    the corresponding rows of the adjacent faces depending on the direction
	of the move (clockwise or counterclockwise).

    Parameters:
    cube (list[list[list[str]]]): The Rubik's cube represented as a list of 6 faces,
                                  each face being a 2D matrix of strings.
    move (str): Specifies the move to be applied. If the string contains a "'",
                it indicates a counterclockwise rotation; otherwise, it's clockwise.

    Returns:
    list[list[list[str]]]: The updated cube after rotating the top face and swapping
                           the corresponding rows of adjacent faces.
	"""
	cube_up,cube_down,cube_front,cube_back,cube_left,cube_right = cube
	prime = "'" in move

	if prime:
		cube_right = rotate_face_only(cube_right, prime)
		(
			cube_front[0][2], cube_front[1][2], cube_front[2][2],
			cube_up[0][2], cube_up[1][2], cube_up[2][2],
			cube_back[0][2], cube_back[1][2], cube_back[2][2],
			cube_down[0][2], cube_down[1][2], cube_down[2][2]
		) = (
			cube_up[0][2], cube_up[1][2], cube_up[2][2],
			cube_back[0][2], cube_back[1][2], cube_back[2][2],
			cube_down[0][2], cube_down[1][2], cube_down[2][2],
			cube_front[0][2], cube_front[1][2], cube_front[2][2]
		)
	else:
		cube_right = rotate_face_only(cube_right, prime)
		(
			cube_front[0][2], cube_front[1][2], cube_front[2][2],
			cube_up[0][2], cube_up[1][2], cube_up[2][2],
			cube_back[0][2], cube_back[1][2], cube_back[2][2],
			cube_down[0][2], cube_down[1][2], cube_down[2][2]
		) = (
			cube_down[0][2], cube_down[1][2], cube_down[2][2],
			cube_front[0][2], cube_front[1][2], cube_front[2][2],
			cube_up[0][2], cube_up[1][2], cube_up[2][2],
			cube_back[0][2], cube_back[1][2], cube_back[2][2]
		)

	# printcube_right)
	return [
		cube_up,
		cube_down,
		cube_front,
		cube_back,
		cube_left,
		cube_right
	]

def move_left(cube: list[list[list[str]]], move: str) -> list[list[list[str]]]:
	"""
    This function performs a rotation of the left face of a Rubik's cube and swaps
    the corresponding rows of the adjacent faces depending on the direction
	of the move (clockwise or counterclockwise).

    Parameters:
    cube (list[list[list[str]]]): The Rubik's cube represented as a list of 6 faces,
                                  each face being a 2D matrix of strings.
    move (str): Specifies the move to be applied. If the string contains a "'",
                it indicates a counterclockwise rotation; otherwise, it's clockwise.

    Returns:
    list[list[list[str]]]: The updated cube after rotating the top face and swapping
                           the corresponding rows of adjacent faces.
	"""
	cube_up,cube_down,cube_front,cube_back,cube_left,cube_right = cube
	prime = "'" in move

	if prime:
		cube_left = rotate_face_only(cube_left, prime)
		(
			cube_front[0][0], cube_front[1][0], cube_front[2][0],
			cube_up[0][0], cube_up[1][0], cube_up[2][0],
			cube_back[0][0], cube_back[1][0], cube_back[2][0],
			cube_down[0][0], cube_down[1][0], cube_down[2][0]
		) = (
			cube_down[0][0], cube_down[1][0], cube_down[2][0],
			cube_front[0][0], cube_front[1][0], cube_front[2][0],
			cube_up[0][0], cube_up[1][0], cube_up[2][0],
			cube_back[0][0], cube_back[1][0], cube_back[2][0]
		)

	else:
		cube_left = rotate_face_only(cube_left, prime)
		(
			cube_front[0][0], cube_front[1][0], cube_front[2][0],
			cube_up[0][0], cube_up[1][0], cube_up[2][0],
			cube_back[0][0], cube_back[1][0], cube_back[2][0],
			cube_down[0][0], cube_down[1][0], cube_down[2][0]
		) = (
			cube_up[0][0], cube_up[1][0], cube_up[2][0],
			cube_back[0][0], cube_back[1][0], cube_back[2][0],
			cube_down[0][0], cube_down[1][0], cube_down[2][0],
			cube_front[0][0], cube_front[1][0], cube_front[2][0]
		)

	# printcube_left)
	return [
		cube_up,
		cube_down,
		cube_front,
		cube_back,
		cube_left,
		cube_right
	]

def move_front(cube: list[list[list[str]]], move: str) -> list[list[list[str]]]:
	"""
    This function performs a rotation of the front face of a Rubik's cube and swaps
    the corresponding rows of the adjacent faces depending on the direction
	of the move (clockwise or counterclockwise).

    Parameters:
    cube (list[list[list[str]]]): The Rubik's cube represented as a list of 6 faces,
                                  each face being a 2D matrix of strings.
    move (str): Specifies the move to be applied. If the string contains a "'",
                it indicates a counterclockwise rotation; otherwise, it's clockwise.

    Returns:
    list[list[list[str]]]: The updated cube after rotating the top face and swapping
                           the corresponding rows of adjacent faces.
	"""
	cube_up,cube_down,cube_front,cube_back,cube_left,cube_right = cube
	prime = "'" in move

	if prime:
		cube_front = rotate_face_only(cube_front, prime)
		(cube_up[2],
		cube_left[2][2], cube_left[1][2], cube_left[0][2],
		cube_down[2],
		cube_right[0][0], cube_right[1][0], cube_right[2][0]
		) = (
		[cube_right[0][0], cube_right[1][0], cube_right[2][0]],
		cube_up[2][0], cube_up[2][1], cube_up[2][2],
		[cube_left[2][2], cube_left[1][2], cube_left[0][2]],
		cube_down[2][0], cube_down[2][1], cube_down[2][2]
		)
	else:
		cube_front = rotate_face_only(cube_front, prime)
		(
			cube_up[2],
			cube_right[0][0], cube_right[1][0], cube_right[2][0],
			cube_down[2],
			cube_left[0][2], cube_left[1][2], cube_left[2][2]
		) = (
			[cube_left[2][2], cube_left[1][2], cube_left[0][2]],
			cube_up[2][0], cube_up[2][1], cube_up[2][2],
			[cube_right[0][0], cube_right[1][0], cube_right[2][0]],
			cube_down[2][2], cube_down[2][1], cube_down[2][0]
		)

	# print(cube_front)
	return [
		cube_up,
		cube_down,
		cube_front,
		cube_back,
		cube_left,
		cube_right
	]

def move_back(cube: list[list[list[str]]], move: str) -> list[list[list[str]]]:
	"""
    This function performs a rotation of the back face of a Rubik's cube and swaps
    the corresponding rows of the adjacent faces depending on the direction
	of the move (clockwise or counterclockwise).

    Parameters:
    cube (list[list[list[str]]]): The Rubik's cube represented as a list of 6 faces,
                                  each face being a 2D matrix of strings.
    move (str): Specifies the move to be applied. If the string contains a "'",
                it indicates a counterclockwise rotation; otherwise, it's clockwise.

    Returns:
    list[list[list[str]]]: The updated cube after rotating the top face and swapping
                           the corresponding rows of adjacent faces.
	"""
	cube_up,cube_down,cube_front,cube_back,cube_left,cube_right = cube
	prime = "'" in move

	if prime:
		cube_back = rotate_face_only(cube_back, prime)
		(
			cube_up[0],
			cube_right[0][2], cube_right[1][2], cube_right[2][2],
			cube_down[0],
			cube_left[2][0], cube_left[1][0], cube_left[0][0]
		) = (
			[cube_left[2][0], cube_left[1][0], cube_left[0][0]],
			cube_up[0][0], cube_up[0][1], cube_up[0][2],
			[cube_right[0][2], cube_right[1][2], cube_right[2][2]],
			cube_down[0][0], cube_down[0][1], cube_down[0][2]
		)
	else:
		cube_back = rotate_face_only(cube_back, prime)
		(
			cube_up[0],
			cube_right[0][2], cube_right[1][2], cube_right[2][2],
			cube_down[0],
			cube_left[0][0], cube_left[1][0], cube_left[2][0]
		) = (
			[cube_right[0][2], cube_right[1][2], cube_right[2][2]],
			cube_down[0][0], cube_down[0][1], cube_down[0][2],
			[cube_left[2][0], cube_left[1][0], cube_left[0][0]],
			cube_up[0][2], cube_up[0][1], cube_up[0][0]
		)

	# print(cube_back)
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
