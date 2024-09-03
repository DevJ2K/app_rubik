import re

def check_notation(notation: str) -> bool:
	"""Function to check if a notation is valid.

	Args:
		notation (str): Notation to check.

	Returns:
		bool: True if is valid notation.
	"""
	regex = r"[FRUBLDfrubld]\d*\'?$"
	match = re.match(regex, notation)
	if match:
		print(match)
		return True

	regex_parenthesis = r"\(([FRUBLDfrubld]\d*\'?$)+\)\d*$"
	return False
