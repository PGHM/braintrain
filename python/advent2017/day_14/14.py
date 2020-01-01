import sys, os, itertools

sys.path.append(os.path.abspath("../day_10"))
sys.path.append(os.path.abspath("../day_12"))

from day_10 import knot_hash
from day_12 import Program, get_all_groups

input_string = 'ffayrhll'
input_strings = ["{}-{}".format(input_string, index) for index in range(0, 128)]
knot_hashes = [knot_hash(x) for x in input_strings]
grid = [list(format(int(x, 16), "0128b")) for x in knot_hashes]
flat_grid = list(itertools.chain.from_iterable(grid))

used_squares = list(filter(lambda x: x == '1', flat_grid))

print("There are {} grids used".format(len(used_squares)))

def get_connected_neighbour(grid, coordinates, x_diff, y_diff):
    x = coordinates[0] + x_diff
    y = coordinates[1] + y_diff
    
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
        return None

    neighbour = grid[x][y]
    if neighbour == '0':
        return None

    return coordinates_to_program_name((x, y))

def coordinates_to_program_name(coordinates):
    return "({}, {})".format(coordinates[0], coordinates[1])

def grid_node_to_program_key_value(grid, coordinates):
    node = grid[coordinates[0]][coordinates[1]]
    program_name = coordinates_to_program_name(coordinates)

    connected_neighbours = [
        get_connected_neighbour(grid, coordinates, 0, -1),
        get_connected_neighbour(grid, coordinates, 1, 0),
        get_connected_neighbour(grid, coordinates, 0, 1),
        get_connected_neighbour(grid, coordinates, -1, 0)
    ]

    return (
        program_name, 
        Program(program_name, [x for x in connected_neighbours if x is not None])
    )

programs = dict([
    grid_node_to_program_key_value(grid, (x, y))
    for x in range(0, len(grid[0]))
    for y in range(0, len(grid))
    if grid[x][y] != '0'
])

program_names = set(programs.keys())
groups = get_all_groups(program_names, programs, [])

print("There are {} regions in the grid".format(len(groups)))
