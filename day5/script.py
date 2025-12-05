import numpy as np
import pandas as pd
import datetime
import math

def get_input(testinput=0):
    filename = 'input.txt' if testinput == 0 else f'testinput{testinput}.txt'
    current_day = datetime.datetime.today().day
    with open(f'./day5/{filename}', 'r') as input:
        return input.readlines()
            

def part1():
    input = get_input()
    intervals = [tuple(map(int, elem.strip('\n').split('-'))) for elem in input[:input.index('\n')]]
    ids = [int(elem.strip('\n')) for elem in input[input.index('\n')+1:]]

    fresh_count = 0

    for id in ids:
        for interval in intervals:
            if id in range(interval[0], interval[1]+1):
                fresh_count += 1
                break
            
    return fresh_count


def part2():
    input = get_input()
    intervals = [tuple(map(int, elem.strip('\n').split('-'))) for elem in input[:input.index('\n')]]

    cut_intervals = []
    for low, high in sorted(intervals):
        if cut_intervals:
            if low <= cut_intervals[-1][1]:
                if high > cut_intervals[-1][1]:
                    cut_intervals[-1][1] = high
            else:
                cut_intervals.append([low, high])

        else:
            cut_intervals.append([low, high])

    range_cut_intervals = [range(l, h) for l, h in cut_intervals]

    # Sum up the range lengths and add len(cut_intervals) due to the exclusion of the upper value in range().
    return sum(map(len, range_cut_intervals)) + len(cut_intervals)


def main(is_part1):
    if is_part1:
        return part1()
    else:
        return part2()


print("Part 1:", main(True))
print("Part 2:", main(False))