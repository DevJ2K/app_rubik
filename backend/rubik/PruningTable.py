from collections import deque
from Rubik import getNeighborsEdgeOrientation

class PruningTable:
    def __init__(self, nbStates) -> None:
        self.table = -1 * nbStates
    
    def generateTable(self, initialState, getNeighbors):
        self.table[initialState] = 0
        queue = deque([initialState])

        while queue:
            currentState = queue.popleft()
            currentDistance = self.table[currentState]

            neighbors = getNeighbors(currentState)

            for neighbor in neighbors:
                if self.table[neighbor] == -1:
                    self.table[neighbor] = currentDistance + 1
                    queue.append(neighbor)
            
    def getDistance(self, state):
        return self.table[state]

def generateEdgePruningTable():
    nbStates = 2**12
    pruningTable = PruningTable(nbStates)
    initialState = 0
    pruningTable.generate_table(initialState, getNeighborsEdgeOrientation)
    return pruningTable

def generateCornerPruningTable():
    nbStates = 3**7
    pruningTable = PruningTable(nbStates)
    initialState = 0
    pruningTable.generate_table(initialState, getNeighborsEdgeOrientation)
    return pruningTable