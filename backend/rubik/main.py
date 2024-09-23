#!/usr/bin/env python3
import sys
from Rubik import Rubik

def basic_function():
	print("It's work !")

def usage(err: str) -> None:
	print(f"\033[1m\033[31m{err} arguments\n\t\033[1m\033[36mUsage: ./rubik \"F U B' 2D\"\033[0m")
	exit(1)

def main():
	if len(sys.argv) > 2:
		usage("Too much")
	if len(sys.argv) < 2:
		usage("Not enough")
	cube = Rubik()
	cube.apply_sequences(sys.argv[1])
	cube.formatSolution(cube.solve())
	solution = " ".join(cube.formatedSolution)
	print(f"\033[1m\033[37m{solution}\033[0m")

if __name__ == "__main__":
	# basic_function()
	main()
