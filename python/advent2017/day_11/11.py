import sys

sys.setrecursionlimit(100000)

def get_uncountered_steps(forward_step, counter_step, steps):
    forward_steps = [x for x in steps if x == forward_step]
    counter_steps = [x for x in steps if x == counter_step]
    forward_length = len(forward_steps)
    counter_length = len(counter_steps)
    if forward_length > counter_length:
        return forward_steps[counter_length:]
    elif counter_length > forward_length:
        return counter_steps[forward_length:]
    else:
        return []

def combine_steps(first_step, second_step, combined_step, steps):
    if first_step not in steps or second_step not in steps:
        return steps

    steps.remove(first_step)
    steps.remove(second_step)
    steps.append(combined_step)
    return combine_steps(first_step, second_step, combined_step, steps)

steps = open('input', 'r').read().rstrip().split(',')
steps = (
    get_uncountered_steps('n', 's', steps) + 
    get_uncountered_steps('ne', 'sw', steps) + 
    get_uncountered_steps('nw', 'se', steps)
)

# Cheated a bit here and looked what steps we had left in the input, but we
# could do the same for all the other combinations, like 'n' + 'se' == 'ne'
# until we only have 0-2 directions left, just wanted to see if the first part
# could be done this way without using coordinate system and an actual path.
# After the combinations we might have to remove opposites again too, but that
# is an easy step to do after that
steps = combine_steps('s', 'ne', 'se', steps)

print("The end distance was {}".format(len(steps)))

# Part 2

def next_coordinates(current_coordinates, direction):
    if direction == 'n':
        return (current_coordinates[0], current_coordinates[1] - 1)
    elif direction == 'ne':
        return (current_coordinates[0] + 1, current_coordinates[1] - 1)
    elif direction == 'se':
        return (current_coordinates[0] + 1, current_coordinates[1])
    elif direction == 's':
        return (current_coordinates[0], current_coordinates[1] + 1)
    elif direction == 'sw':
        return (current_coordinates[0] - 1, current_coordinates[1] + 1)
    elif direction == 'nw':
        return (current_coordinates[0] - 1, current_coordinates[1])

def calculate_farthest_distance(steps, current_coordinates, farthest_distance):
    if len(steps) == 0:
        return farthest_distance

    farthest_distance = max(distance_to_center(current_coordinates), farthest_distance)
    direction = steps.pop(0)
    current_coordinates = next_coordinates(current_coordinates, direction)
    return calculate_farthest_distance(steps, current_coordinates, farthest_distance)

def distance_to_center(coordinates):
    x = abs(coordinates[0])
    y = abs(coordinates[1])
    z = abs(coordinates[0] + coordinates[1])
    return max([x , y, z])

steps = open('input', 'r').read().rstrip().split(',')
farthest_distance = calculate_farthest_distance(steps, (0, 0), 0)

print("Farthest distance was {}".format(farthest_distance))
