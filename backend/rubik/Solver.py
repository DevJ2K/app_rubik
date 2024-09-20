from Rubik import Rubik
from collections import deque
import copy

class Solver:
	def __init__(self, cube: Rubik) -> None:
		self.cube = cube
		self.phaseGoal = self.setPhaseGoal()
		self.phaseTable = [] * 4
		self.setPhaseTable()
		self.allowedMoves = [1] * 18
		self.phase = 1


	def setPhaseTable(self):
		try:
			for i in range(1, 5):
				tempDict = {}
				with open('./database/Phase ' + str(i), 'r') as file:
					for line in file:
						line = line.strip()
						if not line:
							continue
						try:
							hashStr, moves = line.split()
							hash = int(hashStr)
							tempDict[hash] = moves
						except ValueError:
							print(f'Format error : {line}')
					self.phaseTable.append(tempDict)
		except FileNotFoundError:
			print(f'File {file} doesn\'t exist.')
		except PermissionError:
			print(f'Not enough permissions to open {file}')
		except Exception as e:
			print(f'Unexpected error: {e}')


	def setPhaseGoal(self):
		phaseGoal = [0] * 5
		temp = Rubik()
		for i in range(4):
			phaseGoal[i] = self.getPhaseId(temp, i)
		return phaseGoal


	def getPhaseId(self, cube: Rubik, phase: int) -> int:
		match phase:
			case 1:
				return self.idPhase1(cube)
			case 2:
				return self.idPhase2(cube)
			case 3:
				return self.idPhase3(cube)
			case 4:
				return self.idPhase4(cube)
			case _:
				return -1


	def idPhase1(self, cube: Rubik) -> int:
		id = 0
		for i in range(12):
			id <<= 1
			id += cube.edgeOrt[i]
		return id


	def idPhase2(self, cube: Rubik) -> int:
		id = 0
		for i in range(8):
			id <<= 2
			id += cube.cornerOrt[i]
		for j in range(12):
			id <<= 2
			if cube.edgePos[j] < 8:
				id+=1
		return id


	def idPhase3(self, cube: Rubik) -> int:
		faces = "FRUBLD"
		cornerNames = ["URF", "UBR", "DLF", "DFR", "ULB", "UFL", "DRB", "DBL"]
		edgeNames = ["UF", "UR", "UB", "UL", "DF", "DR", "DB", "DL", "FR", "BR", "BL", "FL"]
		id = 0
		for i in range(7):
			for j in range(3):
				id <<= 1
				c = cornerNames[cube.cornerPos[i]][(cube.cornerOrt[i] + j) % 3]
				if not((c == cornerNames[i][j]) or c == faces[(faces.find(cornerNames[i][j]) + 3) % 6]):
					id+=1
		for i in range(11):
			for j in range(2):
				id <<= 1
				c = edgeNames[cube.edgePos[i]][(cube.edgeOrt[i] + j) % 2]
				if not((c == edgeNames[i][j]) or c == faces[(faces.find(edgeNames[i][j]) + 3) % 6]):
					id+=1
		for i in range(8):
			id <<= 1
			if cube.cornerPos[i] % 4 != i % 4:
				id +=1
		id <<= 1
		for i in range(8):
			for j in range(i + 1, 8):
				id ^= cube.cornerPos[i] > cube.cornerPos[j]
		return id


	def idPhase4(self, cube: Rubik) -> int:
		faces = "FRUBLD"
		cornerNames = ["URF", "UBR", "DLF", "DFR", "ULB", "UFL", "DRB", "DBL"]
		edgeNames = ["UF", "UR", "UB", "UL", "DF", "DR", "DB", "DL", "FR", "BR", "BL", "FL"]
		id = 0
		for i in range(8):
			for j in range(3):
				id <<= 1
				c = cornerNames[cube.cornerPos[i]][(cube.cornerOrt[i] + j) % 3]
				if c == faces[(faces.find(cornerNames[i][j]) + 3) % 6]:
					id += 1
		for i in range(12):
			for j in range(2):
				id <<= 1
				c = edgeNames[cube.edgePos[i]][(cube.edgeOrt[i] + j) % 2]
				if c == faces[(faces.find(edgeNames[i][j]) + 3) % 6]:
					id += 1
		return id


	def loadFile(self, phase: int):
		try:
			file = open('./database/Phase ' + str(phase + 1), 'w')
			return file
		except FileNotFoundError:
			print(f'File {file} doesn\'t exist.')
		except PermissionError:
			print(f'Not enough permissions to open {file}')
		except Exception as e:
			print(f'Unexpected error: {e}')


	def nextPhase(self, phase):
		match phase:
			case 0: #phase 2
				self.allowedMoves[0] = 0
				self.allowedMoves[2] = 0
				self.allowedMoves[9] = 0
				self.allowedMoves[11] = 0
			case 1:
				self.allowedMoves[3] = 0
				self.allowedMoves[5] = 0
				self.allowedMoves[12] = 0
				self.allowedMoves[14] = 0
			case 2:
				self.allowedMoves[6] = 0
				self.allowedMoves[8] = 0
				self.allowedMoves[15] = 0
				self.allowedMoves[17] = 0
			case _:
				return


	def BFS(self, step: int, queue: deque, phase: int, outfile):
		moves = ["F", "R", "U", "B", "L", "D"]
		
		if step == 0:
			id = self.getPhaseId(queue[0], phase + 1)
			outfile.write(str(id) + " " + "I" + '\n')
			self.phaseTable[phase][id] = ""
		next = deque()
		while queue:
			curr = queue.pop()
			count = 0
			for i in range(6):
				for j in range(3):
					curr.applyMultipleMoves(moves[i], 1)
					if self.allowedMoves[count] == 1:
						id = self.getPhaseId(curr, phase + 1)
						if id not in self.phaseTable[phase]: #not found
							newState = copy.deepcopy(curr)
							newState.movesList = moves[i] + str(3 - j) + newState.movesList
							outfile.write(str(id) + " " + newState.movesList + '\n')
							self.phaseTable[phase].update({id: newState.movesList})
							next.append(newState)
					count += 1
				curr.applyMultipleMoves(moves[i], 1)
		if len(next) == 0:
			return curr
		return self.BFS(step + 1, next, phase, outfile)


if __name__ == "__main__":
	cube = Rubik()
	solver = Solver(cube)
	for phase in range(4):
		cube = Rubik()
		queue = deque()
		outfile = solver.loadFile(phase)
		queue.append(cube)
		solver.phaseTable = [{}] * 4
		solver.BFS(0, queue, phase, outfile)
		solver.nextPhase(phase)
		print(f"Phase {phase + 1} done!")
	print("All phases done!")
