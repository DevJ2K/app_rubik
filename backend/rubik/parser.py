import re

def check_basic_notation(notation: str) -> bool:
	# Check basic notation
	regex = r"[FRUBLD]\d*\'?$"
	match = re.match(regex, notation)
	if match:
		return True
	return False

def check_parenthesis_notation(notation: str) -> bool:
	# Check with parenthesis
	regex_parenthesis = r"\(([FRUBLD]\d*\'?)+\)\d*$"
	match = re.match(regex_parenthesis, notation)
	if match:
		return True
	return False

def check_notation(notation: str) -> bool:
	"""Function to check if a notation is valid.

	Args:
		notation (str): Notation to check.

	Returns:
		bool: True if is valid notation.
	"""
	return check_basic_notation(notation) or check_parenthesis_notation(notation)


if __name__ == "__main__":
	print(check_notation("(RU4R'U')4"))
	pass
