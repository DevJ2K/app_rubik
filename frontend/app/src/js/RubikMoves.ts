function checkBasicNotation(notation: string) {
    // Check basic notation
    const regex = /^[FRUBLD]\d*'?$/;
    return regex.test(notation);
}

function checkParenthesisNotation(notation: string) {
    // Check with parenthesis
    const regexParenthesis = /^\(([FRUBLD]\d*'?)+\)\d*$/;
    return regexParenthesis.test(notation);
}

function checkNotation(notation: string) {
    /**
     * Function to check if a notation is valid.
     *
     * Args:
     *   notation (string): Notation to check.
     *
     * Returns:
     *   boolean: True if the notation is valid.
     */
    return checkBasicNotation(notation) || checkParenthesisNotation(notation);
}


class RubikMoves {
    /**
     * The class to init a rubik sequence
     * @param {string} notation
     */

	notation: string;
	repeats: number;
	sequences: Array<string>;
    constructor(notation: string) {
        this.notation = notation;
        this.repeats = 1;
        this.sequences = [];

        if (!checkNotation(notation)) {
            throw new Error(`${notation} is not a valid notation.`);
        }

        this.extractRepeats();
        this.extractSequences();
    }

    extractRepeats() {
        const match = this.notation.match(/\d+'?$/);
        if (match) {
            const repeats = match[0].replace(/'/g, '');
            this.repeats = parseInt(repeats, 10);
        }
        return this.repeats;
    }

    private getMove(move: string) {
        const matchNb = move.match(/\d+/);
        let repeats = 1;
        if (matchNb) {
            repeats = parseInt(matchNb[0].replace(/'/g, ''), 10);
        }

        const clearMove = move.replace(/\d/, '');
        return Array(repeats).fill(clearMove);
    }

    extractSequences() {
        this.sequences = [];
        const regex = /[FRUBLDfrubld]\d*'?/g;
        const movesMatch = this.notation.match(regex);

        if (movesMatch) {
            for (const move of movesMatch) {
                this.sequences = this.sequences.concat(this.getMove(move));
            }
        }

		// console.log("OLD SEQ : " + this.sequences);

		// console.log(this.repeats);
		const tmp_sequences = this.sequences;
		if (this.notation.match(/\)\d+$/)) {
			for (let i = 1; i < this.repeats; i++) {
				this.sequences = this.sequences.concat(tmp_sequences);
			}
		}
		// console.log("NEW SEQ : " + this.sequences);
        return this.sequences;
    }

    toString() {
        return this.notation;
    }

    toJSON() {
        return this.toString();
    }
}

export { RubikMoves, checkNotation }
