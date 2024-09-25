from Rubik import Rubik

def print_corner(rubik: Rubik):
	string = ""
	rubik_corners = rubik.getCorners()
	for i in range(len(rubik.getCorners())):
		# string += f"{rubik_corners[i]} | p: {rubik.cornerPos[i]} | o: {rubik.cornerOrt[i]}\n"
		string += f"{rubik.cornerPos[i]}:{rubik_corners[i]} | "
	print(string)

def print_edges(rubik: Rubik):
	string = ""
	rubik_edges = rubik.getEdges()
	for i in range(len(rubik.getEdges())):
		string += f"{rubik.edgePos[i]}:{rubik_edges[i]} | "
	print(string)

def print_edges_ort(rubik: Rubik):
	string = ""
	rubik_edges = rubik.getEdges()
	for i in range(len(rubik.getEdges())):
		string += f"{rubik.edgeOrt[i]}:{rubik_edges[i]} | "
	print(string)

def print_corners_ort(rubik: Rubik):
	string = ""
	rubik_corners = rubik.getCorners()
	for i in range(len(rubik.getCorners())):
		string += f"{rubik.cornerPos[i]}-{rubik.cornerOrt[i]}:{rubik_corners[i]} | "
	print(string)

rubikSolved = Rubik()
print("=== RUBIK SOLVED ===")
# rubikSolved.apply_sequences("F")
# print_edges(rubikSolved)
# print_edges_ort(rubikSolved)
# print_corner(rubikSolved)
print_corners_ort(rubikSolved)


# R U L B U U
rubik1 = Rubik()
# rubik1.apply_sequences("R U L B U U")
# rubik1.apply_sequences("R U F' U'")
# rubik1.apply_sequences("R R D")
# rubik1.apply_sequences("R U")
rubik1.apply_sequences("U U' R B B' D D' D' R F' L L' U' U'")
# rubik1.apply_sequences("R R D")
# rubik1.visualize_cube()

# [
#     "U U' R B B' D D' D' R F' L L' U' U'"
# ]

print("=== RUBIK WITH MOVEMENTS ===")
# print_corner(rubik1)
# print_edges(rubik1)
# print_edges_ort(rubik1)
print_corners_ort(rubik1)

# R
# rubik2 = Rubik([
#     [
#         [
#             "3",
#             "3",
#             "5"
#         ],
#         [
#             "1",
#             "1",
#             "4"
#         ],
#         [
#             "6",
#             "6",
#             "4"
#         ]
#     ],
#     [
#         [
#             "5",
#             "5",
#             "5"
#         ],
#         [
#             "4",
#             "2",
#             "3"
#         ],
#         [
#             "4",
#             "2",
#             "6"
#         ]
#     ],
#     [
#         [
#             "1",
#             "1",
#             "5"
#         ],
#         [
#             "1",
#             "3",
#             "2"
#         ],
#         [
#             "3",
#             "3",
#             "2"
#         ]
#     ],
#     [
#         [
#             "1",
#             "6",
#             "6"
#         ],
#         [
#             "4",
#             "4",
#             "5"
#         ],
#         [
#             "2",
#             "2",
#             "2"
#         ]
#     ],
#     [
#         [
#             "1",
#             "4",
#             "4"
#         ],
#         [
#             "1",
#             "5",
#             "3"
#         ],
#         [
#             "4",
#             "5",
#             "2"
#         ]
#     ],
#     [
#         [
#             "1",
#             "5",
#             "3"
#         ],
#         [
#             "6",
#             "6",
#             "2"
#         ],
#         [
#             "6",
#             "6",
#             "3"
#         ]
#     ]
# ])

