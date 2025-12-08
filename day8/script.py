import numpy as np
import pandas as pd
import datetime
import math

def get_input(testinput=0):
    filename = 'input.txt' if testinput == 0 else f'testinput{testinput}.txt'
    current_day = datetime.datetime.today().day
    with open(f'./day{current_day}/{filename}', 'r') as input:
        return input.readlines()
            

def main(is_part1):
    input = [tuple(map(int, line.strip('\n').split(','))) for line in get_input()]
    distances = {}

    # Calculate all distances.
    for coords1 in input:
        for coords2 in input:
            if coords1 != coords2 and (coords2, coords1) not in distances.keys():
                distances[(coords1, coords2)] = np.linalg.norm(np.subtract(coords1, coords2))

    cliques = []

    # Sort the distances.
    sorted_distances = sorted(distances.items(), key=lambda item: item[1])
    if is_part1:
        sorted_distances = sorted_distances[:1000]

    for nodes, dist in sorted_distances:
        source_clique_idx = -1
        target_clique_idx = -1
        for idx, clique in enumerate(cliques):
            if nodes[0] in clique:
                source_clique_idx = idx
            if nodes[1] in clique:
                target_clique_idx = idx
            
        if source_clique_idx == target_clique_idx == -1:
            cliques.append([nodes[0], nodes[1]])
        elif source_clique_idx == -1 and target_clique_idx != -1:
            cliques[target_clique_idx].append(nodes[0])
        elif source_clique_idx != -1 and target_clique_idx == -1:
            cliques[source_clique_idx].append(nodes[1])
        elif source_clique_idx != target_clique_idx:
            cliques[source_clique_idx].extend(cliques[target_clique_idx])
            del cliques[target_clique_idx]
        
        if not is_part1 and len(cliques[0]) == len(input):
            return nodes[0][0] * nodes[1][0]

    
    return math.prod(map(len, sorted(cliques, key=len, reverse=True)[:3])) if is_part1 else None


print("Part 1:", main(True))
print("Part 2:", main(False))