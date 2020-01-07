import sys

sys.setrecursionlimit(100000)

def position(maze, coordinates):
    return maze[coordinates[1]][coordinates[0]]

def next_coordinates(coordinates, direction):
    if direction == 'N':
        return (coordinates[0], coordinates[1] - 1)
    elif direction == 'E':
        return (coordinates[0] + 1, coordinates[1])
    elif direction == 'S':
        return (coordinates[0], coordinates[1] + 1)
    elif direction == 'W':
        return (coordinates[0] - 1, coordinates[1])

def next_direction_at_turn(maze, coordinates, direction):
    if direction == 'S' or direction == 'N':
        east_coordinates = next_coordinates(coordinates, 'E')
        if position(maze, east_coordinates) == '-':
            return 'E'
        else:
            return 'W'
    
    north_coordinates = next_coordinates(coordinates, 'N')
    if position(maze, north_coordinates) == '|':
        return 'N'
    else:
        return 'S'


def find_path(maze, current_coordinates, direction, path, steps):
    current_position = position(maze, current_coordinates)
    if current_position == ' ':
        return path, steps
    elif current_position == '|' or current_position == '-':
        pass
    elif current_position == '+':
        direction = next_direction_at_turn(maze, current_coordinates, direction)
    else:
        path.append(current_position)

    coordinates = next_coordinates(current_coordinates, direction)
    return find_path(maze, coordinates, direction, path, steps + 1)

maze = [list(x.replace('\n', '')) for x in open('input', 'r').readlines()]
start_coordinates = (maze[0].index('|'), 0)
path, steps = find_path(maze, start_coordinates, 'S', [], 0)

print("Path of the packet was {}".format(''.join(path)))
print("Path of the packet had {} steps".format(steps))
