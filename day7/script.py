import numpy as np
import pandas as pd
import datetime
import math

def get_input(testinput=0):
    filename = 'input.txt' if testinput == 0 else f'testinput{testinput}.txt'
    current_day = datetime.datetime.today().day
    with open(f'./day7/{filename}', 'r') as input:
        return input.readlines()
            

def part1():
    grid = np.array([list(line.strip('\n')) for line in get_input()])
    total_splits = 0

    for i in range(grid.shape[0]):
        if i > 0:
            splitter_indices = np.where(grid[i] == '^')[0]               
            
            for splitter_idx in splitter_indices:
                if grid[i-1][splitter_idx] == '|':
                    grid[i, splitter_idx-1] = '|'
                    grid[i, splitter_idx+1] = '|'
                    total_splits += 1
            
            prev_line_beams = np.where((grid[i-1] == '|') | (grid[i-1] == 'S'))[0]
            for beam_idx in prev_line_beams:
                if grid[i][beam_idx] == '.':
                    grid[i, beam_idx] = '|'

    return total_splits


def part2():
    grid = np.array([list(line.strip('\n')) for line in get_input()])

    # Ugle formatting to have an int array ¯\_(ツ)_/¯
    grid[grid == '.'] = 0
    grid[grid == '^'] = 5
    grid[grid == 'S'] = 3
    
    grid = grid.astype(int)

    grid[grid == 5] = -1
    grid[grid == 3] = -2

    for i in range(grid.shape[0]):
        if i > 0:
            splitter_indices = np.where(grid[i] == -1)[0]               

            for splitter_idx in splitter_indices:
                if grid[i-1][splitter_idx] != 0:                    
                    grid[i, splitter_idx-1] = grid[i, splitter_idx-1] + grid[i-1][splitter_idx]
                    grid[i, splitter_idx+1] = grid[i, splitter_idx+1] + grid[i-1][splitter_idx]

        
            prev_line_beams = np.where((grid[i-1] != -1) & ((grid[i-1] != 0) | (grid[i-1] == -2)))[0]
            for beam_idx in prev_line_beams:
                if grid[i-1][beam_idx] == -2:
                    grid[i, beam_idx] = 1
                elif grid[i][beam_idx] != -1:
                    grid[i, beam_idx] += grid[i-1][beam_idx]

    return sum(map(int, grid[-1]))


def main(is_part1):
    if is_part1:
        return part1()
    else:
        return part2()


print("Part 1:", main(True))
print("Part 2:", main(False))