import numpy as np
import pandas as pd
import datetime
import math

def get_input(testinput=0):
    filename = 'input.txt' if testinput == 0 else f'testinput{testinput}.txt'
    current_day = datetime.datetime.today().day
    with open(f'./day{current_day}/{filename}', 'r') as input:
        return input.readlines()
            

def part1():
    input = [line.strip('\n') for line in get_input(1)]
    lights_list = [line[1:line.index(']')] for line in input]
    print(lights_list)
    buttons_list = [line[line.index(']')+2 : line.index('{')-1].split(' ') for line in input]
    buttons_list = [buttons.split(',') for buttons in buttons_list]
    print(buttons_list)
    return


def part2():
    return


def main(is_part1):
    if is_part1:
        return part1()
    else:
        return part2()


print("Part 1:", main(True))
print("Part 2:", main(False))