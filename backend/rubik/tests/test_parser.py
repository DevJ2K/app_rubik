import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from parser import check_notation

def test_valid_basic_move_majuscule_notation():
	notations = [
		"U", "U'", "U2", "U2'", "U3", "U3'",
		"D", "D'", "D2", "D2'", "D3", "D3'",
		"R", "R'", "R2", "R2'", "R3", "R3'",
		"L", "L'", "L2", "L2'", "L3", "L3'",
		"F", "F'", "F2", "F2'", "F3", "F3'",
		"B", "B'", "B2", "B2'", "B3", "B3'",
	]
	for notation in notations:
		assert check_notation(notation=notation) == True, f"{notation} is supposed to be a valid notation."

def test_valid_basic_move_miniscule_notation():
	notations = [
		"u", "u'", "u2", "u2'", "u3", "u3'",
		"d", "d'", "d2", "d2'", "d3", "d3'",
		"r", "r'", "r2", "r2'", "r3", "r3'",
		"l", "l'", "l2", "l2'", "l3", "l3'",
		"f", "f'", "f2", "f2'", "f3", "f3'",
		"b", "b'", "b2", "b2'", "b3", "b3'",
	]
	for notation in notations:
		assert check_notation(notation=notation) == False, f"{notation} is supposed to be a invalid notation."


def test_prohibited_slice_move_majuscule_notation():
	notations = [
		"M", "M'", "M2", "M2'", "M3", "M3'",
		"E", "E'", "E2", "E2'", "E3", "E3'",
		"S", "S'", "S2", "S2'", "S3", "S3'",
	]
	for notation in notations:
		assert check_notation(notation=notation) == False, f"{notation} is prohibited for this project, is supposed to be False."


def test_prohibited_slice_move_miniscule_notation():
	notations = [
		"m", "m'", "m2", "m2'", "m3", "m3'",
		"e", "e'", "e2", "e2'", "e3", "e3'",
		"s", "s'", "s2", "s2'", "s3", "s3'",
	]
	for notation in notations:
		assert check_notation(notation=notation) == False, f"{notation} is prohibited for this project, is supposed to be False."


def test_prohibited_axis_move_notation():
	notations = [
		"x", "x'", "x2", "x2'", "x3", "x3'",
		"y", "y'", "y2", "y2'", "y3", "y3'",
		"z", "z'", "z2", "z2'", "z3", "z3'",
	]
	for notation in notations:
		assert check_notation(notation=notation) == False, f"{notation} is prohibited for this project, is supposed to be False."

def test_invalid_axis_move_notation():
	notations = [
		"X", "X'", "X2", "X2'", "X3", "X3'",
		"Y", "Y'", "Y2", "Y2'", "Y3", "Y3'",
		"Z", "Z'", "Z2", "Z2'", "Z3", "Z3'",
	]
	for notation in notations:
		assert check_notation(notation=notation) == False, f"{notation} is supposed to be an invalid notation."

def test_valid_parenthesis_notation():
	notations = [
		"(RUR'U')4",
		"(RU4R'U')4",
		"(RUR'U')14",
		"(RURU)4",
	]
	for notation in notations:
		assert check_notation(notation=notation) == True, f"{notation} is supposed to be a valid notation."

def test_invalid_parenthesis_notation():
	notations = [
		"12(RUR'U')",
		"(RU R' U')4",
		"(R(U)R'U')4",
	]
	for notation in notations:
		assert check_notation(notation=notation) == False, f"{notation} is supposed to be an invalid notation."


def test_invalid_single_notation():
	notations = [
		"UU", "U-2'", "U_2", "2U'", "UD3", "U 3'",
		"3", "3'", "2D", " f' ", "4D"
	]
	for notation in notations:
		assert check_notation(notation=notation) == False, f"{notation} is supposed to be an invalid notation."
