#!/usr/bin/python3

import sys
import pdb

test = ''' _ _ _ _ _ _ _ _ _ _
|X X|X X|   |   |   |
|_X_|_X_|_ _|_ _|_ _|
|X X|X X|   |   |   |
|_X_|_X_|_ _|_ _|_ _|
|X X|X X|   |   |   |
|_X_|_X_|_ _|_ _|_ _|
|X X|X X|   |   |   |
|_X_|_X_|_ _|_ _|_ _|
|X X|X X|X X|X X|X X|
|_X_|_X_|_X_|_X_|_X_|'''

puzzle = []
fixed = []
for line in sys.stdin:
    puzzle.append(line.strip())

for line_index in range(len(puzzle)-1, -1, -2):
    del puzzle[line_index]

for line in puzzle:
    split_line = line[1:-1].split('|')
    to_append = []
    for cell in split_line:
        if cell.startswith('X'):
            to_append.append('X')
        else:
            to_append.append(' ')
    fixed.append(to_append)

clues_down = []
for line in fixed:
    for character_index in range(len(line)):
        line_clues = []
        if line[character_index] == 'X':
            run_length = 1
            #character_index += 1
            while character_index < len(line) and line[character_index] == 'X':
                character_index += 1
                run_length += 1
            line_clues.append(run_length)
    if len(line_clues) == 0:
        clues_down.append(0)
    else:
        clues_down.append(line_clues)

for line in clues_down:
    print(line)
                
            
        
    
