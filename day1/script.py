import numpy as np
import pandas as pd
import datetime
import math

def get_day():
    return datetime.datetime.today().day


def get_input(testinput=0):
    filename = 'input.txt' if testinput == 0 else f'testinput{testinput}.txt'
    with open(f'./day1/{filename}', 'r') as input:
        return input.readlines()
            

def main(is_part1):
    input = get_input()
    dial_pos = 50
    zero_count = 0

    for move in input:
        num = int(move[1:])
        is_turn_left = move[0] == 'L'      # True if turn is to the left.
        
        new_dial_pos = dial_pos - num if is_turn_left else dial_pos + num
        
        if is_part1:
            if new_dial_pos % 100 == 0:
                zero_count += 1
        
        elif not is_part1:
            zero_count += abs(int(new_dial_pos / 100))

            # Add one more zero to the count for negative numbers.
            if new_dial_pos / 100 <= 0 and dial_pos != 0:
                zero_count += 1
        
        dial_pos = new_dial_pos % 100
        
    return zero_count


print("Part 1:", main(True))
print("Part 2:", main(False))