# R U
rubik2 = Rubik([
    [
        [
            "1",
            "1",
            "1"
        ],
        [
            "1",
            "1",
            "1"
        ],
        [
            "3",
            "3",
            "3"
        ]
    ],
    [
        [
            "4",
            "2",
            "2"
        ],
        [
            "4",
            "2",
            "2"
        ],
        [
            "4",
            "2",
            "2"
        ]
    ],
    [
        [
            "6",
            "6",
            "6"
        ],
        [
            "3",
            "3",
            "2"
        ],
        [
            "3",
            "3",
            "2"
        ]
    ],
    [
        [
            "5",
            "5",
            "5"
        ],
        [
            "1",
            "4",
            "4"
        ],
        [
            "1",
            "4",
            "4"
        ]
    ],
    [
        [
            "3",
            "3",
            "2"
        ],
        [
            "5",
            "5",
            "5"
        ],
        [
            "5",
            "5",
            "5"
        ]
    ],
    [
        [
            "1",
            "4",
            "4"
        ],
        [
            "6",
            "6",
            "6"
        ],
        [
            "6",
            "6",
            "6"
        ]
    ]
])

# # D' L'
# rubik2 = Rubik([
#     [
#         [
#             "3",
#             "1",
#             "1"
#         ],
#         [
#             "3",
#             "1",
#             "1"
#         ],
#         [
#             "6",
#             "1",
#             "1"
#         ]
#     ],
#     [
#         [
#             "2",
#             "2",
#             "4"
#         ],
#         [
#             "2",
#             "2",
#             "4"
#         ],
#         [
#             "2",
#             "2",
#             "5"
#         ]
#     ],
#     [
#         [
#             "2",
#             "3",
#             "3"
#         ],
#         [
#             "2",
#             "3",
#             "3"
#         ],
#         [
#             "2",
#             "6",
#             "6"
#         ]
#     ],
#     [
#         [
#             "4",
#             "4",
#             "1"
#         ],
#         [
#             "4",
#             "4",
#             "1"
#         ],
#         [
#             "5",
#             "5",
#             "1"
#         ]
#     ],
#     [
#         [
#             "5",
#             "5",
#             "3"
#         ],
#         [
#             "5",
#             "5",
#             "3"
#         ],
#         [
#             "5",
#             "5",
#             "3"
#         ]
#     ],
#     [
#         [
#             "6",
#             "6",
#             "6"
#         ],
#         [
#             "6",
#             "6",
#             "6"
#         ],
#         [
#             "4",
#             "4",
#             "4"
#         ]
#     ]
# ])

# # R R D
# rubik2 = Rubik([
#     [
#         [
#             "1",
#             "1",
#             "2"
#         ],
#         [
#             "1",
#             "1",
#             "2"
#         ],
#         [
#             "1",
#             "1",
#             "2"
#         ]
#     ],
#     [
#         [
#             "1",
#             "1",
#             "1"
#         ],
#         [
#             "2",
#             "2",
#             "2"
#         ],
#         [
#             "2",
#             "2",
#             "2"
#         ]
#     ],
#     [
#         [
#             "3",
#             "3",
#             "4"
#         ],
#         [
#             "3",
#             "3",
#             "4"
#         ],
#         [
#             "5",
#             "5",
#             "5"
#         ]
#     ],
#     [
#         [
#             "3",
#             "4",
#             "4"
#         ],
#         [
#             "3",
#             "4",
#             "4"
#         ],
#         [
#             "6",
#             "6",
#             "6"
#         ]
#     ],
#     [
#         [
#             "5",
#             "5",
#             "5"
#         ],
#         [
#             "5",
#             "5",
#             "5"
#         ],
#         [
#             "3",
#             "4",
#             "4"
#         ]
#     ],
#     [
#         [
#             "6",
#             "6",
#             "6"
#         ],
#         [
#             "6",
#             "6",
#             "6"
#         ],
#         [
#             "3",
#             "3",
#             "4"
#         ]
#     ]
# ])

