from collections import deque
from Solver import Solver
from Rubik import Rubik

def main():
	cube = Rubik()
	solver = Solver(cube)
	for phase in range(1, 4):
		try:
			with open('./database/phase' + str(phase), 'r') as file:
				q = deque()
				solver.BFS(0, q, phase)
		except FileNotFoundError:
			print(f'File {file} doesn\'t exist.')
		except PermissionError:
			print(f'Not enough permissions to open {file}')
		except Exception as e:
			print(f'Unexpected error: {e}')