from collections import deque




def main():
	for phase in range(1, 4):
		try:
			with open('./database/phase' + str(phase), 'r') as file:
				q = deque()
				BFS(0, q)
		except FileNotFoundError:
			print(f'File {file} doesn\'t exist.')
		except PermissionError:
			print(f'Not enough permissions to open {file}')
		except Exception as e:
			print(f'Unexpected error: {e}')