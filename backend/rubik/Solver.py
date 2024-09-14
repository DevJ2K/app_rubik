from Rubik import Rubik

class Solver:
	def __init__(self, cube: Rubik) -> None:
		self.cube = cube
		self.phaseGoal = self.setPhaseGoal()
		self.phaseTable = []
		self.setPhaseTable()
	
	def setPhaseTable(self):
		try:
			for i in range(1, 4):
				tempDict = {}
				with open('./database/phase' + str(i), 'r') as file:
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
		phaseGoal = []
		temp = Rubik()
		for i in range(4):
			phaseGoal.append(self.getPhaseId(temp, i))
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
				print('here')
				return -1

	def idPhase1(self, cube: Rubik) -> int:
		id = 0
		for i in range(12):
			print(cube.edgeOrt[i], end=' ')
			id <<= 1
			id += cube.edgeOrt[i]
		print()
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

	
if __name__ == "__main__":
	pass
	cube = Rubik()
	solver = Solver(cube)
	
