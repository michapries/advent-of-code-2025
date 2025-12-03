import datetime

def get_input(testinput=0):
    filename = 'input.txt' if testinput == 0 else f'testinput{testinput}.txt'
    current_day = datetime.datetime.today().day
    with open(f'./day3/{filename}', 'r') as input:
        return input.readlines()
            

def main(is_part1):
    input = get_input()
    summed = 0

    num_length = 2 if is_part1 else 12

    for block in input:
        block = [int(jolt) for jolt in list(str(block)) if jolt != '\n']
        
        # Add the jolts to a list that can later be converted to an int.
        jolt_list = []

        first_bracket = 0

        # Always select the respective maximum in the current bracket.
        # Values are inside the bracket if they are to the right of the leftmost selected value
        # while having enough digits to their right to complete the number based on num_length.
        for i in reversed(range(num_length)):
            bracketed_block = block[first_bracket:len(block)-i]
            cur_max = max(bracketed_block)
            jolt_list.append(cur_max)
            first_bracket = block.index(cur_max, first_bracket) + 1

        summed += int(''.join(map(str, jolt_list)))

    return summed


print("Part 1:", main(True))
print("Part 2:", main(False))