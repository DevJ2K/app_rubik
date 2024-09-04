import matplotlib.pyplot as plt
import numpy as np

colors = {
	'1': 'white',  # face 1
	'2': 'yellow', # face 2
	'3': 'blue',   # face 3
	'4': 'green',  # face 4
	'5': 'red',    # face 5
	'6': 'orange', # face 6
}

cube = [
	[
		'1', '1', '1',
		'1', '1', '1',
		'1', '1', '1',
	],
	[
		'2', '2', '2',
		'2', '2', '2',
		'2', '2', '2',
	],
	[
		'3', '3', '3',
		'3', '3', '3',
		'3', '3', '3',
	],
	[
		'4', '4', '4',
		'4', '4', '4',
		'4', '4', '4',
	],
	[
		'5', '5', '5',
		'5', '5', '5',
		'5', '5', '5',
	],
	[
		'6', '6', '6',
		'6', '6', '6',
		'6', '6', '6',
	],
]

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_title("Rubik cube visualizer")

x, y = np.meshgrid(cube[0],cube[1])

print(x)
print(y)

# plt.show()
