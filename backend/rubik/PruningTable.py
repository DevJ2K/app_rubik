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

def main():
    nbStates = 2**12
    pruning_table = PruningTable(nbStates)
    initial_state = 0
    pruning_table.generate_table(initial_state, getNeighborsEdgeOrientation)
    return pruning_table