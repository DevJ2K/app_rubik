import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from apply_rubik_moves import move_up


# def test_move_upuscule_without_prime():
# 	assert move_up([
# 	[
# 		['1', '2', '3'],
# 		['4', '5', '6'],
# 		['1', '1', '2'],
# 	],
# 	[
# 		['2', '2', '2'],
# 		['2', '2', '2'],
# 		['2', '2', '2'],
# 	],
# 	[
# 		['3', '3', '3'],
# 		['3', '3', '3'],
# 		['3', '3', '3'],
# 	],
# 	[
# 		['4', '4', '4'],
# 		['4', '4', '4'],
# 		['4', '4', '4'],
# 	],
# 	[
# 		['5', '5', '5'],
# 		['5', '5', '5'],
# 		['5', '5', '5'],
# 	],
# 	[
# 		['6', '6', '6'],
# 		['6', '6', '6'],
# 		['6', '6', '6'],
# 	]
# ]) == [
# 	[
# 		['1', '2', '3'],
# 		['4', '5', '6'],
# 		['1', '1', '2'],
# 	],
# 	[
# 		['2', '2', '2'],
# 		['2', '2', '2'],
# 		['2', '2', '2'],
# 	],
# 	[
# 		['3', '3', '3'],
# 		['3', '3', '3'],
# 		['3', '3', '3'],
# 	],
# 	[
# 		['4', '4', '4'],
# 		['4', '4', '4'],
# 		['4', '4', '4'],
# 	],
# 	[
# 		['5', '5', '5'],
# 		['5', '5', '5'],
# 		['5', '5', '5'],
# 	],
# 	[
# 		['6', '6', '6'],
# 		['6', '6', '6'],
# 		['6', '6', '6'],
# 	]
# ]
