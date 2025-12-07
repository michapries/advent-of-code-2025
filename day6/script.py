import numpy as np
import pandas as pd
import datetime
import math

def get_input(testinput=0):
    filename = 'input.txt' if testinput == 0 else f'testinput{testinput}.txt'
    current_day = datetime.datetime.today().day
    with open(f'./day6/{filename}', 'r') as input:
        return input.readlines()
            

def main(is_part1):
    if is_part1:
        input = [list(filter(None, line.strip('\n').split(' '))) for line in get_input()]
        nums, operators = np.array([list(map(int, line)) for line in input[:-1]]), input[-1]
        grand_total = 0
        for i in range(nums.shape[1]):
            grand_total += math.prod(nums[:, i]) if operators[i] == '*' else sum(nums[:, i])

        return grand_total
    else:
        input = [list(line.strip('\n')) for line in get_input()]
        nums, operators = np.array(input[:-1]).T, [elem for elem in input[-1] if elem != ' ']
        
        op_idx = 0
        grand_total = 0

        intermediate_nums = []

        for line_idx, line in enumerate(nums):
            line_num = ''.join(line).strip()
            if not line_num:
                grand_total += math.prod(intermediate_nums) if operators[op_idx] == '*' else sum(intermediate_nums)
                op_idx += 1
                intermediate_nums = []
            else:
                intermediate_nums.append(int(line_num))
                if line_idx == len(nums)-1:
                    grand_total += math.prod(intermediate_nums) if operators[op_idx] == '*' else sum(intermediate_nums)

        return grand_total


print("Part 1:", main(True))
print("Part 2:", main(False))