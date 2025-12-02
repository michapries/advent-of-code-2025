import numpy as np
import pandas as pd
import datetime
import math
from sympy import divisors

def get_input(testinput=0):
    filename = 'input.txt' if testinput == 0 else f'testinput{testinput}.txt'
    current_day = datetime.datetime.today().day
    with open(f'./day2/{filename}', 'r') as input:
        return input.readlines()
            

def main(is_part1):
    input = get_input()[0]
    intervals = [tuple(map(int, range.split('-'))) for range in input.split(',')]
    invalid_ids = list()
    
    for interval in intervals:
        for val in range(interval[0], interval[1]+1):
            list_val = list(str(val))        # Make the value a list
            val_len = len(list_val)
            
            # Get non-remainder divisors of val_len to obtain lengths of possible sub vals.
            divs = [div for div in divisors(val_len)]

            # For part one, we only want to check the divisor that splits the number into two equal length parts.
            if is_part1:
                divs = [div for div in divs if div == val_len/2]

            for div in divs:
                # Split the value in div equal lenght parts.
                sub_vals_of_length_div = [list_val[i:i+div] for i in range(0, val_len, div)]

                # Check if all elements of the list are equal.
                # Could be done more efficiently but this does the job for this challenge.
                if sub_vals_of_length_div.count(sub_vals_of_length_div[0]) == len(sub_vals_of_length_div) != 1:
                    invalid_ids.append(val)

    return sum(set(invalid_ids))

print("Part 1:", main(True))
print("Part 2:", main(False))