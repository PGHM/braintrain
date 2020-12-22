from collections import namedtuple
import sys
import math

sys.setrecursionlimit(100000)

Rule = namedtuple('Rule', 'inputs output')

# Parsing

def parse_rule(rule_string):
    parts = [part.strip() for part in rule_string.split("=>")]
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

    row_from_column = ''.join([row[:1] for row in grid])
    column_stripped_grid = [row[1:] for row in grid]
    return transpose(column_stripped_grid, result + [row_from_column])

# Dividing

def divide_grid(grid):
    if len(grid[0]) % 2 == 0:
        divisor = 2
    else:
        divisor = 3

    return _divide_grid(grid, divisor, [])

def _divide_grid(grid, divisor, sub_grids):
    if len(grid) == 0:
        return sub_grids

    new_sub_grids = divide_divisor_height_grid(grid[:divisor], divisor, [])
    return _divide_grid(grid[divisor:], divisor, sub_grids + new_sub_grids)

def divide_divisor_height_grid(grid, divisor, sub_grids):
    if len(grid[0]) == 0:
        return sub_grids

    new_sub_grid = [row[:divisor] for row in grid]
    stripped_grid = [row[divisor:] for row in grid]
    return divide_divisor_height_grid(
        stripped_grid, 
        divisor, 
        sub_grids + [new_sub_grid]
    )

# Combining

def combine_sub_grids(sub_grids):
    sub_grids_per_row = int(math.sqrt(len(sub_grids)))
    return _combine_sub_grids(sub_grids, sub_grids_per_row, [])

def _combine_sub_grids(sub_grids, sub_grids_per_row, grid):
    if len(sub_grids) == 0:
        return grid

    row_of_sub_grids = sub_grids[:sub_grids_per_row]
    new_grid_rows = combine_row_of_sub_grids(row_of_sub_grids, [])
    return _combine_sub_grids(
        sub_grids[sub_grids_per_row:],
        sub_grids_per_row, 
        grid + new_grid_rows
    )

def combine_row_of_sub_grids(sub_grids, new_grid_rows):
    if len(sub_grids[0]) == 0:
        return new_grid_rows
    
    first_rows_from_sub_grids = [x[0] for x in sub_grids]
    new_grid_row = ''.join(first_rows_from_sub_grids)
    sub_grids_without_first_row = [x[1:] for x in sub_grids]
    return combine_row_of_sub_grids(
        sub_grids_without_first_row, 
        new_grid_rows + [new_grid_row]
    )

# Expanding

def expand_grid(grid, iterations_left, rules):
    print(iterations_left)
    if iterations_left == 0:
        return grid
    
    sub_grids = divide_grid(grid)
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

rules = [parse_rule(line.strip()) for line in open('input', 'r').readlines()]
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
