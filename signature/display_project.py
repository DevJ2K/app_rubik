import time
import subprocess

BHGREEN = "\033[1;32m"
BHYELLOW = "\033[1;33m"
BHWHITE = "\033[1;37m"
BHBLUE = "\033[1;34m"
BHCYAN = "\033[7;36m"
BHPINK = "\033[1;35m"
BHRED = "\033[1;31m"
BHORANGE = "\033[1;91m"
BHGRAY = "\033[1;90m"
BHBRIGHTBLUE = "\033[1;94m"
BHBRIGHTCYAN = "\033[1;36m"
BHBRIGHTGREEN = "\033[1;92m"
BHBRIGHTYELLOW = "\033[1;93m"
BHBRIGHTMAGENTA = "\033[1;95m"
BHBRIGHTCYAN = "\033[1;96m"
BHBOLD = "\033[1;1m"
ITALIC = "\033[3;1;37m"
UNDERLINE = "\033[4;1;37m"
RESET = "\033[0m"

def display_project():
	toggle = False
	with open("after_sed.txt", "r") as f:
		for line in f:
			for char in line:
				if (char == "$"):
					print(f"{BHCYAN} {RESET}", end="")
				elif (char == "^"):
					toggle = True
					print(f"{BHBRIGHTCYAN}", end="")
				elif (char == "¡"):
					toggle = True
					print(f"{BHGREEN}", end="")
				elif (char == "†"):
					toggle = True
					print(f"{UNDERLINE}", end="")
				elif (char == "‡"):
					toggle = True
					print(f"{BHBRIGHTYELLOW}", end="")
				# elif (char == "8"):
				# 	toggle = True
				# 	print(f"{BHORANGE} ", end="")
				elif (char == "¿"):
					toggle = True
					print(f"{BHPINK}", end="")
				elif (char == "`"):
					toggle = False
					print(f"{RESET}{BHWHITE}", end="")
				elif (char == ":"):
					toggle = False
					print(f":{RESET}{BHWHITE}", end="")
				else:
					if toggle == False:
						print(f"{BHWHITE}{char}{RESET}", end="")
					else:
						print(f"{char}", end="")
	print(f"{RESET} {RESET}")



if __name__ == "__main__":
	display_project()