# R R
# rubik2 = Rubik([
#     [
#         [
#             "1",
#             "1",
#             "2"
#         ],
#         [
#             "1",
#             "1",
#             "2"
#         ],
#         [
#             "1",
#             "1",
#             "2"
#         ]
#     ],
#     [
#         [
#             "1",
#             "2",
#             "2"
#         ],
#         [
#             "1",
#             "2",
#             "2"
#         ],
#         [
#             "1",
#             "2",
#             "2"
#         ]
#     ],
#     [
#         [
#             "3",
#             "3",
#             "4"
#         ],
#         [
#             "3",
#             "3",
#             "4"
#         ],
#         [
#             "3",
#             "3",
#             "4"
#         ]
#     ],
#     [
#         [
#             "3",
#             "4",
#             "4"
#         ],
#         [
#             "3",
#             "4",
#             "4"
#         ],
#         [
#             "3",
#             "4",
#             "4"
#         ]
#     ],
#     [
#         [
#             "5",
#             "5",
#             "5"
#         ],
#         [
#             "5",
#             "5",
#             "5"
#         ],
#         [
#             "5",
#             "5",
#             "5"
#         ]
#     ],
#     [
#         [
#             "6",
#             "6",
#             "6"
#         ],
#         [
#             "6",
#             "6",
#             "6"
#         ],
#         [
#             "6",
#             "6",
#             "6"
#         ]
#     ]
# ])

rubik2 = Rubik([
    [
        [
            "4",
            "4",
            "1"
        ],
        [
            "2",
            "1",
            "1"
        ],
        [
            "2",
            "1",
            "1"
        ]
    ],
    [
        [
            "1",
            "2",
            "2"
        ],
        [
            "1",
            "2",
            "2"
        ],
        [
            "2",
            "5",
            "5"
        ]
    ],
    [
        [
            "3",
            "4",
            "4"
        ],
        [
            "3",
            "3",
            "6"
        ],
        [
            "3",
            "3",
            "6"
        ]
    ],
    [
        [
            "4",
            "2",
            "2"
        ],
        [
            "3",
            "4",
            "4"
        ],
        [
            "3",
            "5",
            "5"
        ]
    ],
    [
        [
            "5",
            "6",
            "6"
        ],
        [
            "5",
            "5",
            "1"
        ],
        [
            "3",
            "3",
            "1"
        ]
    ],
    [
        [
            "5",
            "5",
            "6"
        ],
        [
            "4",
            "6",
            "6"
        ],
        [
            "4",
            "6",
            "6"
        ]
    ]
])

print("=== RUBIK 2 ===")

rubik2.initCube()
# print_corner(rubik2)
# print_edges(rubik2)
# print_edges_ort(rubik2)
print_corners_ort(rubik2)

# rubik1.visualize_cube()
# print("=== RUBIK WITH CUSTOM SETUP ===")
# rubik3 = Rubik([
#     [
#         [
#             "1",
#             "1",
#             "3"
#         ],
#         [
#             "1",
#             "1",
#             "3"
#         ],
#         [
#             "1",
#             "1",
#             "3"
#         ]
#     ],
#     [
#         [
#             "4",
#             "2",
#             "2"
#         ],
#         [
#             "4",
#             "2",
#             "2"
#         ],
#         [
#             "4",
#             "2",
#             "2"
#         ]
#     ],
#     [
#         [
#             "3",
#             "3",
#             "2"
#         ],
#         [
#             "3",
#             "3",
#             "2"
#         ],
#         [
#             "3",
#             "3",
#             "2"
#         ]
#     ],
#     [
#         [
#             "1",
#             "4",
#             "4"
#         ],
#         [
#             "1",
#             "4",
#             "4"
#         ],
#         [
#             "1",
#             "4",
#             "4"
#         ]
#     ],
#     [
#         [
#             "5",
#             "5",
#             "5"
#         ],
#         [
#             "5",
#             "5",
#             "5"
#         ],
#         [
#             "5",
#             "5",
#             "5"
#         ]
#     ],
#     [
#         [
#             "6",
#             "6",
#             "6"
#         ],
#         [
#             "6",
#             "6",
#             "6"
#         ],
#         [
#             "6",
#             "6",
#             "6"
#         ]
#     ]
# ])

# print_corner(rubik3)
# rubik3.initCube()
# print_corner(rubik3)
# print_corners_ort(rubik3)

# print(rubik3.getCorners())
# print(rubik3.cornerPos)
# print(rubik3.edgeOrt, rubik3.cornerOrt, rubik3.edgePos, rubik3.cornerPos)
