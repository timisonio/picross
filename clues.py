#!/usr/bin/python3

import sys
import pdb

block_character = 'X'
gap_character = ' '


def read_puzzle(source):
    # source is some iterable
    # like sys.stdin
    # or a list of strings
    puzzle = []
    line_index = 0
    for line in source:
        if line_index % 2 != 0:  # with this format, skip lines # mod 2 == 0
            line = (
                line.strip()  # consume newlines
                [1:-1]  # disregard first and last character
                .split('|')  # split on pipes
            )
            to_append = []
            for cell in line:
                if cell.startswith(block_character):
                    to_append.append(block_character)
                else:
                    to_append.append(gap_character)
            puzzle.append(to_append)
        line_index += 1
    return puzzle


def make_clues_down(puzzle):
    clues_down = []
    for line in puzzle:
        character_index = 0
        line_clues = []

        while character_index < len(line):
            run_length = 0
            while character_index < len(line) and
            line[character_index] == block_character:
                # begin a string of blocks
                character_index += 1
                run_length += 1
            if run_length > 0:
                line_clues.append(run_length)
            character_index += 1

        if len(line_clues) == 0:
            # no clues in this entire line
            clues_down.append(0)
        else:
            # some clues in this line
            clues_down.append(line_clues)
    return clues_down


def make_clues(puzzle):
    # simple wrapper for make_clues_down
    # zip(*A) returns the transpose of the 2D array!
    return make_clues_down(puzzle), make_clues_down(zip(*puzzle))

if __name__ == "__main__":
    puzzle = read_puzzle(sys.stdin)
    print(make_clues(puzzle))
