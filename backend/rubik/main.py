#!/usr/bin/env python3
import sys
from Rubik import Rubik
from ErrorManager import NotationError, SequenceError, InvalidRubikError
import time

def basic_function():
	print("It's work !")

def usage(err: str) -> None:
	print(f"\033[1m\033[31m{err} arguments\n\t\033[1m\033[36mUsage: ./main \"F U B' 2D\"\033[0m")
	exit(1)

def main():
	try:
		startTime = time.time()
		if len(sys.argv) > 2:
			usage("Too much")
		if len(sys.argv) < 2:
			usage("Not enough")
		cube = Rubik()
		cube.apply_sequences(sys.argv[1])
		cube.formatSolution(cube.solve())
		solution = " ".join(cube.formatedSolution)
		print(f"\033[1m\033[36mSolution: \033[0m{solution}")
		print(f"\033[1m\033[35mNombre de coups: \033[0m{len(cube.formatedSolution)}")
		print(f"\033[1m\033[32mTemps écoulé: \033[0m{time.time() - startTime:.3f} secondes")
		# print(f"\033[1m\033[33mCube résolu ? : \033[0m{cube.isSolved()}")
	except (NotationError, InvalidRubikError, SequenceError) as e:
		print(e)

if __name__ == "__main__":
	# basic_function()
	main()
