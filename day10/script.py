import numpy as np
import pandas as pd
import datetime
import math
import re
import gc

def get_input(testinput=0):
    filename = 'input.txt' if testinput == 0 else f'testinput{testinput}.txt'
    current_day = datetime.datetime.today().day
    with open(f'./day10/{filename}', 'r') as input:
        return input.readlines()


class TreeNode():
    def __init__(self, lights, children, layer):
        self.lights = lights
        self.children = children
        self.layer = layer

    def add_children(self, new_children):
        self.children.append(new_children)



def apply_buttons(lights, buttons):
    updated_lights = lights.copy()
    for button in buttons:
        updated_lights[button] = '#' if lights[button] == '.' else '.'
    return updated_lights


def part1():
    input = [line.strip('\n') for line in get_input(0)]#[88:89]
    lights_list = [list(line[1:line.index(']')]) for line in input]
    buttons_raw = [line[line.index(']')+2 : line.index('{')-1].split(' ') for line in input]
    total_presses = 0
    ooo = 0
    for buttons_list, lights in zip(buttons_raw, lights_list):
        buttons = [list(map(int, re.findall(r'\d+', b))) for b in buttons_list]
        layer = 0
        
        lights_permutations = [['.'] * len(lights)]

        idx = 0
        while True:
            perm = lights_permutations.pop(0)            
            # if len(lights_permutations) % 25000 == 0:
            #     print(len(lights_permutations))
            if perm == lights:
                #print(ooo, layer)
                total_presses += layer
                ooo += 1
                break
            else:
                for b in buttons:
                    new_perm = apply_buttons(perm, b)
                    if new_perm not in lights_permutations:
                        lights_permutations.append(new_perm)
                    idx += 1
                if idx >= len(buttons) ** (layer+1):
                    layer += 1 
                    #print('lay', ooo, layer)

    return total_presses





def part2():
    return


def main(is_part1):
    if is_part1:
        return part1()
    else:
        return part2()


print("Part 1:", main(True))
print("Part 2:", main(False))