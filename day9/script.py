import numpy as np
import pandas as pd
import datetime
import math

def get_input(testinput=0):
    filename = 'input.txt' if testinput == 0 else f'testinput{testinput}.txt'
    current_day = datetime.datetime.today().day
    with open(f'./day9/{filename}', 'r') as input:
        return input.readlines()
            

def main(is_part1):
    input = [tuple(map(int, line.strip('\n').split(','))) for line in get_input(0)]
    max_area = 0
    for i, (Ax, Ay) in enumerate(input):
        for Bx, By in input[i+1:]:
            area = (abs(Ax - Bx)+1) * (abs(Ay - By)+1)
            if area > max_area:
                if is_part1:
                    max_area = area

    return max_area


print("Part 1:", main(True))
print("Part 2:", main(False))