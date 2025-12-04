import numpy as np
import pandas as pd
import datetime
import math

def get_input(testinput=0):
    filename = 'input.txt' if testinput == 0 else f'testinput{testinput}.txt'
    current_day = datetime.datetime.today().day
    with open(f'./day4/{filename}', 'r') as input:
        return input.readlines()
            

def main(is_part1):
    grid = np.array([list(line.strip('\n')) for line in get_input()])
    
    access_count = 0

    while True:
        at_locs = np.where(grid == '@')
        prev_grid = grid.copy()
        
        for loc in list(zip(*at_locs)):
            paper_count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    new_x, new_y = loc[0]+i, loc[1]+j
                    if 0 <= new_x < grid.shape[0] and 0 <= new_y < grid.shape[1] and not i == j == 0:
                        if grid[new_x][new_y] == '@':
                            paper_count += 1

            if paper_count < 4:
                access_count +=1
                if not is_part1:
                    grid[loc[0], loc[1]] = 'x'

        if np.array_equal(grid, prev_grid) or is_part1:
            break
        
    return access_count


print("Part 1:", main(True))
print("Part 2:", main(False))