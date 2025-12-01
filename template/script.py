import numpy as np
import pandas as pd
import datetime
import math

def get_day():
    return datetime.datetime.today().day


def get_input(testinput=0):
    filename = 'input.txt' if testinput == 0 else f'testinput{testinput}.txt'
    with open(f'./day{get_day()}/{filename}', 'r') as input:
        return input.readlines()
            

def part1():
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