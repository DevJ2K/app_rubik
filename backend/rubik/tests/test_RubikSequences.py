import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from RubikMoves import RubikMoves

def test_extract_repeats_from_sequences_without_parenthesis():
	assert RubikMoves("R'").repeats == 1
	assert RubikMoves("R4'").repeats == 4
	assert RubikMoves("R123").repeats == 123
	assert RubikMoves("L12").repeats == 12
	assert RubikMoves("R").repeats == 1
	assert RubikMoves("R4").repeats == 4

def test_extract_repeats_from_sequences_with_parenthesis():
	assert RubikMoves("(R')").repeats == 1
	assert RubikMoves("(R')4").repeats == 4
	assert RubikMoves("(R1)3").repeats == 3
	assert RubikMoves("(L)12").repeats == 12
	assert RubikMoves("(R)").repeats == 1
	assert RubikMoves("(R5R6)4").repeats == 4

def test_extract_sequences():
	assert RubikMoves("(R')").sequences == ["R'"]
	assert RubikMoves("(R4'U3')3").sequences == ["R'","R'","R'","R'","U'","U'","U'","R'","R'","R'","R'","U'","U'","U'","R'","R'","R'","R'","U'","U'","U'",]
	assert RubikMoves("(R')7").sequences == ["R'","R'","R'","R'","R'","R'","R'",]
	assert RubikMoves("(R'U4)2").sequences == ["R'","U","U","U","U","R'","U","U","U","U",]
