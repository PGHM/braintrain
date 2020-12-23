from collections import defaultdict

# Because the approach taken in part 1 did not work at all because it was far
# too inefficient and I could not figure out a functional way because of
# Python's limitations this became a lesson in Python's cProfiler and making
# things efficient instead of beautiful

# Enums are slow, list index lookups (even in very small lists) are slow, len
# is slow (even in very small lists), making things is slow (obviously)

# First run with the approach like in part 1 took 30 minutes (MacBook Pro
# 2020), this version takes 7.5 seconds (1.9 seconds with PyPy)

CLEAN = '.'
WEAKENED = 'W'
INFECTED = '#'
FLAGGED = 'F'

# First value is movement in x direction, second in y direction
NORTH = (0, 1)
EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)

LEFT_DIRECTIONS = {
    NORTH: WEST,
    EAST: NORTH,
    SOUTH: EAST,
    WEST: SOUTH
}

RIGHT_DIRECTIONS = {
    NORTH: EAST,
    EAST: SOUTH,
    SOUTH: WEST,
    WEST: NORTH
}

def parse_infected_nodes(initial_grid, y, node_statuses):
    if len(initial_grid) == 0:
        return

    row = enumerate(initial_grid[0])
    for node in row:
        if node[1] == INFECTED:
            node_statuses[(node[0], y)] = INFECTED
    
    return parse_infected_nodes(initial_grid[1:], y - 1, node_statuses)

initial_grid = [line.strip() for line in open('input', 'r').readlines()]
node_statuses = defaultdict(lambda: CLEAN)
parse_infected_nodes(initial_grid, 0, node_statuses)

bursts = 10000000
x = len(initial_grid) // 2
y = -(len(initial_grid) // 2)
direction = NORTH
infection_count = 0

for i in range(0, bursts):
    current_location = (x, y)
    node_status = node_statuses[current_location]
    if node_status == CLEAN:
        direction = LEFT_DIRECTIONS[direction]
        node_statuses[current_location] = WEAKENED
    elif node_status == WEAKENED:
        node_statuses[current_location] = INFECTED
        infection_count += 1
    elif node_status == INFECTED:
        direction = RIGHT_DIRECTIONS[direction]
        node_statuses[current_location] = FLAGGED
    elif node_status == FLAGGED: 
        direction = RIGHT_DIRECTIONS[RIGHT_DIRECTIONS[direction]]
        node_statuses[current_location] = CLEAN

    x += direction[0]
    y += direction[1]

print("{} nodes were infected because of new bursts".format(infection_count))
