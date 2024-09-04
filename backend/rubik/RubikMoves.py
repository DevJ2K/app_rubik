from parser import check_notation, check_basic_notation, check_parenthesis_notation
from ErrorManager import NotationError
import re

class RubikMoves:
	"""The class to init a rubik sequence
	"""
	def __init__(self, notation: str) -> None:
		self.notation: str = notation
		self.repeats: int = 1
		self.sequences: list[str] = []
		if check_notation(notation) == False:
			raise NotationError(f"{notation} is not a valid notation.")

		self.extract_repeats()
		self.extract_sequences()


	def extract_repeats(self) -> int:
		match = re.search(r"\d+\'?$", self.notation)
		if match:
			repeats = re.sub(r'\'', '', match.group())
			self.repeats = int(repeats)
		# 	print(self.repeats)
		# else:
		# 	print("No repeat.")

		return self.repeats

	def __get_move(self, move) -> list[str]:
		match_nb = re.search(r"\d+", move)
		repeats = 1
		if match_nb:
			repeats = re.sub(r'\'', '', match_nb.group())
			repeats = int(repeats)

		clear_move = re.sub(r"\d", '', move)
		# print(f"{move} | {clear_move} : {repeats}")
		return [clear_move for i in range(repeats)]

	def extract_sequences(self) -> list[str]:
		self.sequences.clear()
		regex = r"[FRUBLDfrubld]\d*\'?"
		moves_match = re.findall(regex, self.notation)
		if moves_match:
			print(moves_match)
			for move in moves_match:
				self.sequences += self.__get_move(move)
		self.sequences *= self.repeats
		return self.sequences

	def __str__(self) -> str:
		return self.notation

	def __repr__(self) -> str:
		return self.__str__()


if __name__ == "__main__":
	RubikMoves("r4'")
	RubikMoves("r'")
	RubikMoves("(r')")
	RubikMoves("(RU42R'U'R41')4")
	pass
