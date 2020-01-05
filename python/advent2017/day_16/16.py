from collections import namedtuple
from functools import reduce
from string import ascii_lowercase

Move = namedtuple('Move', 'type parameters')

def swap(programs, index1, index2):
    programs[index1], programs[index2] = programs[index2], programs[index1]
    return programs

def parse_move(move_string):
    type_string = move_string[0]
    parameter_string = move_string[1:]

    if type_string == 's':
        return Move('spin', int(parameter_string))
    elif type_string == 'x':
        parameters = [int(x) for x in parameter_string.split('/')]
        return Move('exchange', parameters)
    elif type_string == 'p':
        parameters = parameter_string.split('/')
        return Move('partner', parameters)

def apply_move(programs, move):
    if move.type == 'spin':
        return programs[-move.parameters:] + programs[:-move.parameters]
    elif move.type == 'exchange':
        return swap(programs, move.parameters[0], move.parameters[1])
    elif move.type == 'partner':
        index1 = programs.index(move.parameters[0])
        index2 = programs.index(move.parameters[1])
        return swap(programs, index1, index2)

programs = list(ascii_lowercase[:16])
moves = [parse_move(x.rstrip()) for x in open('input', 'r').read().split(',')]
final_programs = reduce(apply_move, moves, programs)

print("Final order of the programs is {}".format(''.join(final_programs)))

def find_cycle(moves, positions, programs):
    programs = reduce(apply_move, moves, programs)
    position = ''.join(programs)

    if position in positions:
        cycle_start_index = positions.index(position)
        return cycle_start_index, programs, len(positions) - cycle_start_index
    
    positions.append(position)
    return find_cycle(moves, positions, programs)

wanted_iterations = 1000000000
initial_position = ''.join(programs)

cycle_start_index, cycle_start_programs, cycle_length = find_cycle(
    moves, 
    [initial_position], 
    programs
)

needed_iterations = (wanted_iterations - cycle_start_index) % cycle_length
needed_moves = moves * needed_iterations
final_programs = reduce(apply_move, needed_moves, cycle_start_programs)

print("Final order of the programs is {}".format(''.join(final_programs)))
