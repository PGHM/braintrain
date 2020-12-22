from collections import namedtuple
import sys
import math

sys.setrecursionlimit(100000)

Rule = namedtuple('Rule', 'inputs output')

# Parsing

def parse_rule(rule_string):
    parts = [x.strip() for x in  rule_string.split("=>")]
    rule_output = parts[1].split("/")
    
    rule_default_input = parts[0].split("/")
    rule_default_input_90 = rotate(rule_default_input)
    rule_default_input_180 = rotate(rule_default_input_90)
    rule_default_input_270 = rotate(rule_default_input_180)
    rule_flipped_input = [''.join(reversed(x)) for x in rule_default_input]
    rule_flipped_input_90 = rotate(rule_flipped_input)
    rule_flipped_input_180 = rotate(rule_flipped_input_90)
    rule_flipped_input_270 = rotate(rule_flipped_input_180)

    inputs = [
        rule_default_input,
        rule_default_input_90,
        rule_default_input_180,
        rule_default_input_270,
        rule_flipped_input,
        rule_flipped_input_90,
        rule_flipped_input_180,
        rule_flipped_input_270
    ]
    return Rule(inputs, rule_output)

# "Math"

def rotate(grid):
    reversed_grid = list(reversed(grid))
    return transpose(reversed_grid, [])

def transpose(grid, result):
    if len(grid[0]) == 0:
        return result

    row_from_column = ''.join([x[:1] for x in grid])
    column_stripped_grid = [x[1:] for x in grid]
    return transpose(column_stripped_grid, result + [row_from_column])

# Dividing

def divide_grid(grid, divisor, sub_grids):
    if len(grid) == 0:
        return sub_grids

    sub_grids += divide_divisor_height_grid(grid[:divisor], divisor, [])
    return divide_grid(grid[divisor:], divisor, sub_grids)

def divide_divisor_height_grid(grid, divisor, sub_grids):
    if len(grid[0]) == 0:
        return sub_grids

    new_sub_grid = [x[:divisor] for x in grid]
    stripped_grid = [x[divisor:] for x in grid]
    return divide_divisor_height_grid(
        stripped_grid, 
        divisor, 
        sub_grids + [new_sub_grid]
    )

# Combining

def combine_sub_grids(sub_grids):
    sub_grids_per_row = int(math.sqrt(len(sub_grids)))
    return _combine_sub_grids(sub_grids, sub_grids_per_row, [])

def _combine_sub_grids(sub_grids, sub_grids_per_row, result):
    if len(sub_grids) == 0:
        return result

    row_of_sub_grids = sub_grids[:sub_grids_per_row]
    result += combine_sub_grid_row(row_of_sub_grids, [])
    return _combine_sub_grids(
        sub_grids[sub_grids_per_row:],
        sub_grids_per_row, 
        result
    )

def combine_sub_grid_row(row_of_sub_grids, result):
    if len(row_of_sub_grids[0]) == 0:
        return result
    
    first_rows = [x[0] for x in row_of_sub_grids]
    combined_first_rows = ''.join(first_rows)
    result += [combined_first_rows]
    stripped_row_of_sub_grids = [x[1:] for x in row_of_sub_grids]
    return combine_sub_grid_row(stripped_row_of_sub_grids, result)

# Expanding

def expand_grid(grid, iterations_left, rules):
    print(iterations_left)
    if iterations_left == 0:
        return grid

    if len(grid[0]) % 2 == 0:
        divisor = 2
    else:
        divisor = 3
    
    sub_grids = divide_grid(grid, divisor, [])
    expanded_sub_grids = [expand_sub_grid(x, rules) for x in sub_grids]
    new_grid = combine_sub_grids(expanded_sub_grids)
    return expand_grid(new_grid, iterations_left - 1, rules)

def expand_sub_grid(sub_grid, rules):
    correct_rule = [x for x in rules if rule_matches_grid(sub_grid, x)][0]
    return correct_rule.output

def rule_matches_grid(grid, rule):
    return any([x == grid for x in rule.inputs])

# Counting

def count_pixels_on(grid):
    all_pixels = ''.join(grid)
    return len([x for x in all_pixels if x == '#'])

# Main

grid = [
    '.#.',
    '..#',
    '###'
]

first_part_iterations = 5
second_part_extra_iterations = 13

rules = [parse_rule(x.rstrip()) for x in open('input', 'r').readlines()]
first_part_final_grid = expand_grid(grid, first_part_iterations, rules)
second_part_final_grid = expand_grid(
    first_part_final_grid,
    second_part_extra_iterations, 
    rules
)

first_part_pixels_on = count_pixels_on(first_part_final_grid)
second_part_pixels_on = count_pixels_on(second_part_final_grid)

print(
    "Pixels on in first part: {}, and second part: {}".format(
        first_part_pixels_on, 
        second_part_pixels_on
    )
)
