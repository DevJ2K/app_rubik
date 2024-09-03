import re

def check_notation(notation: str) -> bool:
	"""Function to check if a notation is valid.

	Args:
		notation (str): Notation to check.

	Returns:
		bool: True if is valid notation.
	"""

	# Check basic notation
	regex = r"[FRUBLDfrubld]\d*\'?$"
	match = re.match(regex, notation)
	if match:
		print(match)
		return True

	# Check with parenthesis
	regex_parenthesis = r"\(([FRUBLDfrubld]\d*\'?)+\)\d*$"
	match = re.match(regex_parenthesis, notation)
	if match:
		print(match)
		return True
	return False

if __name__ == "__main__":
	# check_notation("(RUR'U')4")
	pass
